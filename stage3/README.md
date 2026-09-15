# Stage 3 — R7全国都道府県 公金・基金債券運用実態

調査基準日：2026-09-15

Stage 3 は、R4～R6の総務省・e-Stat全国統一データと、47都道府県が公表するR7（FY2025）の公金管理・基金運用資料を接続し、現預金・債券配分、利回り、年限、ラダー、一括運用、ガバナンス、金利正常化後の方針変化を比較した最終調査レイヤーです。

## 最終レポート

- `reports/national_prefecture_public_fund_bond_investment_R7.md`
  - 「全国都道府県における基金・公金の債券運用実態 ― R7の現預金・債券配分、利回り、年限、運用手法、ガバナンスの比較 ―」

## 主要データ

- `processed/R7_national_comparison_table.csv` — 47都道府県R7最終比較表
- `processed/R7_fund_allocation_core.csv` — 基金・年間平均残高で直接比較可能な5県
- `processed/R7_supplementary_comparison.csv` — 年度末・公金全体・年度途中等の補助比較
- `processed/R7_strict_comparability_47.csv` — R7比較可能性A～E
- `processed/management_features.csv` — 一括運用・ラダー・リスク管理等
- `processed/maturity_comparison.csv` — 公表された年限情報
- `processed/policy_change_matrix.csv` — 金利正常化後の方針変化
- `processed/typology.csv` — 複数属性による運用類型
- `processed/summary_statistics.csv` — Python再計算値

## 図表

- `charts/fig1_R6_securities_ratio_47.svg`
- `charts/fig2_R7_cash_bond_ratio_5.svg`
- `charts/fig3_R7_ratio_vs_balance.svg`
- `charts/fig4_R7_deposit_bond_yields.svg`
- `charts/fig5_maturity_ladder.svg`
- `charts/fig6_policy_change.svg`

## 出典・監査

- `sources/source_dictionary.csv` — 本文Source IDと一次資料URL
- `qa/final_audit.md` — 最終数値・定義監査

## 比較上の最重要注意

総務省表31の「年度末有価証券」と、各県独自資料の「年間平均債券残高」は同じ指標ではありません。Stage 3ではこれらを別系列として扱い、R6→R7の変化は同一公表系列が確認できる場合だけ判定します。

また、基金、公金全体、歳計現金、年度末残高、平均残高、実績、見込、計画を混同せず、検索で確認できなかった値を0として補完していません。

最終判定：**FINAL DATA/REPORT QA PASS**
