# 主要15基金の1～5年cash-flow復元可能性

## 1. Scope and materiality

R8一般会計基金繰入は32基金、351.85764億円。取崩額上位15基金は336.78819億円で、全体の95.717%を占める。

したがってclient-ready版のbottom-up ALMでは、全基金を均等に深掘りするより、まずこの15基金の支出時期・事業終期・contingency性を分類する方がmaterialityに即している。

## 2. Reconstruction classes

### A. 比較的復元しやすい — multi-year project pipelineが公開

#### 県立学校教育環境整備基金

R8取崩: 27.46937億円。

県立学校振興計画はR5～R14の10年間で、前期R5～R9・後期R10～R14に区分される。R8当初予算では県立学校振興計画校舎等整備事業28.49787億円が基金充当事業として明記され、整備完了率100%の対象期間はR5～R10。個別校の完成予定も示される。

Sources:
- https://www.pref.ehime.jp/uploaded/attachment/169539.pdf
- https://www.pref.ehime.jp/uploaded/attachment/38042.pdf

ALM implication: 1～5年のcapital pipelineへ満期を合わせるべき基金。残高全体を長期coreとみなさない。

#### 県有施設更新整備基金

R8取崩: 22.42660億円。

新居浜警察署の公開工程では、R7～R8庁舎建築、R9旧庁舎解体、R10車庫建築、R11宿舎建築まで工程が見える。

Source:
- https://www.pref.ehime.jp/uploaded/attachment/137970.pdf

ALM implication: 大型施設案件を束ねたmulti-year capital liabilityとして扱える。基金充当全案件を同じ形式で集めれば1～5年bucketをかなり精緻化できる。

#### とべ動物園魅力向上基金

R8取崩: 3.68625億円。

とべ動物園の魅力向上行動計画はR1～R9で、第3期がR7～R9。施設・動物取得・ソフト事業へ基金を充当。

Sources:
- https://www.pref.ehime.jp/uploaded/attachment/49083.pdf
- https://www.pref.ehime.jp/uploaded/attachment/24811.pdf

ALM implication: 少なくともR9までのprogram horizon内へ満期を合わせる。計画終期を越える長期運用を安易に置かない。

#### 森林環境保全基金

R8取崩: 8.19662億円。

R8運営委員会資料ではR7/R8の基金積立、税収、前年度残額、指定事業・公募事業の予算を同一表で比較できる。森林環境税の課税期間も現行条例で確認できる。

Sources:
- https://www.pref.ehime.jp/page/6946.html
- https://www.pref.ehime.jp/uploaded/attachment/175100.pdf

ALM implication: 毎年度のtax inflowとannual program outflowをrolling forecast化しやすい。将来年度の個別事業額は予算成立前には確定しないため、1年bucketは高精度、2～5年はpolicy-based forecastとする。

## 3. Annual rolling programとして復元する基金

#### 地域医療介護総合確保基金

R8取崩: 34.21152億円。

医療分は2026-05-31現在約64.73億円。基金終了時期は設定されていない。R7年度計画まで公開され、R9年度事業提案もR8中に募集済みであるため、少なくとも翌年度pipelineの形成時期が分かる。

Source:
- https://www.pref.ehime.jp/page/4330.html

一方、地域医療構想調整会議ではR8要望・一部実績の個別資料が非公開とされる場合がある。

Sources:
- https://www.pref.ehime.jp/site/tiikiiryokoso/4314.html
- https://www.pref.ehime.jp/site/tiikiiryokoso/4317.html

ALM implication: 12～24か月はannual planning cycleからかなり復元できるが、3～5年を確定債務とみなすのは不適切。rolling pipelineとして毎年更新する。

#### 企業立地促進基金

R8取崩: 23.25831億円。

R7に設置。R8当初予算で30.73008億円を基金へ積み立てる。東予港西条地区ではR8年度中の産業用地公募を見据えた事業等が基金充当とされる。企業立地奨励は案件成立に依存するため、支出タイミングはcontingent liabilityに近い。

Sources:
- https://www.pref.ehime.jp/uploaded/attachment/170546.pdf
- https://www.pref.ehime.jp/uploaded/attachment/157410.pdf

ALM implication: committed projects / probable pipeline / uncommitted reserveに分ける。未確定奨励金枠を全額即時現金とする必要はないが、案件成立時の支払条件を確認せず長期固定しない。

#### デジタル社会形成推進基金

R8取崩: 13.95915億円。

現行DX実行プランは長期的なDX展開の財源として基金を位置付け、R8までの現行戦略・KPIが多数存在する。R7は官民共創拠点整備等でも基金充当が確認できる。

