# Senior Manager Review — Ehime Fund & Bond Management Report

**Target:** `stage4/reports/ehime_fund_bond_management_consulting_report_R7_R8.md`  
**Review stage:** Stage 5 / pre-client submission  
**Assessment basis:** `report_quality_framework.md`  
**Status:** SENIOR MANAGER REVIEW REQUIRED

## 1. Executive assessment

現行稿は、初校としては強い。特に以下は維持すべきである。

- 中心的な問いを「債券比率」ではなく「支払能力を損なわず満期まで拘束可能な資金」に置いている。
- R6統一統計とR7実績、年間平均と期末値等の比較限界を比較的厳密に扱っている。
- 愛媛県の非公表の実運用を推定していない。
- 基金繰替を流動性需要のproxyとして構造化し、単純な他県追随を避けている。
- 151.27 / 435.32 / 574.70億円のscenario envelopeを提示している。
- 第11章で満期ラダー、第12章で追加収益、第13～15章でrisk / governance / roadmapまで接続している。

一方、client-ready水準へ上げるには、**分析の骨格に対して各章の説明密度が不足している**。問題は文章量そのものではなく、重要な数字・比較・モデルについて `Evidence → Interpretation → Ehime implication → Decision` の後半が短いことである。

現行稿は「良いanalytical draft」から「クライアントが判断に使えるconsulting report」へ移る直前の状態と評価する。

---

## 2. Preliminary score

| Axis | Max | Current | Senior Manager comment |
|---|---:|---:|---|
| Decision usefulness | 15 | 12 | 中心ケースと方向性は明確。最終判断条件をさらに明示したい |
| Problem framing | 10 | 9 | 問い・情報制約は非常に明確 |
| Storyline | 10 | 7 | 15章がやや並列的。第8章以降を一つのALMストーリーへ再接続したい |
| Evidence quality | 15 | 13 | 一次資料・定義差への配慮が強み。ケース別の原資料追跡をさらに整理できる |
| Analytical depth | 15 | 9 | Factは豊富だが、原因・代替説明・boundary conditionが不足 |
| Benchmarking | 10 | 8 | 全国比較は強い。代表県ケーススタディとtransferability分析が不足 |
| Recommendation quality | 10 | 7 | 提言は妥当だが、条件・優先順位・棄却条件を強めたい |
| Implementation readiness | 5 | 3 | roadmapあり。owner、decision forum、deliverable、KPIまで具体化余地 |
| Risk / limitations | 5 | 4 | 留保は良好。limit・trigger・stress responseへ深掘り余地 |
| Communication quality | 5 | 4 | Executive Summaryは強い。本文見出しと図表をmessage-ledに改善可能 |
| **Total** | **100** | **76** | **SENIOR MANAGER REVIEW REQUIRED** |

76点は「誤りが多い」という意味ではない。骨格は有効だが、client-ready gateのうちDecision LogicとImplementationに追加作業が必要という判定である。

---

## 3. Chapter-by-chapter review

優先度は次の3区分とする。

- **A — retain / polish:** 骨格・厚みとも概ね十分。編集中心。
- **B — deepen:** 骨格は維持し、解釈・含意・case evidenceを補強。
- **C — major deepen:** レポートの価値を決める中核章。大幅な分析増補が必要。

| Section | Rating | Review |
|---|---|---|
| Executive Summary | A | 現状の強み。大幅増量ではなくdecision messagesの整理 |
| Ch.1 Why now | B | 金融環境の説明を増やし過ぎず、「なぜ自治体ALMの問題になるか」を厚くする |
| Ch.2 Bond purchase surge | B | 急増の複数要因、反証、地方部門統計の限界を整理 |
| Ch.3 47-prefecture structure | B | 分布の意味、外れ値、時系列、愛媛の位置づけを解釈 |
| Ch.4 R7 changes | B | 5県比較をcase-basedにし、比率変化と利回り変化を分離して説明 |
| Ch.5 Cash retained by peers | B | cash ratio差の原因仮説とtransferabilityを深掘り |
| Ch.6 Bond instruments | B | 商品列挙から、信用・流動性・年限・規程のtrade-offへ進める |
| Ch.7 Comparable peers | B | 公式C群と運用実務peerの二軸をケーススタディ化 |
| Ch.8 Fund purposes | B | fund typologyをALM bucketに直接つなげる |
| Ch.9 Required liquidity | C | このレポートの核心。季節性、peak、P90、stressの意味を大幅補強 |
| Ch.10 Investable amount | C | 151/435/575億円のdecision logic、assumption、boundary conditionを明文化 |
| Ch.11 Portfolio / ladder | C | bucket設計、年限配分、商品配分、timing、代替設計を厚くする |
| Ch.12 Income effect | B | sensitivityからvalue caseへ。運用コスト・機会費用・同年限比較も論じる |
| Ch.13 Risk | C | risk taxonomyからlimits、metrics、stress responseまで具体化 |
| Ch.14 Governance | B | 方向性良好。RACI的責任、会議体、例外承認、記録を追加 |
| Ch.15 Roadmap | B | phaseだけでなく90-day deliverable、owner、KPI、go/no-go gateを追加 |
| Conclusion | A/B | 結論自体は明確。client decisionとnext gateをさらに短く強くする |

---

## 4. Most important gap: Chapter 10 decision logic

