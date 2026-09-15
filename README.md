# saiken — 都道府県基金・公金の債券運用分析

都道府県が基金・歳計現金その他の公金を、現預金と債券へどのように配分し、どの年限・商品・管理方法で運用しているかを、公表情報だけで比較・分析する調査リポジトリです。

内部資料・非公表資料・庁内限定情報は使用していません。

## Stage 1 — R4～R6 全国統一統計

対象：令和4～6年度決算（FY2022～FY2024）

一次資料：総務省・e-Stat「地方財政状況調査（都道府県分）」表01、02、31。

主成果物：

- `processed/prefecture_fund_investment_R4_R6.csv` — long形式（47都道府県×3年度）
- `processed/wide_data.csv` — wide形式（47都道府県）
- `processed/R6_rankings.csv` — R6主要指標
- `processed/source_dictionary.csv` — 一次資料・変数定義
- `processed/QA.csv` — データ品質監査
- `prefecture_fund_investment_analysis.md` — Stage 1分析レポート

注意：Stage 1で比較するのは年度末の「基金に占める有価証券」であり、国債購入額や年間平均債券残高ではありません。

## Stage 2 — R7・R8 公表資料探索

47都道府県の公式サイト、決算・監査資料、公金管理資料、議会会議録等を検索し、R7・R8の公表状況、定量値、運用方針を構造化しました。

- `stage2/processed/prefecture_R7_R8_public_fund_investment_long.csv`
- `stage2/processed/prefecture_R7_R8_disclosure_matrix.csv`
- `stage2/reports/prefecture_R7_R8_public_fund_investment_analysis.md`

## Stage 3 — R7 全国比較・最終レポート

Stage 2を再監査し、平均残高／年度末、基金／公金全体、実績／見込／計画を分離したうえで最終比較を作成しました。

### 最終レポート

**`stage3/reports/national_prefecture_public_fund_bond_investment_R7.md`**

> 全国都道府県における基金・公金の債券運用実態  
> ― R7の現預金・債券配分、利回り、年限、運用手法、ガバナンスの比較 ―

### 主要成果物

- `stage3/processed/R7_national_comparison_table.csv` — 47都道府県R7比較表
- `stage3/processed/R7_fund_allocation_core.csv` — 直接比較可能な5県
- `stage3/processed/R7_strict_comparability_47.csv` — A～E比較可能性
- `stage3/processed/management_features.csv` — 一括運用・ラダー・リスク管理
- `stage3/processed/maturity_comparison.csv` — 年限比較
- `stage3/processed/policy_change_matrix.csv` — 金利正常化後の方針変化
- `stage3/processed/typology.csv` — 運用類型
- `stage3/charts/` — 図1～図6
- `stage3/sources/source_dictionary.csv` — Source ID・一次資料
- `stage3/qa/final_audit.md` — 最終監査

Stage 3 最終判定：**FINAL DATA/REPORT QA PASS**

## Stage 4 — 愛媛県基金の債券運用余地・ALM分析

全国比較を目標値として使わず、愛媛県自身の基金繰替、基金残高、取崩し、財源対策用基金、災害ストレスから必要流動性を推計し、その残余を債券運用可能なコア資金として評価しました。

### 最終レポート

**`stage4/reports/ehime_fund_bond_capacity_ALM_R7.md`**

> 愛媛県基金の債券運用余地  
> ― 必要流動性、基金繰替運用、ALM及び全国比較からみた適正ポートフォリオ ―

### 中心結果

R6基金総額1,302.28億円に対する公表情報ベースの政策レンジ：

- 保守ケース：債券151.27億円（11.6％）
- 標準ケース：債券435.32億円（33.4％）
- 積極ケース：債券574.70億円（44.1％）

標準ケースは、過去最大の基金繰替968.01億円を、即時現金・near-cash・1年以内満期債で100％カバーしたうえで残余資金を満期分散するALM設計です。比率そのものを最適値とは扱いません。

- `stage4/processed/` — R2～R6基金、R3～R6繰替、季節統計、3ケース、収益感応度、全国ベンチマーク等
- `stage4/charts/` — 図1～図9
- `stage4/sources/source_dictionary.csv` — 愛媛県一次資料・国際実務・学術文献
- `stage4/qa/final_audit.md` — 最終監査

2026年9月15日時点ではR7基金全体の実際債券残高を公表資料から確定できないため、R6数値で代替していません。

Stage 4 最終判定：**FINAL EHIME ALM REPORT QA PASS**
