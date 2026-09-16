# Stage 8 — Client-Ready Canonical Report Rewrite

## Purpose

Rewrite the canonical Ehime fund / bond-management report against the fixed Stage5 quality framework, using Stage6 Ehime public-source evidence and Stage7 external benchmark / market / best-practice evidence.

## Canonical report

`stage4/reports/ehime_fund_bond_management_consulting_report_R7_R8.md`

## Rewrite order executed

1. Ch.9 Required liquidity
2. Ch.10 Investable amount
3. Ch.11 Target portfolio architecture
4. Ch.13 Risk
5. Ch.14 Governance
6. Ch.15 Implementation roadmap
7. Ch.4–7 peer integration
8. Ch.12 value case
9. Ch.8 fund typology
10. Ch.1–3 context
11. Conclusion
12. Executive Summary last

## Stage8 files

- `rewrite_change_log.md`
- `chapter_quality_review.md`
- `qa_recompute.py`
- `numerical_qa.md`
- `source_qa.md`
- `client_ready_final_review.md`

## Core decision framework

`cash need → liquidity architecture → investable surplus → maturity matching → value / risk → governance → staged implementation`

The report does not recommend copying another prefecture's bond ratio or maturity limit.

## Key numerical position

The existing top-down scenarios are retained:

- Conservative: 151.27 oku yen
- Standard: 435.32 oku yen
- Active: 574.70 oku yen

The Standard case remains a policy envelope / center case, not an immediately executable purchase amount. It covers the historical maximum fund substitution (968.01 oku yen) with <=1y liquidity assets while allocating the residual across maturity buckets.

## QA status

- Numerical QA: PASS
- Source / Evidence QA: PASS
- Chapter quality review: PASS
- Evidence integrity: PASS
- Decision logic: PASS
- Implementation readiness: PASS
- Communication: PASS
- Final Stage5-framework score: **93/100**

## Final judgement

**CLIENT-READY PASS — HIGH CONFIDENCE**

## Remaining update triggers

1. Publication of R7 Ehime detailed settlement / fund-level cash balances.
2. Publication or confirmation of the current full Ehime Public Funds Management Policy and granular limits.
3. Better same-tenor deposit data for >1y horizons.
4. R9 budget information that changes major-fund 1–5y pipelines.

These should update the execution sizing and policy limits, but do not require redesigning the report's ALM framework.
