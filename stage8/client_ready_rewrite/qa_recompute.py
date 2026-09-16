"""Recompute key numerical claims in the Stage 8 canonical report.

All values below are taken from already validated public-source-derived inputs
stored in stage3-stage7. This script is intended as a compact QA gate, not a
new data-collection pipeline.
"""
import numpy as np

fund_substitution = np.array([
    815.99, 451.53, 465.32, 631.54,
    736.67, 203.51, 619.29, 686.82,
    710.49, 247.87, 623.12, 968.01,
    839.72, 398.32, 749.22, 842.79,
])

print("Fund substitution distribution (oku yen)")
for name, value in [
    ("min", fund_substitution.min()),
    ("q1", np.quantile(fund_substitution, 0.25)),
    ("mean", fund_substitution.mean()),
    ("median", np.median(fund_substitution)),
    ("p75", np.quantile(fund_substitution, 0.75)),
    ("p90", np.quantile(fund_substitution, 0.90)),
    ("p95", np.quantile(fund_substitution, 0.95)),
    ("max", fund_substitution.max()),
]:
    print(name, round(float(value), 5))

print("seasonal means", fund_substitution.reshape(4, 4).mean(axis=0))

total_funds = 1302.27675
max_substitution = 968.01
scenarios = {
    "conservative": dict(cash=968.01, near=183.0, le1=0.0,
                         y1_3=90.76005, y3_5=45.380025, y5p=15.126675),
    "standard": dict(cash=765.9125, near=101.04875, le1=101.04875,
                     y1_3=133.7067, y3_5=116.9933625, y5p=83.5666875),
    "active": dict(cash=659.18, near=68.39375, le1=205.18125,
                   y1_3=110.856525, y3_5=129.3326125, y5p=129.3326125),
}

print("\nScenario checks")
for name, s in scenarios.items():
    bonds = s["le1"] + s["y1_3"] + s["y3_5"] + s["y5p"]
    liquid = s["cash"] + s["near"] + s["le1"]
    print(name, {
        "bonds_oku": round(bonds, 6),
        "bond_ratio_pct": round(bonds / total_funds * 100, 6),
        "le1_liquidity_oku": round(liquid, 6),
        "max_coverage_pct": round(liquid / max_substitution * 100, 6),
    })

ladder = [
    101.04875, 66.85335, 66.85335, 58.49668125, 58.49668125,
    16.7133375, 16.7133375, 16.7133375, 16.7133375, 16.7133375,
]
print("\nstandard ladder total", round(sum(ladder), 6))

peer_bond_ratios = np.array([25.083034, 65.002573, 60.097265, 61.652518, 15.231788])
print("R7 direct-five simple mean", round(peer_bond_ratios.mean(), 6))

major15 = 336.78819
all32 = 351.85764
print("major15 withdrawal coverage", round(major15 / all32 * 100, 6))

one_year_deposit = 0.447
one_year_tbill = 1.4332
print("one-year near-date market reference spread bp", round((one_year_tbill - one_year_deposit) * 100, 2))

for amount in [151.26675, 435.3155, 574.703]:
    print("income sensitivity", amount, {
        f"{spread:.1f}pt": round(amount * spread, 5)
        for spread in [0.1, 0.2, 0.3, 0.5]
    }, "million yen")
