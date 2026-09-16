# Market Data Methodology

## 1. 目的

canonical report Ch.12で、異なる資金拘束期間を持つ商品を無条件に比較しないための市場データ基盤を作る。

## 2. 預金系列

日本銀行「預金種類別店頭表示金利の平均年利率等（月次）」のうち、主要時系列に掲載される `預入金額1千万円以上・1年定期` と普通預金を使用する。期間は2023-01～2026-08。

この系列は金融機関の店頭表示平均であり、地方公共団体が引合い・入札により得る実際の預金金利ではない。したがってmarket referenceとして利用し、愛媛県の実運用金利と推定しない。

BOJ主要時系列の一覧では、同じカテゴリで2年・3年・5年の大口定期系列を確認できなかった。このため年限の異なる預金金利を補間・推定しない。

## 3. 国債系列

財務省の国債入札結果から、直近の1年T-Bill、2年、5年、10年、20年の募入平均利回りを取得した。これらはprimary auction yieldであり、日々の流通市場constant-maturity yieldとは定義が異なる。

財務省は主要年限金利の公式CSV (`jgbcm.csv`, `jgbcm_all.csv`) を公開しているが、本実行環境では `text/csv` content-typeをweb readerが処理できず、containerからも外部DNS接続できなかった。このためCSV時系列自体は未取込とし、URLをsource dictionaryに登録した。これはpublic-data absenceではなくexecution-environment ingestion gapである。

## 4. Maturity matching rule

- 1年定期 vs 約1年T-Bill：`matched_near_date` とする。月次預金金利と8月19日auctionのため完全同日ではない。
- 1年定期 vs 2/5/10/20年国債：`term_extension_not_maturity_matched` とする。
- 2年預金 vs 2年国債、5年預金 vs 5年国債：預金側公式標準系列を確認できないため `not_directly_comparable` とする。
- interpolation、proxy、任意の銀行の商品金利による穴埋めは行わない。

## 5. 計算

すべてPythonで計算する。

`spread_bp = (bond_yield_pct - deposit_yield_pct) * 100`

百分率の差1.00ポイント = 100bp。

## 6. Ch.12での使用上の注意

2026年8月の1年定期0.447%と1年T-Bill平均利回り1.4332%の差98.62bpは、比較的近い期間のmarket referenceである。しかし、地方公共団体が実際に購入可能な価格・預金入札金利・手数料・settlement timingまで同一ではないため、実現可能な追加収益を98.62bpと断定しない。

2年以上の国債との差はterm premiumだけでなくyield curve、発行条件、観測日の差を含む。Ch.12では期間延長の機会費用・流動性リスクを説明する参考値としてのみ使う。
