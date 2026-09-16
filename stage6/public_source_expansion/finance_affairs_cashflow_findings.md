# 愛媛県「財政事情」時系列 — 資金繰り・基金繰替に使える情報

## 1. Coverage

県公式「財政事情の公表」ページでは、平成14年5月から令和8年5月まで、原則5月・11月の資料を追跡できる。本Stageでは公式ページ上のリンクを49件カタログ化した。

Official index: https://www.pref.ehime.jp/page/8806.html

Open-data catalog: https://www.pref.ehime.jp/opendata-catalog/dataset/1400.html

個別PDFは `finance_affairs_catalog_H14_R8.csv` を参照。

## 2. Why this source matters

既存Stage 4ではR3～R6財務書類から基金繰替額を16期間に構造化し、peak / P75 / P90 / seasonal averageを計算した。「財政事情」はこれを補完し、基金繰替の借入・返済が年度内のどの時期に発生したかを説明できる。

したがって第9章では、金額分布だけでなく次の二次元で必要流動性を説明できる。

- size: いくら必要になったか
- time: いつ借り、いつまでに返したか

## 3. Verified annual cash-flow pattern

令和3年度から令和7年度について、各翌年度5月公表の「財政事情」の一時借入金欄を確認すると、基金からの繰替運用による借入れは共通して次の時間構造を持つ。

1. 4月及び5月に基金から借入れ
2. それらを8月までに償還
3. その後8月及び11月に再度借入れ
4. それらを3月までに償還
5. 銀行等からの「一時借入金」は当該年度にはなし

### R3

Source: https://www.pref.ehime.jp/uploaded/attachment/48805.pdf

同資料は「令和3年度は4月及び5月に借入れを行い、いずれも8月までに償還」「その後、8月及び11月に借入れを行い、いずれも3月までに償還」と記載する。

### R4

Source: https://www.pref.ehime.jp/uploaded/attachment/48803.pdf

R4についても4・5月借入→8月まで返済、8・11月借入→3月まで返済という年度内循環を確認。

### R5

Source: https://www.pref.ehime.jp/uploaded/attachment/117751.pdf

同様の借入・返済パターンを確認。

### R6

Source: https://www.pref.ehime.jp/uploaded/attachment/148420.pdf

同様の借入・返済パターンを確認。

### R7

Source: https://www.pref.ehime.jp/uploaded/attachment/181293.pdf

R7も4・5月借入→8月まで返済、8・11月借入→3月まで返済。したがって、Stage 4でR3～R6から確認していた季節性がR7でも継続したことを公開資料から確認できる。

## 4. Interpretation for Ch.9

この反復パターンは、愛媛県の基金が「年度末まで使われない長期貯蓄」だけではなく、歳計現金の季節的不足を埋めるTreasury liquidity poolとして機能していることを強く示す。

一方、4・5月の借入分が8月までに返済され、その後に改めて8月・11月に借りる構造であることは、peak額を年間365日すべて即時現金で保持する必要があることを意味しない。Client-ready版では、支払時期に合わせた次のbucket設計の根拠として用いる。

- immediate cash: 直近数週の歳計現金不足とforecast error
- near cash: 数週間～数か月の確度の高い需要
- <=1y maturity: 4～5月、8月、11月、年度末等の需要日に合わせた満期
- >1y assets: 上記年度内需要と基金固有支出を控除した残余のみ

## 5. Limits

「財政事情」の文章記述は借入・返済の月を示すが、全号で日次又は月次残高を同じ粒度で公表しているわけではない。したがって13週cash forecastそのものを過去資料から完全復元できるとは扱わない。

Stage 4の財務書類由来16期間データをamount dimension、「財政事情」をtiming dimensionとして組み合わせるのが適切である。

## 6. Next extraction opportunity

49号全てについて、次の項目を機械的に抽出すれば長期的なTreasury historyを作れる。

- 一時借入金の有無
- 基金繰替の借入月
- 基金繰替の返済月
- 県債残高
- 基金残高
- 県有財産中の基金・有価証券
- 県税・主要歳入の進捗率

今回のclient-ready改稿に必要な優先範囲としては、金利正常化以前との比較を含めR3～R7の借入返済パターンまで取得済みとする。
