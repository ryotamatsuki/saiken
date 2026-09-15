# Stage 3 最終数値監査

| check | result | detail |
|---|---|---|
| 47 prefectures | PASS | rows=47, unique=47 |
| comparability counts | PASS | {'D': 28, 'B': 6, 'C': 6, 'E': 5, 'A': 2} |
| core ratio sums | PASS | cash+bond=100 for 5 core prefectures |
| core range | PASS | range=49.770785pt |
| report chapters | PASS | chapters 1-14 present |
| executive summary | PASS | present |
| source IDs | PASS | used=19, undefined=[] |
| source dictionary unique | PASS | rows=26, unique=26 |
| no internal info | PASS | public-only statement present |
| no forced zero | PASS | missing-data rule present |
| period distinction | PASS | period distinction present |
| securities/bond distinction | PASS | definition distinction present |
| chart refs | PASS | fig1-fig6 referenced |

## 判定

**FINAL DATA/REPORT QA PASS**

## 監査原則
- 平均残高と年度末残高を同一ランキングに入れない。
- 基金と公金全体を同一分母で比較しない。
- 実績、見込、計画を分離する。
- 有価証券と債券を同義扱いしない。
- 検索で未確認の項目をゼロとしない。
- R4～R6総務省表31と各県独自のR7資金運用実績は別系列として扱う。
- 比率、中央値、四分位点、構成比はPythonで再計算した。
- 本文の主要数値はSource IDを介して一次資料辞書へ追跡可能にする。
