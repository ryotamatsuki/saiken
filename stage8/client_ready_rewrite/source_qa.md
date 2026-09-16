# Stage 8 Source / Evidence QA

**Target:** `stage4/reports/ehime_fund_bond_management_consulting_report_R7_R8.md`  
**Review date:** 2026-09-16

## 1. Evidence hierarchy check

The rewritten report follows the intended hierarchy:

1. official national / prefectural primary sources
2. official statistics
3. official assembly / audit / plan materials
4. international institutions and professional guidance
5. academic evidence where useful
6. reliable media only where primary extraction is not directly available

**Result: PASS**

## 2. Headline Ehime facts

The following headline claims were traced to existing source dictionaries and processed inputs:

- R6 total funds 1,302.28 oku yen / cash-deposits 1,286.87 / securities 15.40 / 1.18%: `STAT-R6-MIC` / `STAT-R6-EHIME`.
- R3–R6 16-period fund-substitution amounts: `EHIME-FS-R3`–`EHIME-FS-R6` and `ehime_fund_substitution_period_totals.csv`.
- R3–R7 recurring borrowing/repayment months: Stage6 `finance_affairs_cashflow_findings.md`, traced to Ehime official Finance Affairs PDFs.
- 400 oku fiscal buffer target and stress references: `EHIME-POLICY-2023`.
- R8 32-fund general-account withdrawals 351.85764 oku yen: `EHIME-BUDGET-R8-EXPLANATION`.
- Stage6 top-15 coverage 95.717% and 1–5y reconstruction: `major_funds_cashflow_reconstruction.md` plus official underlying URLs.
- non-cash fund examples: `EHIME-SETTLEMENT-R6`, `EHIME-MIURA-FUND`.

**Result: PASS**

## 3. R7 / R8 temporal integrity

- R6 unified year-end figures are not described as R7 actual holdings.
- R7 peer annual averages are kept separate from year-end or forecast data.
- Tokyo R7 forecast-in-R8-plan and R8 assumed allocation are not presented as the same measure.
- Ehime R7 detailed settlement remains explicitly unavailable / pending as of the review date.

**Result: PASS**

## 4. Peer comparability

Stage7 peer evidence is used by management archetype rather than as a ranking target.

- Saitama: annual-average fund allocation / bucket management.
- Shizuoka: annual-average allocation / pooled operation / deposit competition.
- Niigata: public-funds reform and annual plan; not treated as fund-only allocation.
- Kumamoto: policy architecture; peer-specific 21y / 1,000 oku limits are not transferred.
- Kagawa: R6 unified allocation plus cash-management evidence; R6 0% is not treated as an R7 target.
- Tokyo: plan / actual distinctions retained.
- Hyogo: fund categories and maturity practices are used as a reference, with comparability limitation.

**Result: PASS**

## 5. Market-data integrity

The report distinguishes:

- BOJ 10m-yen-plus 1y time-deposit posted average rate.
- MOF primary-auction yields.
- a near-date 1y reference spread from a realizable municipal investment return.
- 2/5/10/20y term-extension references from true same-tenor comparisons.

The report does not describe the 2y+ differences as maturity-matched spreads.

**Result: PASS**

## 6. Best-practice integrity

GFOA, IMF, OECD and World Bank guidance is presented as external benchmark / design evidence, not Japanese law and not Ehime's current rules.

The report explicitly states that the current full text of the Ehime Public Funds Management Policy is not publicly confirmed and therefore does not invent:

- current eligible-asset list
- maximum maturity
- issuer limits
- rating requirements
- authority matrix
- exception-sale approval rules

**Result: PASS**

## 7. Secondary-source use

`NIKKEI-2026-09-13` is used only for the reported macro observation that local-government-sector JGB/FILP-bond holdings rose from 16.3bn yen to about 1.6tn yen. The report immediately states the stock/flow, sector-coverage and estimation limitations and pairs the claim with BOJ methodology (`BOJ-FFA-METHOD`). It is not used to infer Ehime's behavior.

**Result: PASS**

## 8. Source traceability

Source IDs referenced in the report resolve across:

- `stage3/sources/source_dictionary.csv`
- `stage4/sources/source_dictionary.csv`
- `stage4/sources/jgb_purchase_surge_source_dictionary.csv`
- `stage4/sources/fund_ordinance_budget_source_dictionary.csv`
- `stage6/public_source_expansion/`
- `stage7/external_benchmark_market_evidence/source_dictionary.csv`

The canonical report's final source section is intentionally a major-source list, not a duplicate of every repository dictionary.

**Result: PASS**

## 9. Copyright handling

No third-party report/PDF is newly mirrored in Stage8. The report uses official URLs, source IDs, extracted facts and derived analysis. Existing Stage6/7 copyright rules remain intact.

**Result: PASS**

## 10. Explicit unresolved public-data gaps

The report preserves the following gaps instead of filling them by inference:

1. R7 Ehime detailed settlement package / fund-level cash balances.
2. current full text of the Ehime Public Funds Management Policy and granular limits.
3. complete public same-tenor large-deposit series beyond one year.
4. future outflows that are intrinsically contingent rather than merely undisclosed.

These gaps affect final execution sizing and limit setting, but do not invalidate the ALM decision framework.

## Final evidence gate

**SOURCE / EVIDENCE QA: PASS**

**Gate A — Evidence integrity: PASS**
