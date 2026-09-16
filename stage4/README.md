# Stage 4 — 愛媛県基金の債券運用・ALM分析

調査基準日：2026-09-16

Stage 4 は、全国都道府県のR7以降の公金・基金運用、自治体の国債・財投債保有急増の背景、愛媛県のR3～R6基金繰替、R2～R6基金残高、財政運営基本方針、R8予算、基金条例・決算を統合し、必要流動性と債券運用可能レンジ、モデル満期ラダーを分析する。

## Canonical consulting report

- `reports/ehime_fund_bond_management_consulting_report_R7_R8.md`
  - **「愛媛県における基金の債券運用高度化に向けた調査分析 ― 全国のR7以降の運用動向、必要流動性及び基金別ALMからみた運用余地 ―」**
  - 愛媛県の基金担当者向けに、全国動向、国債保有急増の背景、現預金・債券配分、類似団体、基金用途、必要流動性、債券運用余地、モデル・ポートフォリオ、リスク、ガバナンス、ロードマップを1冊に統合。
  - 最終QA：`qa/final_consulting_report_audit.md`
  - 判定：**FINAL CONSULTING REPORT PASS**

## 固定構成

- `reports/FINAL_REPORT_STRUCTURE_FREEZE_20260916.md`
  - Executive Summary＋第1～15章＋結論＋付録＋出典・参考資料。
  - 事実と考察を分離。
  - 全国レポート等の内部成果物は調査基盤として再利用するが、最終読者に別資料参照を要求しない。
  - 愛媛県の非公表R7実運用は推定しない。
  - 第11章は実運用の再現ではなく、公開情報から導くモデル・ポートフォリオと満期ラダー。

## 主要な調査モジュール

- `reports/ehime_fund_bond_capacity_ALM_R7.md` — 初期ALM分析。
- `reports/fiscal_management_policy_integration_note.md` — 財政運営基本方針のALM制約化。
- `reports/fund_ordinance_budget_research_note.md` — 条例・予算・決算による基金別bottom-up調査。
- `research/jgb_purchase_surge_background_20260916.md` — 地方公共団体の国債・財投債保有急増の背景調査。

## 主要データ

- `processed/ehime_fund_substitution_R3_R6_long.csv` — R3～R6基金別・期間別繰替64行。
- `processed/ehime_fund_substitution_period_totals.csv` — 16期間合計。
- `processed/ehime_fund_substitution_seasonal_stats.csv` — 4～5月・夏期・秋期・年度末の季節統計。
- `processed/ehime_liquidity_distribution.csv` — 中央値、P75、P90、最大等。
- `processed/ehime_liquidity_bond_scenarios.csv` — 保守・標準・積極3ケース。
- `processed/ehime_scenario_income_sensitivity.csv` — 預金対比スプレッド別増収感応度。
- `processed/ehime_fiscal_management_policy_constraints.csv` — 財政運営基本方針の制約。
- `processed/ehime_R8_fund_withdrawals.csv` — R8一般会計32基金、計351.85764億円の取崩予算。
- `processed/ehime_fund_ordinance_liquidity_register.csv` — 主要基金の用途・保持制約・推奨満期bucket。
- `processed/ehime_fund_statutory_sunset_rules.csv` — 法定最低額・政策フロア・終期・国庫返還・非現金元本等。
- `processed/ehime_peer_comparison_R7_R8.csv` — 公式CグループとALM類似団体の比較。
- `processed/ehime_model_ladder_standard_case.csv` — 標準ケース435.3155億円の例示満期ラダー。

## 図表

- `charts/fig1`～`fig9` — 基金残高、基金繰替、3シナリオ、収益感応度等。
- `charts/fig10_R7_direct_cash_bond_allocation.svg` — R7直接比較5県の現預金・債券構成。
- `charts/fig11_standard_case_maturity_ladder.svg` — 標準ケースのモデル満期ラダー。

## 出典

- `sources/source_dictionary.csv` — 愛媛県ALM・基金条例等の主要Source ID。
- `sources/jgb_purchase_surge_source_dictionary.csv` — 国債保有急増背景のSource ID。
- `sources/consulting_report_source_supplement_20260916.csv` — 類似団体等の追加一次資料。

最終レポート末尾にも、国・公的機関、愛媛県、他都道府県・自治体、国際機関・学術文献、報道・補助資料の5区分で出典・参考資料を収録している。

## 現時点の中心結果

R6基金総額1,302.28億円を共通分母とするtop-downの政策レンジは次のとおり。

- 保守：151.27億円、11.6％
- 標準：435.32億円、33.4％
- 積極：574.70億円、44.1％

これは「最適額」ではなくscenario envelopeである。標準ケースは過去最大基金繰替968.01億円を、即時現金・near-cash・1年以内満期債で100％カバーする。

R7末又はR8期首の基金別現金残高は、R7決算関係が令和8年9月議会で審議中のため現時点では取得対象外としている。このため基金別bottom-upの合計による最終的な債券運用可能額は、R7決算公表後の更新事項である。

## QA

- `qa/final_audit.md` — 初期Stage4監査。
- `qa/fiscal_policy_integration_audit.md` — 財政運営基本方針統合監査。
- `qa/fund_ordinance_budget_research_audit.md` — 条例・予算・基金別制約監査。
- `qa/jgb_purchase_surge_background_audit.md` — 国債保有急増背景調査監査。
- `qa/final_consulting_report_audit.md` — canonical consulting report最終監査。

最終判定：**FINAL CONSULTING REPORT PASS**
