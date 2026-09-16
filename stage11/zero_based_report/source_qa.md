# Source QA

Status: **PASS with disclosed limitations**

## Source hierarchy

Stage 11 prioritizes Ehime official/public-data extracts and national public statistics, followed by other local-government primary-source extracts. Market inputs are BOJ/MOF-derived structured data already stored in the repository. No external web research was added to construct new conclusions.

## Mixed files

Where a permitted structured file contains factual and interpretive columns, only factual fields are inputs:

- `ehime_fiscal_management_policy_constraints.csv`: metric, value, unit, period, source and status facts only; prior `alm_treatment` is excluded.
- `ehime_fund_ordinance_liquidity_register.csv`: public purpose/rule, floor/horizon, public amount, R8 withdrawal and source IDs only; prior interpretation/recommended maturity fields are excluded.
- `peer_case_comparison.csv`: peer portfolio and management facts only; `ehime_transferability` is excluded.
- `finance_affairs_cashflow_findings.md`: only the verified R3-R7 borrowing/repayment timing facts are used; prior chapter interpretation is excluded.

## Definition controls

- R6 nationwide panel: year-end unified data.
- R7 directly comparable peer allocations: annual-average actuals; not mixed with year-end data.
- R8 fund withdrawals: budget amounts, not actuals.
- BOJ one-year deposit rate: published average series, not an Ehime negotiated rate.
- MOF JGB/T-bill observations: reference auction yields on different dates; 2-20 year values are not described as same-tenor spreads against one-year deposits.

## Material evidence gaps

The permitted public data room does not provide a complete current public-funds policy text, daily/weekly cash flows, a complete 3-5 year fund-expenditure calendar, or same-date live execution rates. These gaps affect the ability to set a single investable amount and longest maturity, and are therefore carried into the final DATA CONSTRAINED judgement rather than filled by assumption.

## Result

**SOURCE QA PASS**