Sources:
- https://www.pref.ehime.jp/page/60521.html
- https://www.pref.ehime.jp/uploaded/attachment/137961.pdf

ALM implication: R8までの高確度支出をshort bucketへ置き、R9以降は次期DX計画が明らかになるまでcore判定を保守的にする。

#### 農林水産業体質強化緊急対策基金

R8取崩: 2.92212億円。

基金全体の統一5年表は確認できないが、個別事業には複数年の数値計画がある。例えば媛スマ関連事業はR7:34百万円、R8:67百万円、R9:96百万円、R10:125百万円という事業想定を公表し、基金充当を明示する。

Source:
- https://www.pref.ehime.jp/uploaded/attachment/137968.pdf

ALM implication: 基金全体ではなく、主要な基金充当事業を積み上げるbottom-up方式が適する。

#### 資源循環促進基金

R8取崩: 2.59961億円。

R8海洋ごみ対策等の基金充当事業は予算資料で確認できるが、R9以降の確定額は未公表。

Source:
- https://www.pref.ehime.jp/uploaded/attachment/169532.pdf

ALM implication: annual programとして1年以内を厚く見て、2～5年は継続事業のpolicy forecastとする。

#### スポーツ推進基金

R8取崩: 5.31301億円。

第2期愛媛県スポーツ推進計画と年度事業が公開されているが、基金取崩を1～5年の年度別金額に固定した表は確認できない。

Source:
- https://www.pref.ehime.jp/soshiki/23/index.html

ALM implication: annual budget cycleを基準にrolling forecast。基金残高全体の長期固定は避ける。

## 4. Financial-policy / debt-service funds

#### 財政基盤強化積立金

R8取崩: 107.00億円。

R8予算資料ではR6末260億円、R7積立27・取崩60・R7末227億円見込、R8積立1・取崩107・R8末121億円見込を公表。

#### 県債管理基金

R8取崩: 37.56450億円。

同資料ではR6末230億円、R7積立16・取崩37・R7末209億円見込、R8積立44・取崩37・R8末216億円見込を公表。

Common source:
- https://www.pref.ehime.jp/uploaded/attachment/169527.pdf

ALM implication: この2基金は「余剰資金」ではなく財政buffer / debt-service liabilityと一体で分析する。R9以降の1～5年cash-flowを作るには、中期財政見通し、県債元金償還schedule、次期財政運営方針との接続が必要。

## 5. Low-predictability / contingent funds

#### 職員退職手当基金

R8取崩: 37.00億円。

R8当初の取崩額は確認できるが、公開資料から基金取崩の1～5年scheduleを直接確認できない。

ALM implication: 退職手当支出自体は人員年齢構成から一定程度予測可能なはずだが、公開情報のみではfund-level cash-flowに落とし切れない。R8の37億円は12m committed outflowとして扱い、将来年度は保守的留保が必要。

#### 災害に強い愛媛づくり基金

R8取崩: 7.84577億円。

平時の防災・減災事業は予算化されるが、災害発生時の支出は外生的。

ALM implication: mean forecastではなくstress reserveとして扱う。3～5年の「予定支出額」を一点予測するより、即時利用可能性・stress coverageを管理する。

## 6. Newly established fund

#### 官民共創推進基金

R8取崩: 3.33536億円。

R8設置、基金積立額39.4億円。条例には明示的なsunsetはない。

Sources:
- https://www.pref.ehime.jp/uploaded/attachment/174646.pdf
- https://www.pref.ehime.jp/site/gikai/135186.html

ALM implication: 新設直後で過去run-rateがないため、R8実績とR9予算要求が揃うまで3～5年のcore資金判定を慎重にする。

## 7. What can be used immediately in Ch.9–11

公開資料だけでも、上位15基金を次のliability classesへ分けられる。

- fiscal/debt-service buffer
- scheduled capital pipeline
- annual rolling program
- contingent/stress reserve
- newly established / insufficient history

これにより、`cash balance - floor - 12m withdrawal - 1-3y pipeline - stress reserve - non-cash requirements` の各控除項目を基金ごとに同じ意味で置くのではなく、liability type別に設計できる。

## 8. Remaining critical gap

最大の残存ギャップはR7末又はR8期首の**基金別cash balance**である。これが公表されれば、上記cash-flow evidenceと接続してbottom-up investable amountをかなり実用的な形で計算できる。

また、公開資料のみでは一部基金についてR9～R12の確定支出額が存在しない。これは資料不足だけでなく、政策・災害・企業立地等の性質上、将来支出そのものが未確定である。この場合は無理に一点予測せず、committed / probable / contingent の三層でモデル化する。
