# Numerical QA

Status: **PASS**

All new arithmetic used in Stage 11 was performed in Python. No hand-calculated result is used as a final numerical output.

## Reconciliation tests

- R8 withdrawal detail rows sum to **351.85764億円**, equal to the source TOTAL: PASS.
- Fund-level R3-R6 substitution rows aggregate to all 16 period totals; only floating-point rounding remains: PASS.
- R6 fund total from the Ehime balance series (**1,302.28億円**) agrees with the nationwide panel (**1,302.27675億円**) within source rounding: PASS.
- R6 securities ratio **1.1827854563%** agrees with `processed/ehime_analysis.csv`: PASS.
- 2026-08 one-year deposit rate **0.447%** and the near-date one-year MOF reference **1.4332%** imply **98.62bp**; the recompute code derives this value from inputs rather than hard-coding it: PASS.

## Distribution checks

The substitution distribution uses 16 observations: mean **624.388125億円**, median **659.18億円**, P75 **765.9125億円**, P90 **841.255億円**, P95 **874.095億円**, maximum **968.01億円**.

The four period means are **775.7175**, **325.3075**, **614.2375**, and **782.29億円**. The second period has the highest coefficient of variation among the four periods.

## Stress checks

Four Stage 11 comparison structures are now recomputed: `短期中心`, `中短期中心`, `均等分散`, and `中長期比重`. Modified-duration price approximations are generated for +25bp, +50bp, +100bp, and -50bp. These structures are explicitly illustrative; they are not optimized or recommended allocations.

## Prohibited numerical practices

- Prior-report recommended amount imported: **NO**.
- Prior maturity ladder imported: **NO**.
- Budget amount treated as actual expenditure: **NO**.
- Year-end balance treated as annual average: **NO**.
- Different-tenor rates labelled a same-tenor spread: **NO**.
- Mark-to-market decline labelled realized loss without sale: **NO**.
- A statistical residual labelled an investable amount: **NO**.

## Result

**NUMERICAL QA PASS**
