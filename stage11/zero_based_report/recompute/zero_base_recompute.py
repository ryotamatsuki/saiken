#!/usr/bin/env python3
"""Stage 11 zero-based reproducible calculations.

Inputs are permitted factual/structured GitHub datasets only.
No prior report, prior scenario file, prior ladder file, or report-derived QA is imported.
Run from repository root.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "stage11" / "zero_based_report" / "recompute"
OUT.mkdir(parents=True, exist_ok=True)

bal = pd.read_csv(ROOT / "stage4" / "processed" / "ehime_fund_balance_R2_R6.csv")
sub = pd.read_csv(ROOT / "stage4" / "processed" / "ehime_fund_substitution_period_totals.csv")
sub_long = pd.read_csv(ROOT / "stage4" / "processed" / "ehime_fund_substitution_R3_R6_long.csv")
wd = pd.read_csv(ROOT / "stage4" / "processed" / "ehime_R8_fund_withdrawals.csv")
wd = wd[wd["fund_name"] != "TOTAL"].copy()

x = sub["amount_oku_yen"]
summary = pd.DataFrame([{
    "n": len(x), "min": x.min(), "q1": x.quantile(.25), "mean": x.mean(),
    "median": x.median(), "p75": x.quantile(.75), "p90": x.quantile(.90),
    "p95": x.quantile(.95), "max": x.max(), "std_sample": x.std(ddof=1),
    "cv_pct": x.std(ddof=1) / x.mean() * 100
}])
summary.to_csv(OUT / "substitution_distribution.csv", index=False)

season = sub.groupby("period")["amount_oku_yen"].agg(["mean","std","min","max"]).reset_index()
season["cv_pct"] = season["std"] / season["mean"] * 100
season.to_csv(OUT / "substitution_seasonality.csv", index=False)

sub_long["amount_oku_yen"] = sub_long["amount_m_yen"] / 100
fund_use = sub_long.groupby("fund").agg(
    occurrences=("amount_oku_yen","size"),
    years=("fiscal_year","nunique"),
    total_oku_yen=("amount_oku_yen","sum"),
    avg_when_used_oku_yen=("amount_oku_yen","mean"),
    max_when_used_oku_yen=("amount_oku_yen","max"),
).reset_index().sort_values("total_oku_yen", ascending=False)
fund_use["share_of_all_substitution_pct"] = fund_use["total_oku_yen"] / fund_use["total_oku_yen"].sum() * 100
fund_use.to_csv(OUT / "substitution_fund_concentration.csv", index=False)

wd = wd.sort_values("R8_budget_withdrawal_oku_yen", ascending=False)
total_wd = wd["R8_budget_withdrawal_oku_yen"].sum()
rows = []
for n in [1,3,5,7,10,15]:
    s = wd.head(n)["R8_budget_withdrawal_oku_yen"].sum()
    rows.append({"top_n":n,"amount_oku_yen":s,"share_pct":s/total_wd*100})
pd.DataFrame(rows).to_csv(OUT / "r8_withdrawal_concentration.csv", index=False)

fy_total = (bal.set_index("fiscal_year")["fund_total_m_yen"] / 100).to_dict()
yrmax = sub.groupby("fiscal_year")["amount_oku_yen"].max().to_dict()
rows = []
for fy in ["R3","R4","R5","R6"]:
    r = fy_total[fy] - yrmax[fy]
    rows.append({
        "fiscal_year":fy,
        "year_end_fund_total_oku_yen":fy_total[fy],
        "same_year_max_substitution_oku_yen":yrmax[fy],
        "statistical_residual_oku_yen":r,
        "residual_pct":r/fy_total[fy]*100,
    })
pd.DataFrame(rows).to_csv(OUT / "historical_residuals.csv", index=False)

r6_total = float(fy_total["R6"])
levels = {
    "mean":x.mean(), "median":x.median(), "p75":x.quantile(.75),
    "p90":x.quantile(.90), "p95":x.quantile(.95), "historical_max":x.max()
}
rows = []
for k,v in levels.items():
    rows.append({
        "liquidity_reference":k,
        "reference_need_oku_yen":v,
        "r6_statistical_residual_oku_yen":r6_total-v,
        "residual_pct_of_r6_fund":(r6_total-v)/r6_total*100,
    })
pd.DataFrame(rows).to_csv(OUT / "statistical_capacity_outer_envelope.csv", index=False)

for c in [
    "fiscal_adjustment_m_yen","debt_reduction_m_yen","facility_renewal_m_yen",
    "school_environment_m_yen","digital_m_yen","medical_care_m_yen",
    "disaster_resilience_m_yen"
]:
    bal[c + "_share_pct"] = bal[c] / bal["fund_total_m_yen"] * 100
bal.to_csv(OUT / "ehime_balance_dynamics.csv", index=False)

dep = pd.read_csv(ROOT / "stage7" / "external_benchmark_market_evidence" / "market_data" / "deposit_rates_by_maturity.csv")
jgb = pd.read_csv(ROOT / "stage7" / "external_benchmark_market_evidence" / "market_data" / "jgb_yields_by_maturity.csv")
aug = float(dep.loc[dep["period"]=="2026-08","time_deposit_10m_plus_1y_pct"].iloc[0])
one = float(jgb.loc[jgb["tenor_years"]==1,"yield_pct"].iloc[0])
observed_1y_reference_spread_bp = (one - aug) * 100

def mod_duration(maturity, y_pct):
    y = y_pct / 100
    if maturity == 1:
        return 1/(1+y)
    coupon = y * 100
    pvs = []
    for t in range(1, int(maturity)+1):
        cash = coupon + (100 if t == maturity else 0)
        pvs.append((t, cash/(1+y)**t))
    price = sum(p for _,p in pvs)
    mac = sum(t*p for t,p in pvs) / price
    return mac/(1+y)

yields = {int(r.tenor_years):float(r.yield_pct) for _,r in jgb.iterrows()}
durations = {t:mod_duration(t,yields[t]) for t in yields}

# Stage 11 comparison structures only; not optimized and not recommendations.
structures = {
    "短期中心": {1:.50, 2:.35, 5:.15, 10:0, 20:0},
    "中短期中心": {1:.25, 2:.35, 5:.30, 10:.10, 20:0},
    "均等分散": {1:.20, 2:.20, 5:.20, 10:.20, 20:.20},
    "中長期比重": {1:.10, 2:.15, 5:.30, 10:.35, 20:.10},
}
rows = []
for name,w in structures.items():
    wy = sum(w.get(t,0)*yields[t] for t in yields)
    wm = sum(w.get(t,0)*t for t in yields)
    md = sum(w.get(t,0)*durations[t] for t in yields)
    row = {
        "structure":name,
        "weighted_maturity_years":wm,
        "weighted_reference_yield_pct":wy,
        "modified_duration_proxy":md,
    }
    for bp in [25,50,100,-50]:
        row[f"price_effect_{bp:+}bp_pct"] = -md*(bp/10000)*100
    rows.append(row)
pd.DataFrame(rows).to_csv(OUT / "illustrative_maturity_structures.csv", index=False)

rows = []
for amount in [100,300,500]:
    for bp in [10,25,50,observed_1y_reference_spread_bp]:
        inc_oku = amount * bp / 10000
        rows.append({
            "amount_oku_yen":amount,
            "incremental_spread_bp":bp,
            "annual_incremental_income_oku_yen":inc_oku,
            "annual_incremental_income_million_yen":inc_oku*100,
        })
pd.DataFrame(rows).to_csv(OUT / "income_sensitivity.csv", index=False)

print("observed_1y_reference_spread_bp", observed_1y_reference_spread_bp)
print("ZERO-BASE RECOMPUTE COMPLETE")
