# Stage 2 — R7/R8 47都道府県 公金・基金運用（公表資料ベース）

## Status

**STAGE 2 COMPLETE**

47都道府県についてR7（FY2025）・R8（FY2026）の公式公表資料を横断確認し、Stage 1（R4～R6全国統一統計）と接続した。愛媛県を含む全団体について公表資料のみを使用し、内部資料・非公表情報は使用していない。

## データの考え方

- R4～R6: 総務省・e-Statの全国統一統計（`national_standardized`）。
- R7～R8: 各都道府県の個別公表資料。実績・計画・方針を `period_type` と `source_framework` で分離。
- `SEARCHED_NOT_FOUND` は「存在しない」を意味しない。
- 「有価証券」「債券」「国債」は同義扱いしない。
- 公表資料で比較できない情報は `public_data_gaps.csv` に明示した。

## 主な成果物

- `processed/prefecture_R7_R8_public_fund_investment_long.csv`: 47×2年度の調査本体（94行）。
- `processed/prefecture_R7_R8_disclosure_matrix.csv`: 47県の開示スコア・比較可能性。
- `processed/prefecture_R4_R8_integrated.csv`: R4～R8統合（235行）。
- `processed/public_data_gaps.csv`: 47×2年度×10項目の公開情報ギャップ（940行）。
- `processed/comparison_candidates.csv`: Stage 1の6変数から機械抽出した愛媛県類似10県。
- `processed/advanced_management_prefectures.csv`: 公表資料で確認できる運用実務要素による先進候補12県。
- `processed/QA.csv`: 完全性・整合性・内部データ不使用等のQA。
- `sources/source_dictionary.csv`: 数値・方針ごとの一次資料辞書。
- `sources/search_log.csv`: 47県×R7/R8の検索記録。
- `reports/prefecture_R7_R8_public_fund_investment_analysis.md`: 分析レポート。

## 比較可能性

A=2県、B=6県、C=2県、D=32県、E=5県。A/B/Cの詳細は disclosure matrix を参照。

愛媛県はR7/R8の基金全体の国債残高・利回り・年限等を同じ粒度で示す公表資料を今回確認できず、比較可能性Eとした。この判定は「国債運用をしていない」という意味ではなく、公表資料ベースでの比較可能性を示す。

## 再現性・留意点

類似県は、R6の標準財政規模、基金総額、基金/標準財政規模、歳出総額、有価証券比率、現預金比率をZ標準化し、愛媛県からのユークリッド距離で算出。運用先進候補は、公表資料で確認できる債券残高・国債残高・利回り・収入・年限・ラダー・一括運用・委員会・リスク方針・直近強化の10要素を機械集計した。

R7/R8は各県の公表形式が統一されていないため、単純な全国順位は作らない。詳細はレポートの「データ上の限界」を参照。
