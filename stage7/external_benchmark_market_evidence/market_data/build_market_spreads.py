"""Reproduce Stage 7 market-rate calculations from captured official observations.

This script does not scrape the web. Source observations are preserved in the
Stage 7 CSV files with official source IDs/URLs. All derived averages and basis-
point spreads are calculated here rather than by hand.
"""
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent

dep = pd.read_csv(BASE / "deposit_rates_by_maturity.csv")
dep["year"] = dep["period"].str[:4]
annual = dep.groupby("year", as_index=False)[
    ["time_deposit_10m_plus_1y_pct", "ordinary_deposit_pct"]
].mean()
annual.to_csv(BASE / "deposit_rate_annual_summary.csv", index=False)

jgb = pd.read_csv(BASE / "jgb_yields_by_maturity.csv")
dep_2026_08 = float(
    dep.loc[dep["period"].eq("2026-08"), "time_deposit_10m_plus_1y_pct"].iloc[0]
)

rows = []
for _, r in jgb.iterrows():
    tenor = int(r["tenor_years"])
    status = "matched_near_date" if tenor == 1 else "term_extension_not_maturity_matched"
    rows.append(
        {
            "as_of": r["observation_date"][:7],
            "deposit_tenor_years": 1,
            "bond_tenor_years": tenor,
            "deposit_pct": dep_2026_08,
            "bond_pct": float(r["yield_pct"]),
            "spread_bp": round((float(r["yield_pct"]) - dep_2026_08) * 100, 2),
            "comparison_status": status,
        }
    )

calc = pd.DataFrame(rows)
calc.to_csv(BASE / "term_extension_spreads_reproduced.csv", index=False)

print("Annual deposit-rate averages (%)")
print(annual.to_string(index=False))
print("\nReference spreads (bp)")
print(calc.to_string(index=False))
