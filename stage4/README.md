# Stage 4 — 愛媛県基金の債券運用余地・ALM分析

調査基準日：2026-09-15

Stage 4 は、Stage 3の全国比較をベンチマークとして、愛媛県のR3～R6基金繰替運用、R2～R6基金残高、基金別取崩構造、財源対策用基金、災害ストレスを統合し、必要流動性と債券運用可能レンジを推計する。

## 最終レポート

- `reports/ehime_fund_bond_capacity_ALM_R7.md`
  - 「愛媛県基金の債券運用余地 ―必要流動性、基金繰替運用、ALM及び全国比較からみた適正ポートフォリオ―」

## 主要成果物

- `processed/ehime_fund_substitution_R3_R6_long.csv` — R3～R6基金別・期間別繰替64行
- `processed/ehime_fund_substitution_period_totals.csv` — 16期間合計
- `processed/ehime_fund_substitution_stats.csv` — 年度別最大・最小・平均・中央値・期間加重平均
- `processed/ehime_fund_substitution_seasonal_stats.csv` — 4～5月・夏期・秋期・年度末の季節統計
- `processed/ehime_fund_balance_R2_R6.csv` — 基金総額・主要基金残高
- `processed/ehime_major_fund_5yr_long.csv` — 主要基金5年推移・確認できた積立取崩
- `processed/ehime_other_specific_fund_flows_R2_R6.csv` — その他特定目的基金の積立取崩
- `processed/ehime_fund_classification.csv` — 基金のALM類型
- `processed/ehime_liquidity_distribution.csv` — 16期間の分布統計
- `processed/ehime_liquidity_bond_scenarios.csv` — 保守・標準・積極3ケース
- `processed/ehime_income_sensitivity.csv` — 一般的な増収感応度
- `processed/ehime_scenario_income_sensitivity.csv` — 3ケース別増収感応度
- `processed/ehime_national_benchmark.csv` — R7直接比較県との外部妥当性チェック
- `processed/evidence_table.csv` — 学術・国際実務エビデンス
- `charts/fig1`～`fig9` — 指定9図
- `sources/source_dictionary.csv` — Source ID・一次資料
- `qa/final_audit.md` — 最終監査

## 中心結果

R6基金総額1,302.28億円を基準に、公表情報だけで構築した政策レンジは次のとおり。

- 保守：債券151.27億円、11.6％
- 標準：債券435.32億円、33.4％
- 積極：債券574.70億円、44.1％

標準ケースは、過去最大基金繰替968.01億円を、即時現金・near-cash・1年以内満期債で100％カバーする。これは統計的な最適比率ではなく、ALMの政策設計レンジである。

R3～R6の基金繰替は16期間で203.51～968.01億円。季節平均は4～5月775.72億円、夏期325.31億円、秋期614.24億円、年度末782.29億円であり、ピーク額を365日すべて即時現金で持つ必要性は確認できない。一方、基金が年度内資金繰りに大きく使われているため、全国の高債券比率県をそのまま模倣することもできない。

2026-09-15時点でR7基金全体の実際債券残高は公表資料から確定できないため、R6値で代替していない。R7財源対策用基金残高436億円見込みは補助事実としてのみ扱う。

最終判定：**FINAL EHIME ALM REPORT QA PASS**
