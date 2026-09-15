# saiken — 都道府県基金・債券運用分析

日経新聞「自治体の国債購入 急増」の問題意識を踏まえ、総務省・e-Statの全国統一統計だけで47都道府県の基金運用を比較するデータセットです。

## 第1段階

対象：令和4～6年度決算（FY2022～FY2024）

一次資料：総務省「地方財政状況調査（都道府県分）」表01、02、31。

主成果物：

- `processed/prefecture_fund_investment_R4_R6.csv` — long形式（47都道府県×3年度）
- `processed/wide_data.csv` — wide形式（47都道府県）
- `processed/R6_rankings.csv` — 主要6ランキング
- `processed/ehime_analysis.csv` — 愛媛県の全国ポジション
- `processed/source_dictionary.csv` — 変数別の一次資料・列名・URL
- `processed/QA.csv` — データ品質監査
- `processed/stage2_candidates.csv` — 第2段階候補県
- `prefecture_fund_investment_analysis.md` — 日本語分析レポート
- `charts/` — 図表
- `raw/` — e-Statから取得した原CSV

注意：第1段階で比較するのは「基金に占める有価証券運用」であり、「国債購入額ランキング」ではありません。

現在の判定：**DATASET COMPLETE**
