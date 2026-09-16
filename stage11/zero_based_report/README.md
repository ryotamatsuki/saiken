# Stage 11 — Zero-Based Public Funds Strategy Review

## Purpose

愛媛県の基金・公金管理について、旧canonical report、旧Executive Summary、旧Conclusion、旧推奨額・旧ラダーを分析入力にせず、GitHub内の構造化データ・出典台帳・公開事実抽出・市場データからゼロベースで再構築した独立分析である。

## Main deliverable

- `ehime_public_funds_strategy_report.md` — 最終レポート

## Analytical working papers

- `management_questions.md`
- `hypothesis_tree.md`
- `independent_fact_base.md`
- `independent_findings.md`
- `scenario_analysis.md`
- `peer_model_analysis.md`
- `portfolio_analysis.md`
- `risk_analysis.md`
- `strategic_options.md`
- `report_storyline.md`

## Reproducible calculations

Run from repository root:

```bash
python stage11/zero_based_report/recompute/zero_base_recompute.py
```

The script uses only permitted factual/structured inputs and regenerates Stage 11 statistical, concentration, maturity-stress and income-sensitivity outputs.

## QA

- `numerical_qa.md` — PASS
- `source_qa.md` — PASS with disclosed limitations
- `independence_qa.md` — PASS under the operational information firewall
- `final_review.md` — Senior Manager gate

## Information firewall

See `information_firewall.md`. Stage 4 prior report contents and Stage 8–10 rewrite/QA materials are prohibited analytical inputs. Mixed files are used only for factual fields explicitly permitted in `data_room_inventory.csv`.

## Final designation

**ZERO-BASED CONSULTING REPORT — DATA CONSTRAINED**

The analysis identifies material strategic and management implications, but public data are insufficient to set a defensible single investable amount, target securities ratio, longest maturity, or product allocation. The principal missing inputs are weekly cash-flow forecasts, major-fund multi-year payment schedules, the integrated debt-service calendar, current full policy text, and live same-tenor execution rates.
