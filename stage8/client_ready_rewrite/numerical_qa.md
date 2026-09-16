# Stage 8 Numerical QA

**Target:** `stage4/reports/ehime_fund_bond_management_consulting_report_R7_R8.md`  
**Method:** Python only. Manual arithmetic is not used for the checked headline claims.  
**Reproduction:** `qa_recompute.py`

## 1. Fund substitution distribution

Input: `stage4/processed/ehime_fund_substitution_period_totals.csv`, 16 periods from R3–R6.

| Metric | Recomputed (oku yen) | Report |
|---|---:|---:|
| min | 203.51000 | 203.51 |
| Q1 | 461.87250 | 461.87 |
| mean | 624.38813 | 624.39 |
| median | 659.18000 | 659.18 |
| P75 | 765.91250 | 765.91 |
| P90 | 841.25500 | 841.26 |
| P95 | 874.09500 | 874.10 |
| max | 968.01000 | 968.01 |

Seasonal means by period position:

- Apr–May: 775.71750 oku yen -> report 775.72
- summer: 325.30750 -> 325.31
- autumn: 614.23750 -> 614.24
- year-end: 782.29000 -> 782.29

**Result: PASS**

## 2. Scenario envelope

Input total funds: 1,302.27675 oku yen.

| Case | Recomputed bonds | Bond ratio | <=1y liquidity | Coverage of 968.01 peak |
|---|---:|---:|---:|---:|
| Conservative | 151.26675 | 11.615561% | 1,151.01000 | 118.904763% |
| Standard | 435.31550 | 33.427265% | 968.01000 | 100.000000% |
| Active | 574.70300 | 44.130635% | 932.75500 | 96.357992% |

Report rounding: 151.27 / 435.32 / 574.70 oku yen; 11.6% / 33.4% / 44.1%; 118.9% / 100.0% / 96.4%.

**Result: PASS**

## 3. Standard ladder

Input: `stage4/processed/ehime_model_ladder_standard_case.csv`.

1y 101.04875 + 2y 66.85335 + 3y 66.85335 + 4y 58.49668125 + 5y 58.49668125 + 6–10y 16.7133375 each = **435.31550 oku yen**.

**Result: PASS**

## 4. Materiality of Stage 6 major-fund review

Top 15 R8 withdrawals: 336.78819 oku yen.  
All 32 general-account fund withdrawals: 351.85764 oku yen.

Coverage = **95.717174%**, report 95.717%.

**Result: PASS**

## 5. R7 direct-five comparison

Bond ratios used: Fukushima 25.083034%, Saitama 65.002573%, Chiba 60.097265%, Shizuoka 61.652518%, Tottori 15.231788%.

Simple mean = **45.413436%**, report 45.4%.

This remains explicitly labelled a disclosure-selected reference sample, not a national average.

**Result: PASS**

## 6. Market reference spread

BOJ Aug-2026 10m-yen-plus 1y time-deposit average: 0.447%.  
MOF 2026-08-19 approx-1y T-Bill average accepted yield: 1.4332%.

Difference = `(1.4332 - 0.447) * 100` = **98.62 bp**.

The report correctly states that this is a near-date market reference and not a realizable municipal return estimate.

**Result: PASS**

## 7. Income sensitivity

Using `Incremental income = bond amount × spread`:

| Case | +0.1pt | +0.2pt | +0.3pt | +0.5pt |
|---|---:|---:|---:|---:|
| Conservative 151.26675 oku | 15.126675m yen | 30.253350m | 45.380025m | 75.633375m |
| Standard 435.31550 oku | 43.531550m | 87.063100m | 130.594650m | 217.657750m |
| Active 574.70300 oku | 57.470300m | 114.940600m | 172.410900m | 287.351500m |

Displayed values are rounded to one decimal million yen in the canonical report.

**Result: PASS**

## Final numerical gate

**NUMERICAL QA: PASS**

No headline calculation checked in this review requires correction. The model amounts remain scenario values rather than actual Ehime holdings or optimal allocations.
