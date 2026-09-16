# Stage 7 — External Benchmark & Market Evidence Pack

**調査基準日:** 2026-09-16  
**目的:** canonical report全面増補前に、外部実務benchmark・市場データ・公金運用best practiceを固定する。

## 1. Scope

1. 他県6ケース: 埼玉・静岡・熊本・新潟・香川・東京
2. 補助reference: 兵庫
3. 市場データ: BOJ大口1年定期/普通預金、MOF直近1/2/5/10/20年国債auction yield
4. Best practice: GFOAを中心に、既存Stage4のOECD/IMF/World Bankを再整理
5. 愛媛向けcontrol mappingとCh.9–15 evidence mapping

## 2. Directory

### Peer cases

- `peer_cases/saitama_case.md`
- `peer_cases/shizuoka_case.md`
- `peer_cases/kumamoto_case.md`
- `peer_cases/niigata_case.md`
- `peer_cases/kagawa_case.md`
- `peer_cases/tokyo_case.md`
- `peer_cases/hyogo_reference_case.md`
- `peer_cases/peer_case_comparison.csv`
- `peer_cases/peer_case_synthesis.md`

### Market data

- `market_data/deposit_rates_by_maturity.csv`
- `market_data/deposit_rate_annual_summary.csv`
- `market_data/jgb_yields_by_maturity.csv`
- `market_data/maturity_matched_spreads.csv`
- `market_data/term_extension_spreads_reproduced.csv`
- `market_data/market_data_source_dictionary.csv`
- `market_data/market_data_methodology.md`
- `market_data/maturity_matched_market_analysis.md`
- `market_data/build_market_spreads.py`

### Best practice

- `best_practices/public_treasury_best_practice_matrix.csv`
- `best_practices/ehime_control_mapping.md`

### Integration / QA

- `source_dictionary.csv`
- `stage7_evidence_matrix.md`
- `stage7_qa.md`

## 3. Core findings

### Peer cases

債券比率はmanagement qualityの代理変数ではない。埼玉R7は65.0%、静岡61.65%、東京R7実績見込み35%、香川R6統一統計0%と大きく異なる。一方で、良好な事例に共通するのはcash-flowに応じた期間区分、一括運用、maturity diversification、annual plan、review/reportingである。

熊本は21年以内・原則満期保有・定額ladder・購入総額上限1,000億円を明示。東京は基金目的に応じて短期2年以下、中期2～5年、長期5～10年を使い分け、R8に複合ラダー型を導入。兵庫は歳計現金への繰替と2～30年の債券購入を同じ資金管理体系で運用している。

### Market data

BOJの1,000万円以上1年定期平均金利は2023年平均0.00458%から2026年1～8月平均0.36625%へ上昇。2026年8月は0.447%。同月の約1年T-Bill入札平均利回り1.4332%との差は98.62bp。

ただし2年・5年等については同じBOJ標準系列の大口定期金利を確認できず、2/5/10/20年国債との差は同年限spreadではなくterm-extension referenceとして管理する。

### Best practice

GFOAは、public fundsについてsafety・liquidityをreturnより優先し、rolling cash forecast、written investment policy、maturity/issuer diversification、market-value monitoring、四半期performance reporting等を推奨する。これを愛媛向けには13-week coverage、forecast error、maturity concentration、issuer exposure、mark-to-market、forced-sale count等の候補metricへ翻訳した。

## 4. Evidence handling

- public source only
- annual average / year-end / forecastを混同しない
- peer-specific limitを愛媛推奨limitへ転用しない
- GFOA等を日本法又は愛媛県現行規程とみなさない
- 公開PDFは原則mirrorせず、公式URL・抽出fact・derived dataを保存
- calculations are Python-reproducible

## 5. Gaps

1. BOJ標準主要時系列で2年・3年・5年大口定期を確認できず、1年以外の完全なmaturity matchは未構築。
2. MOF `jgbcm_all.csv` は公開済みだが、本実行環境でtext/csvを直接取込できず、直近auction HTMLで代替。
3. 一部peerのissuer/WAM/duration等の詳細limitはnot publicly confirmed。
4. Stage6から、R7愛媛県詳細決算と現行愛媛県公金管理方針本文が引き続きpending。

## 6. QA / readiness

**Stage 7 status:** `PASS WITH EXPLICIT PUBLIC-DATA GAPS`  
**Rewrite decision:** `READY FOR CLIENT-READY REWRITE`

残存gapはモデルの前提・留保として明示し、後日公開資料が追加された場合に更新する。現時点で一般的な追加資料探索を全面増補開始のblocking conditionとはしない。
