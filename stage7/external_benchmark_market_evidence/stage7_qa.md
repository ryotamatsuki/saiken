# Stage 7 QA — External Benchmark & Market Evidence

**Review date:** 2026-09-16  
**Scope:** peer cases / maturity-matched market data / public treasury best practice

## 1. Completion matrix

| Requirement | Status | Note |
|---|---|---|
| 6 peer cases | PASS | 埼玉・静岡・熊本・新潟・香川・東京 |
| Hyogo reference | PASS | maturity/governance補助case |
| peer comparison | PASS | 共通CSV＋synthesis |
| deposit market data | PASS WITH SCOPE LIMIT | BOJ 1,000万円以上・1年定期＋普通預金、2023-01～2026-08 |
| JGB market data | PASS WITH SCOPE LIMIT | MOF直近1/2/5/10/20年auction average yields |
| maturity-matched comparison | PARTIAL BY PUBLIC SERIES | 1年のみnear-date direct match。2/5年同年限預金標準系列は未確認 |
| GFOA best-practice matrix | PASS | policy/program/cash/performance/MTM/market risk/diversification |
| Ehime control mapping | PASS | 数値limitは設定せず |
| source dictionary | PASS | 新規一次資料中心 |
| chapter evidence matrix | PASS | Ch.9–15へmapping |
| Python reproducibility | PASS | `build_market_spreads.py` + derived CSV |
| public-source only | PASS | 内部・非公表資料なし |
| copyright handling | PASS | 第三者PDF mirrorなし、公式URL＋派生情報のみ |

## 2. Numerical QA

Pythonで以下を再計算した。

- 埼玉R7債券比率: `8841 / 13601 = 65.002573%` → 公表表示65.0%
- 静岡R7債券比率: `5447 / 8835 = 61.652518%`
- 兵庫R7基金債券等比率（参考）: `2239 / 7928 = 28.241675%`
- 東京R8想定債券比率: `14800 / 34800 = 42.528736%` → 公表表示43%
- 2026-08 1年定期0.447% vs 1年T-Bill1.4332%: `98.62bp`
- 1年定期から2/5/10/20年国債への参考差: `126.10 / 179.20 / 254.80 / 340.90bp`

後4つは同年限比較ではないためCSVで `term_extension_not_maturity_matched` と明示した。

## 3. Source QA

- R6/R7/R8を混同しない。
- annual average / year-end / forecastを別field・注記で区別した。
- peer比率を優劣ranking又は愛媛推奨比率へ変換していない。
- 熊本21年・1,000億円、兵庫30年、東京10年はpeer-specific limitとして扱った。
- GFOA recommendationを日本法又は愛媛県現行規程として扱っていない。
- BOJ預金系列は自治体入札金利ではなくposted average market referenceと明示した。

## 4. Explicit public-data / ingestion gaps

### Gap A — same-tenor deposit series beyond 1 year

BOJ主要時系列では、1,000万円以上・1年定期と普通預金を確認できたが、同じ標準一覧で2年・3年・5年の大口定期を確認できなかった。個別銀行金利やinterpolationで埋めていない。

### Gap B — MOF constant-maturity CSV ingestion

財務省は主要年限の国債金利CSV (`jgbcm.csv`, `jgbcm_all.csv`) を公式公開している。ただし本実行環境では `text/csv` がweb reader非対応、containerは外部DNS不可で、全期間CSVを直接取込できなかった。代替として財務省の各auction result HTMLから1/2/5/10/20年の直近primary yieldsを一次資料で取得した。

### Gap C — peer granular limits

埼玉・静岡・香川等では、個別issuer limit、WAM、duration、現在の詳細数値limitの全ては公開確認できない。`not_publicly_confirmed` とした。

### Gap D — inherited Stage 6 disclosure gaps

- R7愛媛県詳細決算パッケージ
- 愛媛県公金管理方針の現行最新版本文

は引き続き公表待ち/未確認。

## 5. Completion judgement

**PASS WITH EXPLICIT PUBLIC-DATA GAPS**

完全な `STAGE 7 EXTERNAL EVIDENCE PASS` としない理由は、2年・5年等の預金と国債の完全な同年限時系列を公開標準系列から構築できていないためである。

一方、全面増補に必要な意思決定evidenceは十分に揃った。

- Ch.9: Stage6 cash-flow + GFOA/OECD/IMF + 香川/兵庫
- Ch.10: Stage6 fund pipeline + IMF surplus + peer allocation range
- Ch.11: 東京/熊本/兵庫 + GFOA market risk
- Ch.12: BOJ/MOF 1年matched reference + spread sensitivity
- Ch.13: GFOA market risk / MTM / diversification
- Ch.14: GFOA policy/performance + 新潟/熊本/東京/兵庫
- Ch.15: GFOA program + peer reform cases

## 6. Rewrite readiness

**READY FOR CLIENT-READY REWRITE**

残存gapは本文で明示し、R7詳細決算又は現行愛媛県公金管理方針が後日公開された場合に差し替える方式とする。これ以上の一般的な資料探索を全面増補開始の前提条件とはしない。
