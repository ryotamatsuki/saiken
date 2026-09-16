#!/usr/bin/env python3
"""Stage 10 reproducible calculations. Run from repository root."""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
P4 = ROOT / "stage4" / "processed"
OUT = ROOT / "stage10" / "deep_analytical_execution"

sub = pd.read_csv(P4 / "ehime_fund_substitution_period_totals.csv")
withdraw = pd.read_csv(P4 / "ehime_R8_fund_withdrawals.csv")
bal = pd.read_csv(P4 / "ehime_fund_balance_R2_R6.csv")

x = sub["amount_oku_yen"]
print("substitution_n", len(x))
for name, val in {
    "mean": x.mean(), "median": x.median(), "p75": x.quantile(.75),
    "p90": x.quantile(.90), "p95": x.quantile(.95), "max": x.max()
}.items(): print(name, round(float(val), 6))

season = sub.groupby("period")["amount_oku_yen"].agg(["mean", "std"])
season["cv"] = season["std"] / season["mean"]
print("\nseasonal\n", season)

year_max = sub.groupby("fiscal_year")["amount_oku_yen"].max()
year_totals = bal.set_index("fiscal_year")["fund_total_m_yen"] / 100
same_year = pd.DataFrame({"fund_total_oku_yen": year_totals, "max_substitution_oku_yen": year_max}).dropna()
same_year["residual_oku_yen"] = same_year.fund_total_oku_yen - same_year.max_substitution_oku_yen
same_year["residual_pct"] = same_year.residual_oku_yen / same_year.fund_total_oku_yen * 100
print("\nsame_year_residual\n", same_year)
print("residual_mean", same_year.residual_oku_yen.mean())
print("residual_median", same_year.residual_oku_yen.median())

# R8 withdrawal concentration excluding TOTAL row.
w = withdraw[withdraw.fund_name != "TOTAL"].sort_values("R8_budget_withdrawal_oku_yen", ascending=False)
total = w.R8_budget_withdrawal_oku_yen.sum()
for n in [3,5,7,10,15]:
    s = w.head(n).R8_budget_withdrawal_oku_yen.sum()
    print(f"top{n}", round(s,6), round(s/total*100,6))

# Scenario calculations. Distinguish total bonds from bonds locked >1y.
P75 = float(x.quantile(.75)); P90 = float(x.quantile(.90)); HMAX = float(x.max())
for basis, total_fund in [("R6_confirmed_actual", 1302.27675), ("R8_year_end_budget_forecast", 1254.0)]:
    print("\n", basis)
    for bond_total in [300,400,435.32,480,500,600]:
        gap = HMAX - P75
        max_long = max(0, total_fund - HMAX)
        if bond_total <= max_long:
            long_bond = bond_total; within1 = 0; near = total_fund - P75 - bond_total; immediate = P75
        elif bond_total <= total_fund - P75:
            long_bond = max_long; within1 = bond_total-long_bond; near = total_fund-P75-bond_total; immediate=P75
        else:
            within1 = min(gap,bond_total); long_bond=bond_total-within1; near=0; immediate=total_fund-bond_total
        liquid1 = immediate+near+within1
        print(bond_total, round(immediate,4), round(near,4), round(within1,4), round(long_bond,4), round(liquid1/HMAX*100,3))

# Stress residuals using R8 year-end budget forecast denominator.
for label, need in [("P75",P75),("P90",P90),("historical_max",HMAX),("max_plus_2018_flood_reference",HMAX+183)]:
    residual=1254.0-need
    print("stress",label,round(need,4),round(residual,4),round(residual/1254*100,4))

# Illustrative maturity structures based on Stage7 reference auction yields.
yields={1:1.4332,2:1.708,5:2.239,10:2.995}
dur={1:0.95,2:1.85,5:4.4,10:7.8}
structures={
 "短期重視型":{1:.4,2:.4,5:.15,10:.05},
 "前倒しラダー型":{1:.3,2:.3,5:.25,10:.15},
 "均等ラダー型":{1:.25,2:.25,5:.25,10:.25},
 "中長期重視型":{1:.1,2:.2,5:.3,10:.4},
}
for name, weights in structures.items():
    wam=sum(k*v for k,v in weights.items())
    y=sum(yields[k]*v for k,v in weights.items())
    d=sum(dur[k]*v for k,v in weights.items())
    print("maturity",name,round(wam,4),round(y,5),round(d,4),"+100bp",round(-d,4))

# 1y market reference spread.
print("1y_reference_spread_bp", round((1.4332-0.447)*100,2))