435.32億円は現行稿の中心的な数字であり、最もレビューを受ける可能性が高い。したがって「計算できた数字」ではなく「管理原則から導かれた政策ケース」として説明する必要がある。

client-ready版では少なくとも以下を明記する。

### 4.1 What it is

- R6基金総額を共通分母としたtop-down policy envelope。
- R7/R8基金別cash balanceによるbottom-up validation前の暫定ケース。

### 4.2 Why 435.32

- 過去最大基金繰替968.01億円を1年以内の流動性でcoverするという設計原則。
- 即時現金、near-cash、1年以内満期債をどう分担させるか。
- 即時現金をP75等に置く意味。

### 4.3 Why not 151.27

- 追加安全性と失われるterm premiumのtrade-off。
- どの予測能力が未整備なら保守ケースが妥当か。

### 4.4 Why not 574.70

- より高いcash-flow forecast精度、満期マッチング、運用管理能力を必要とすること。
- どのstressで流動性不足が起こり得るか。

### 4.5 What would invalidate 435.32

例：

- R7/R8基金別1～3年支出予定が想定以上。
- 財源対策用基金の即時利用可能性をより高く確保する必要。
- cash forecast errorが大きい。
- 運用規程上、想定商品・年限が利用できない。
- 県の実際の既保有債券が既に相当額あることが公表資料で判明。

この「棄却条件」があることで、モデルはむしろ信頼性が上がる。

---

## 5. Chapter 11 should become a target portfolio architecture, not a sample table

現行の6層bucketと1～10年ladderは有用だが、client-ready版では「なぜこの構造か」を明確にする。

追加すべき論点：

- immediate cash / near-cash / <=1y securitiesの機能差。
- 1～3年、3～5年、5年以上へ配分するliability-side rationale。
- equal ladderとfront-loaded ladderの比較。
- 1年以内101.05億円を月・四半期へ分割する考え方。
- 10年超を初期段階で抑制する理由。
- 国債60%等の商品構成例が「最適比率」でないことの説明。
- security typeよりmaturity matchを優先する場面。
- purchase timingを複数回に分ける理由と再投資方針。

図11のタイトルも、単に「標準ケースのモデル満期ラダー」ではなく、message titleへ変更したい。

例：

> 最大繰替を1年以内流動性で覆ったうえで、中長期資金を年次分散することで途中売却リスクを抑制できる

---

## 6. Peer benchmarking should move from table to mini case studies

優先して4～6県を選び、1県あたり半ページ程度のcase noteを作る。

候補軸：

- 高債券比率・明確な運用管理
- 中位比率
- 低比率だが利回り改善
- 財政構造が愛媛に近い
- governance disclosureが強い

各caseの共通テンプレート：

1. observed portfolio
2. liquidity retained
3. eligible instruments / maturity
4. governance
5. recent change
6. what Ehime can learn
7. what cannot be transferred directly

これにより「埼玉65%」のような数字が単なるランキングからmanagement insightへ変わる。

---

## 7. Risk chapter needs measurable controls

現状のrisk taxonomyは妥当。client-ready版では、各riskへcontrolを対応させる。

| Risk | Example management metric |
|---|---|
| Liquidity risk | minimum immediate liquidity, 13-week coverage ratio, stress coverage |
| Interest-rate risk | maturity concentration, weighted average maturity, duration proxy |
| Reinvestment risk | annual maturity concentration |
| Credit risk | issuer/category limits |
| Concentration risk | max exposure per issuer / maturity bucket |
| Forecast risk | forecast error, peak error |
| Operational risk | exception count, reconciliation status |
| Governance risk | overdue review, limit breach closure time |

具体的なlimit値は、愛媛県の現行規程・実運用を確認せず断定しない。

---

## 8. Implementation should have gates, not only phases

現行Phase 1～5は良い。次のgateを追加する。

### Gate 1 — Data Ready

基金別cash / non-cash、12m withdrawal、1–5y pipelineが揃う。

### Gate 2 — Liquidity Model Validated

13週予測とstress testが一定期間機能する。

### Gate 3 — Policy Ready

eligible assets、maturity limits、issuer limits、exception rulesが承認される。

### Gate 4 — Pilot Ready

小規模なladderで運用・monitoringを検証。

### Gate 5 — Scale Decision

liquidity compliance、forecast error、income uplift、operational burdenを評価し、拡大・維持・縮小を決める。

---

## 9. Recommended rewrite sequence

改稿順序は章番号順ではなく、decision value順とする。

1. Ch.9 Required liquidity
2. Ch.10 Investable amount
3. Ch.11 Portfolio / ladder
4. Ch.13 Risk
5. Ch.14 Governance
6. Ch.15 Roadmap
7. Ch.4–7 Peer benchmarking
8. Ch.12 Value case
9. Ch.8 Fund typology
10. Ch.1–3 Context
11. Executive Summary / Conclusionを最後に再調整

この順序なら、核心モデルを先に完成させ、そのロジックに合わせて前半とExecutive Summaryを整合させられる。

---

## 10. Client-ready target

次版では、100点満点の単純目標より、以下のgateを優先する。

- Evidence integrity: PASS
- Decision logic: PASS
- Implementation readiness: PASS
- Communication: PASS
- Total score: 85点以上を最低ライン、90点以上を最終目標

特に、Ch.9–11が「公開情報だけでここまで言える」「ここから先はこの追加データが必要」という境界を明確に示せれば、本レポートの独自価値は大きく高まる。
