# Stage 4 最終監査

| check | result | detail |
|---|---|---|
| temp rows | PASS | rows=64 |
| period totals | PASS | 16 periods |
| R5 historical max | PASS | max=96,801m |
| scenario sums | PASS | all scenarios sum to R6 baseline |
| scenario order | PASS | 11.6 < 33.4 < 44.1 |
| 15 chapters | PASS | chapters 1-15 |
| R7 unknown | PASS | no R6 substitution |
| public only | PASS | public-only |
| figures | PASS | fig1-fig9 |
| source IDs | PASS | undefined=[] |

## 判定

**FINAL EHIME ALM REPORT QA PASS**

## 監査原則
- 基金残高と即時必要現金を区別した。
- 基金繰替運用と基金取崩を区別した。
- R7実運用額が未確認の場合、R6数値で代替しない。
- 1年以内満期債を、資金需要日と満期が対応する場合のみ流動性資産に含める。
- 3ケースは政策設計レンジであり、統計的な最適解とは表現しない。
- 全国比較はtarget settingではなくexternal validity checkとして利用する。
- 計算はPythonで実施し、百万円の原数値を保持した。
