# 愛媛県における基金の債券運用高度化に向けた調査分析
## ― 全国のR7以降の運用動向、必要流動性及び基金別ALMからみた運用余地 ―

**調査基準日：2026年9月16日**  
**想定読者：愛媛県の基金・公金・財政・会計・資金運用担当者**  
**情報範囲：国・地方公共団体・国際機関・学術機関等が公表した情報のみ。内部資料、庁内限定資料及び非公表の実運用情報は使用していない。**

> 本報告書の中心的な問いは「愛媛県の債券比率を何％にすべきか」ではない。各基金の用途と支出時期、年度内の資金需要、財政上のバッファを先に把握し、**満期まで拘束しても支払能力を損なわない資金はいくらか**を求め、その残余をどの年限・商品へ配分するかを検討することである。

### 本報告書の読み方

- **確認事実（Confirmed fact）**：公表一次資料又は再現可能な公的統計から確認した事実。
- **本調査の解釈（Analytical interpretation）**：確認事実をつないだ分析。愛媛県の実運用を推定したものではない。
- **モデル／シナリオ（Model / scenario）**：公開情報だけから政策判断を比較するために置いた仮定。現行方針・最適値ではない。
- **提言（Recommendation）**：安全性・流動性・法令・説明責任を優先制約とし、その範囲で導いた実施案。
- **公開情報上の限界（Public-data limitation）**：2026年9月16日時点で、R7愛媛県詳細決算パッケージ、現行最新版の愛媛県公金管理方針本文、1年超の完全な同年限預金・国債比較系列は未確認又は未取得である。

---

# Executive Summary

## What changed — 超低金利を前提とした公金運用から、流動性と期間対価を管理する局面へ移った

日本銀行「資金循環統計」を基にした2026年9月13日付日本経済新聞の集計では、地方公共団体部門が保有する国債・財投債の残高は2025年3月の163億円から2026年3月には約1.6兆円へ増加した。これは「購入額が100倍」というフロー比較ではなく、**保有残高が約100倍となったストック比較**であり、対象も都道府県だけではない。この限定を置いても、地方公共団体にとって債券が再び主要な運用選択肢になっていることを示すマクロな変化である（出典：`NIKKEI-2026-09-13`, `BOJ-FFA-METHOD`）。

背景には、日本銀行が2024年3月にマイナス金利政策・イールドカーブ・コントロールを終了し、その後政策金利を段階的に引き上げ、長期国債買入れも減額してきたことがある。一方、預金金利も上昇しており、「国債利回りが上がった＝預金から債券へ移すべき」という単純な関係ではない。2026年8月の日本銀行「預入金額1千万円以上・1年定期」平均金利は0.447％、2026年8月19日の約1年国庫短期証券の募入平均利回りは1.4332％で、near-dateの市場参考差は98.62bpであった。ただし、預金側は店頭表示平均、債券側は国債primary auctionであり、愛媛県が実際に得られる追加収益を表すものではない（出典：`BOJ-IR02`, `MOF-TBILL-1401`; 本調査Python計算）。

## What we found — 愛媛県の制約は「基金残高」ではなく、基金が年度内Treasury liquidityを担っていることである

総務省の全国統一統計によるR6年度末の愛媛県基金総額は1,302.28億円、現金・預金1,286.87億円、有価証券15.40億円、有価証券比率1.18％である。R6全国47都道府県の有価証券比率は単純平均12.30％、中央値4.36％、第1四分位1.40％、第3四分位13.96％であり、愛媛県は第1四分位を下回った。ただし、これはR6年度末の統一統計であり、R7現在の実運用を示さない（出典：`STAT-R6-MIC`）。

より重要なのは資金需要である。R3～R6の財務書類から構造化した16期間の基金繰替額は203.51～968.01億円で、平均624.39億円、中央値659.18億円、P75 765.91億円、P90 841.26億円であった。季節平均は4～5月775.72億円、夏期325.31億円、秋期614.24億円、年度末782.29億円である。さらに県「財政事情」を確認すると、R3～R7にかけて、概ね4・5月に基金から借入れ、8月までに返済し、その後8月・11月に再度借り入れ、年度末までに返済する循環が反復している。したがって、愛媛県の基金は長期貯蓄だけでなく、年度内の資金不足を埋めるTreasury liquidity poolとして機能している（出典：`EHIME-FS-R3`～`EHIME-FS-R6`, Stage6 `finance_affairs_cashflow_findings.md`; 本調査集計）。

R8当初予算では一般会計への基金繰入が32基金、351.86億円である。Stage6で深掘りした取崩額上位15基金だけで336.79億円、全体の95.717％を占める。これらは、財政・県債管理、施設・学校整備、医療介護、退職手当、企業立地、災害対応等であり、同じ「基金」であっても経済的な資金拘束可能期間は大きく異なる。したがってALMは基金総額ではなく、**基金別cash balanceから、法定・政策フロア、12か月以内支出、1～3年pipeline、stress reserve、非現金・回転資産を控除する**形で行う必要がある。

## What it means — 435.32億円は「推奨購入額」ではなく、最大繰替を1年以内流動性で覆う中心シナリオである

R6基金総額1,302.28億円を共通分母としたtop-down policy envelopeは、保守151.27億円（11.6％）、標準435.32億円（33.4％）、積極574.70億円（44.1％）である。これは全国平均や他県比率から逆算したものではない。

標準ケースは、過去最大の基金繰替968.01億円を、即時現金765.91億円、near-cash 101.05億円、1年以内満期債101.05億円の合計で100％カバーする。その外側の435.32億円を1～10年程度までの満期bucketへ配置する考え方である。即時現金をP75に近い水準へ置くため、通常時の厚い流動性を維持しつつ、最大繰替までの差をnear-cashと1年以内満期債で埋める。

一方、R7末又はR8期首の基金別cash balanceは2026年9月16日時点で詳細決算の公表を確認できず、bottom-upで435.32億円を完全に裏付ける段階ではない。したがって標準ケースは、**現時点の中心検討ケース／上限管理の外枠**として扱い、R7詳細決算公表後に再計算する。

## What we recommend — 比率目標ではなく、流動性を先に固定する段階導入とする

本報告書が提案する順序は次のとおりである。

1. **13週・1年・3～5年のcash-flow forecastを整備する。** 13週は週次、1年は月次、3～5年は事業・基金別pipelineとして管理する。
2. **基金別ALM台帳を作る。** cash / non-cash、法定・政策フロア、12か月取崩、1～3年pipeline、stress reserve、sunsetを登録する。
3. **流動性を階層化する。** immediate cash、near-cash、1年以内満期資産を分け、最大繰替・P90・forecast errorでstress testする。
4. **残余だけをラダーへ配分する。** 初期段階は10年以内を基本とし、1～3年、3～5年、5～10年をliability側から決める。
5. **少額pilotから開始し、KPIでscale decisionを行う。** yieldだけでなく、13-week coverage、forecast error、maturity concentration、forced-sale count、mark-to-market、exception countを評価する。

他県から学ぶべきなのは比率ではなく管理構造である。埼玉県は期間別bucket、静岡県は1年以上運用可能資金の切り分け、熊本県は21年以内・定額ラダー・原則満期保有・購入総額上限、東京都は基金目的に応じた2年以下／2～5年／5～10年の複合ラダー、兵庫県は歳計現金への繰替と2～30年の満期分散を一つの資金管理体系で運用している。これらの**考え方**は参考になるが、数値limitや比率を愛媛県へ移植してはならない。

## What must happen first — 最初の90日は「購入」ではなく、Data ReadyとLiquidity Model Validatedに使う

最初の90日で優先すべき成果物は、①基金別ALM台帳、②13週cash forecast、③12か月maturity/outflow calendar、④現行公金管理方針上のeligible assets・maturity・issuer・exception rule確認、⑤stress test、⑥pilot設計である。これらが揃う前に標準435.32億円を一括して長期債へ移すことは提言しない。

---

# 第1章　金利正常化は「債券を買う好機」ではなく、公金ALMを再設計する契機である

## 1.1 地方公共団体の国債・財投債保有急増は、運用環境の変化を示すが、都道府県基金の購入フローではない

2026年9月13日付日本経済新聞は、日本銀行の資金循環統計を基に、地方公共団体部門の国債・財投債保有残高が2025年3月の163億円から2026年3月に約1.6兆円となったと報じた。ここで重要なのは、①購入額ではなく保有残高、②都道府県だけでなく地方公共団体部門全体、③資金循環統計には推計・市場価格評価を含む、という三点である。したがって1.6兆円を「都道府県基金が1年間に買った国債」と解釈してはならない（出典：`NIKKEI-2026-09-13`, `BOJ-FFA-METHOD`）。

それでも、地方公共団体が債券を再び主要な運用対象として認識していることを示す背景指標としては有用である。超低金利期には預金と国債の双方の収益が極めて低く、長期拘束を受け入れる経済的対価が小さかった。金利正常化後は、短期・中期・長期で期間対価が再び観察できるようになり、資金の「いつまで使わないか」を把握する価値が高まった。

## 1.2 金利上昇は預金にも波及しているため、債券比率ではなく機会費用を比較すべきである

日本銀行は2024年3月に金融政策の枠組みを見直し、2024年7月、2025年1月、2025年12月、2026年6月と政策金利を段階的に引き上げた。同時に預金金利も上昇している（出典：`BOJ-POLICY-2024-03`ほか、`BOJ-IR02`）。このため、債券投資の経済価値は「債券利回り」ではなく、同程度の拘束期間を持つ預金等の代替資産との差で測る必要がある。

愛媛県への含意は、利回りが高い年限を探すことではない。まずcash-flowから拘束可能期間を決め、その期間内で預金・短期債・中長期債を比較することである。**年限は利回りから逆算せず、資金需要から決める。**

## 1.3 管理職が判断すべき問いは「買うか否か」ではなく「どの資金を何年まで拘束できるか」である

この問いに変えると、議論は商品選択からALMへ移る。1か月後に必要な資金は高利回りでも10年債へ置けない。一方、5年間使用予定が低い資金を常に普通預金へ置けば、流動性を過剰に保有する可能性がある。したがって、本報告書は以降、全国比較を「目標比率探し」ではなく、愛媛県のliability sideを設計するためのbenchmarkとして用いる。

---

# 第2章　自治体の債券運用拡大は金利正常化だけでは説明できず、預金再評価・再投資・制度変更も含む

## 2.1 確認できるのは「金融環境」と「複数自治体の制度変更」が同時に起きたことである

金利正常化後、東京都はR8計画で特定目的基金の一括運用・複合ラダーを導入し、新潟県はR7に基金一括運用を開始した。富山県等でも対象債券・年限の見直しが確認される。これらは、金融環境の変化が資金管理制度を見直す契機になったことを示す一方、個々の自治体が同じ理由・同じ速度で債券を増やしたことまでは示さない（出典：`TOKYO-R8-PLAN`, `NIIGATA-POLICY`, Stage3/4 peer data）。

## 2.2 反証：債券比率が上がらなくても運用利回りは上昇している

埼玉県では基金債券比率がR6の66.6％からR7の65.0％へやや低下する一方、基金運用利回りは0.349％から0.609％へ上昇した。千葉県も債券比率は60.0％から60.1％とほぼ横ばいだが、利回りは0.331％から0.482％へ上昇している。したがって、金利正常化の便益は、新規債券購入だけでなく、預金金利上昇、既存債償還後の再投資、運用競争性の改善等を通じても生じる。

愛媛県で評価すべきKPIも、債券比率そのものではない。追加収益、minimum liquidity compliance、forced-saleの有無、cash forecast精度等を同時に見る必要がある。

## 2.3 本調査の解釈と限界

本調査は、金利正常化が地方公共団体の債券保有増加を促した可能性を合理的な説明として扱うが、資金循環統計から因果効果を識別したものではない。政策判断に必要なのは因果推定の精緻化より、現在の市場環境で愛媛県が負担する流動性の機会費用を可視化することである。

---

# 第3章　R6全国分布では愛媛県は現預金中心だが、それだけでは運用余地を判断できない

## 3.1 全国47都道府県の分布は「単一の適正比率」が存在しないことを示す

総務省のR6全国統一統計では、都道府県の基金有価証券比率の単純平均は12.30％、中央値4.36％、第1四分位1.40％、第3四分位13.96％である。愛媛県は1.18％で、第1四分位を下回る（出典：`STAT-R6-MIC`; 本調査集計）。

この位置は「債券運用余地があり得る」ことを示すスクリーニング情報にはなるが、「全国平均まで増やすべき」という根拠にはならない。基金の用途、歳計現金との関係、取崩予定、条例・運用規程が都道府県ごとに異なるためである。

## 3.2 愛媛県の低比率は、まずliability sideと照合して初めて意味を持つ

R6年度末の愛媛県基金総額1,302.28億円に対し現金・預金は1,286.87億円、有価証券は15.40億円であった。もし基金の大半が長期に使用予定のない資金なら、1.18％は低い可能性がある。しかし実際には基金繰替が最大968.01億円、R8基金取崩予算が351.86億円あり、非現金資産やsunset基金も存在する。したがって、低い有価証券比率だけを見て「余剰現金」と評価することはできない。

## 3.3 判断：全国分布は外部妥当性の確認に使い、投資可能額は愛媛県自身のcash-flowから求める

全国比較は、愛媛県のシナリオが極端な設計になっていないかを確認する用途に限定する。具体的な投資可能額は第8～10章で、基金用途・cash-flow・stressを積み上げて求める。

---

# 第4章　R7実績は「高債券比率モデル」一色ではなく、複数の公金管理モデルが併存する

## 4.1 直接比較できる5県でも債券比率は15.2～65.0％まで分散する

R7の基金年間平均残高について現預金と債券を同一基準で比較できる5県では、鳥取15.2％、福島25.1％、千葉60.1％、静岡61.7％、埼玉65.0％であり、単純平均は45.4％である。ただし、開示可能性によるサンプル選択が強く、全国平均とは扱わない。福岡県R7年度末の債券比率74.9％も確認できるが、年間平均ベースの5県とは別基準である（出典：`R7-FUKUSHIMA`, `SAITAMA-R7`, `R7-CHIBA`, `SHIZUOKA-R7`, `R7-TOTTORI`, `R7-FUKUOKA`）。

## 4.2 埼玉県 — 高い債券比率より「期間別に商品を使い分ける」管理が参考になる

埼玉県R7基金年間平均残高は1兆3,601億円、現預金4,760億円、債券8,841億円、債券比率65.0％、運用利回り0.609％である。公表説明では、短期は普通預金、中期は定期預金、長期の1年超資金は債券という期間区分を持ち、一括運用を行う（出典：`SAITAMA-R7`, `SAITAMA-MGMT`）。

愛媛県が学ぶべきなのは65％という比率ではなく、「必要時期を先に判定して資産を割り当てる」仕組みである。愛媛県では基金繰替の規模が大きいため、埼玉県と同じ比率を置く前に、年度内liquidityをどのbucketで保持するかを決める必要がある。

## 4.3 静岡県 — 一括運用と競争的引合いは、債券だけでなく預金運用の高度化も含む

静岡県R7基金年間平均残高は8,835億円、現預金3,388億円、債券5,447億円、債券比率61.65％、全体利回り約0.535％である。1年以上運用可能な資金を債券へ振り向けつつ、預金も競争的に運用している（出典：`SHIZUOKA-R7`）。

これは、運用高度化を「債券化」と同義にしない重要な反証である。愛媛県でも、短期資金については預金引合いの改善、長期資金については債券という役割分担を設計する方が合理的である。

## 4.4 新潟県 — R7の一括運用導入は、policy・annual plan・reportingを同時に整備した改革例である

新潟県はR7に一括運用を導入し、預金、国庫短期証券、国債、政府保証債、地方債、JFM債、財投機関債等を対象とする公金管理方針・年度計画を整備した。R7の公金運用収入は19.05117433億円と公表されているが、これは基金のみのallocationではない（出典：`NIIGATA-POLICY`, `NIIGATA-R7`）。

愛媛県への含意は、商品拡大だけを先行させず、cash-flow forecast、年度計画、会議体、実績公表を同時に設計することである。

---

# 第5章　他県の「残す現金」は35～85％に分散し、必要流動性は比率ではなくcash-flowから決まる

## 5.1 現預金比率の差は運用姿勢だけでは説明できない

R7直接比較5県の現預金比率は、埼玉35.0％、静岡38.3％、千葉39.9％、福島74.9％、鳥取84.8％である。現金・預金は、日々の支払、歳計現金への繰替、年度内事業、債券満期までのつなぎ、予測誤差・災害対応等の複数機能を持つ。したがって、現預金比率が高いことを非効率と即断できない。

## 5.2 香川県と兵庫県は、基金をTreasury liquidityとして見るうえで重要な比較対象である

香川県R6全国統一統計では基金有価証券比率0％、現預金100％であった。R7と同一定義のallocationは未確認であるが、県「財政事情」では基金の譲渡性預金等を見合いとして歳計現金不足時に当座借越を利用する資金繰りが確認できる（出典：`KAGAWA-R6`, `KAGAWA-FISCAL-155`）。これは、基金の価値が運用利回りだけでなく、年度内liquidity facilityとしての機能にもあることを示す。

兵庫県R7基金年間平均残高は7,928億円、債券等2,239億円、比率28.24％、運用利回り0.631％である。歳計現金への繰替を優先し、余資を預金・債券へ配分する一方、R8新規購入計画では2～30年へ満期を分散している（出典：`HYOGO-R7R8`, `HYOGO-MGMT`）。愛媛県と同様、基金のTreasury機能と中長期運用を両立させる事例として有用である。

## 5.3 判断：愛媛県の比較軸は「現金比率」ではなく「どの需要をどの流動性階層で覆うか」である

必要流動性のすべてを普通預金で保持する必要はない。直近支払はimmediate cash、数週間～数か月はnear-cash、支払日が読める年度内資金は1年以内満期資産、1～5年は確度の高いpipelineに満期を合わせる。このliquidity continuumを構築して初めて、中長期債へ配分できる残余が定義できる。

---

# 第6章　商品より先に満期を決めることが、他県の高度運用に共通する

## 6.1 国債だけでなく地方債・政府保証債・JFM債・財投機関債等が使われている

全国事例では、国債に加え、地方債、政府保証債、地方公共団体金融機構債、財投機関債、高速道路会社債等が対象となる例がある。ただし対象範囲は各自治体の法令解釈・公金管理方針・信用基準で異なる。愛媛県の現行最新版「公金管理方針」本文は公開検索で確認できないため、本報告書は他県商品を愛媛県で購入可能と断定しない（出典：Stage6 `public_funds_policy_public_status.md`）。

## 6.2 熊本・東京・兵庫は、年限管理の異なる三つのモデルを示す

熊本県の公金管理方針は、対象債券、21年以内、原則満期保有、定額ラダー、債券購入総額上限1,000億円等を明文化している（出典：`KUMAMOTO-POLICY`）。東京都R8計画は、短期2年以下、中期2～5年、長期5～10年を基金目的・取崩予定へ対応させ、特定目的基金で一括運用・複合ラダーを導入する（出典：`TOKYO-R8-PLAN`）。兵庫県は2・3・5・10・20・30年等へ購入時期・年限を分散する（出典：`HYOGO-R7R8`）。

三者に共通するのは「最も高い利回りの年限を選ぶ」ことではない。資金需要を先に区分し、満期を分散し、原則として途中売却を必要としない構造を作ることである。

## 6.3 愛媛県への提言：初期設計は10年以内とし、5年超はdocumented liability matchをgateとする

愛媛県は基金繰替が大きく、R7末cash balanceと基金別3～5年pipelineが未確定である。この状態で20年・30年まで一気に長期化する根拠は弱い。初期モデルでは10年以内でladderを構築し、5年超は使用予定が低いことを文書化できる資金だけに限定する。10年超は将来、長期的に拘束可能な資金がbottom-upで確認され、governance・market-value monitoringが定着した後の別途判断とする。

---

# 第7章　愛媛県のbenchmarkは「財政構造」と「運用実務」を分けて選ぶ

## 7.1 公式類似団体は財政構造を見るbenchmarkであり、運用手法の模範とは限らない

愛媛県のR6財政比較分析表では財政力指数0.45でCグループに属し、北海道、石川、新潟、富山、福井、山梨、奈良、山口、香川、愛媛、熊本の11道県が含まれる。愛媛県の標準財政規模は3,713.60億円である（出典：`EHIME-R6-FISCAL-COMP`）。

同じCグループでも、新潟はR7一括運用を導入、熊本は詳細な公金管理方針を持ち、香川はR6統一統計上現預金中心である。財政力指数が近いことは、運用モデルが同じことを意味しない。

## 7.2 ALM類似団体と先進実務peerを分ける

R6全国統一データで標準財政規模、基金総額、基金／標準財政規模、歳出規模、有価証券比率、現預金比率を標準化したALM類似度では、徳島、香川、青森、沖縄、和歌山、群馬、三重等が愛媛に近い。これらの多くはR6時点で現預金中心である。一方、埼玉・静岡・熊本・東京・兵庫は、比率や規模が愛媛と異なっても、bucket、ladder、policy、reportingの実務benchmarkとして価値が高い。

したがって本報告書では、

- **構造benchmark**：香川、徳島等。資金規模・財政構造の近さを確認する。
- **運用実務benchmark**：埼玉、静岡、新潟、熊本、東京、兵庫等。管理手法を比較する。

と役割を分ける。

## 7.3 Transferability matrix — 移植するのは「仕組み」、移植しないのは「比率・年限・上限」

| Peer | 愛媛に参考になる仕組み | 直接移植しないもの |
|---|---|---|
| 埼玉 | 短期・中期・長期の期間bucket、一括運用、原則満期保有 | 債券比率65％ |
| 静岡 | 1年以上運用可能資金の切り分け、預金も含めた競争性 | 債券比率61.7％ |
| 新潟 | policy・annual plan・会議体・一括運用を同時導入 | 公金全体収入を基金収入とみなすこと |
| 熊本 | eligible assets、年限、ladder、例外売却、上限を明文化 | 21年、1,000億円というpeer固有limit |
| 香川 | 基金を年度内資金繰りへ接続するTreasury視点 | R6有価証券0％を現行目標とすること |
| 東京 | 2/5/10年bucket、複合ladder、基金目的別期間設計 | 都規模の運用額・組織体制 |
| 兵庫 | 繰替需要と長期債の併存、年度計画、資金管理委員会 | 30年年限 |

判断は明確である。愛媛県は他県の「何％」ではなく「どう判定し、どう統制しているか」を採用すべきである。

---

# 第8章　基金を会計上の名称ではなくeconomic durationで分類すると、運用可能期間が見える

## 8.1 同じ「基金」でもliability profileは異なる

基金を一括して長期資金とみなすとALMを誤る。財政基盤強化積立金は財政shockへのbuffer、県債管理基金はdebt-service liability、県有施設更新整備基金・県立学校教育環境整備基金はcapital pipeline、地域医療介護総合確保基金はannual rolling program、災害に強い愛媛づくり基金はcontingent reserve、美術品等取得基金は非現金資産を含む定額運用基金である。

本報告書では、少なくとも次の8類型で管理する。

1. fiscal stabilization
2. debt service
3. capital pipeline
4. annual / rolling program
5. sunset fund
6. statutory / contingent reserve
7. revolving fund
8. non-cash endowment / fixed asset fund

## 8.2 R8取崩上位15基金で全体の95.717％をカバーできるため、materiality順のbottom-upが有効である

R8一般会計基金繰入32基金351.85764億円のうち、取崩額上位15基金は336.78819億円で95.717％を占める（出典：Stage6 `major_funds_cashflow_reconstruction.md`; 本調査Python確認）。全基金を同じ深さで分析するより、上位基金とハード制約を先に確認する方が意思決定に有効である。

代表例は次のとおりである。

| 基金・類型 | R8取崩（億円） | 公開情報から見えるduration | ALM上の扱い |
|---|---:|---|---|
| 財政基盤強化積立金 / fiscal buffer | 107.00 | shock・財源対策で機動利用 | 高流動性を優先 |
| 県債管理基金 / debt service | 37.56 | 償還scheduleに従う | 償還日へmaturity match |
| 職員退職手当基金 / scheduled liability | 37.00 | R8支出は確定、将来は公開情報不足 | 12mは短期、将来は保守的留保 |
| 地域医療介護総合確保基金 / rolling program | 34.21 | 翌年度pipeline形成時期は確認可能 | 12～24mをrolling更新 |
| 県立学校教育環境整備基金 / capital pipeline | 27.47 | R5～R10等の整備工程 | 1～5年へ満期対応 |
| 企業立地促進基金 / contingent program | 23.26 | 案件成立に依存 | committed/probable/contingent分離 |
| 県有施設更新整備基金 / capital pipeline | 22.43 | 新居浜警察署等でR11まで工程確認 | 1～5年へ満期対応 |
| デジタル社会形成推進基金 / program | 13.96 | 現行計画期間後は不確実 | 直近短期、先は保守的 |
| 森林環境保全基金 / annual program | 8.20 | 年度収支を追跡可能 | rolling 1y forecast |
| 災害に強い愛媛づくり基金 / contingent reserve | 7.85 | 災害時支出は外生的 | stress reserve |

## 8.3 非現金資産は投資可能額の分母から除く

美術品等取得基金30億円はR6末で美術品等約28.44億円、現金約1.56億円、医師確保奨学基金2.5億円も貸付金約0.91億円を含む。「三浦保」愛基金は寄附株式100万株を原資とする。これらを基金総額のまま「債券化可能資金」に含めると過大推計になる（出典：`EHIME-SETTLEMENT-R6`, `EHIME-MIURA-FUND`）。

## 8.4 判断：基金別ALM台帳の起点はcash balanceである

基金別コア投資可能額は次式で確認する。

`Core investable_i = cash balance_i - statutory/policy floor_i - approved 12m withdrawals_i - committed 1-3y pipeline_i - stress reserve_i - revolving/non-cash requirements_i`

この式は各控除項目を機械的に全基金へ入れるものではない。基金類型によって、何をfloor・pipeline・stressとみなすかを変える。R7末/R8期首の基金別cash balanceが公表された時点で、この式を主要15基金から適用し、top-downシナリオと突合する。

---

# 第9章　必要流動性は「金額 × 時間 × 不確実性」で測り、固定現金比率では管理しない

## 9.1 金額：R3～R6の16期間では最大968.01億円、P90 841.26億円であった

基金繰替は、公開情報から愛媛県のTreasury liquidity needを測る最も直接的なproxyの一つである。R3～R6の16期間の繰替額は次の分布となる（出典：`EHIME-FS-R3`～`EHIME-FS-R6`; `ehime_fund_substitution_period_totals.csv`; 本調査Python計算）。

| 指標 | 億円 |
|---|---:|
| 最小 | 203.51 |
| 第1四分位 | 461.87 |
| 平均 | 624.39 |
| 中央値 | 659.18 |
| P75 | 765.91 |
| P90 | 841.26 |
| P95 | 874.10 |
| 最大 | 968.01 |

季節平均は4～5月775.72億円、夏期325.31億円、秋期614.24億円、年度末782.29億円である。平均だけでは年度初め・年度末の高需要を過小評価し、最大だけでは平常時の流動性を過大保有する可能性がある。したがって、minimum liquidityは単一統計量ではなく、通常時・高需要時・stress時を分けて設計する。

![基金繰替は夏期に低下する一方、年度初め・年度末に高まり、単一の年間現金残高では捉えにくい](../charts/fig3_fund_substitution_seasonality.svg)

## 9.2 時間：R3～R7で4・5月借入→8月返済→8・11月再借入→年度末返済の循環が反復した

Stage6で愛媛県「財政事情」を確認したところ、R3～R7について、基金からの借入は概ね①4月・5月に実施、②8月までに返済、③8月・11月に再借入、④年度末までに返済、という時間構造を持つ。R7でも同じパターンが継続している（出典：Stage6 `finance_affairs_cashflow_findings.md`）。

この事実は二つの意味を持つ。第一に、基金は年度内Treasury liquidityとして実際に使われているため、長期運用額を決める際に基金繰替を無視できない。第二に、ピーク968.01億円を365日すべて即時現金で保持する必要性までは示していない。支払時期までに確実に満期が来る短期資産で一部を覆える可能性がある。

ただし「財政事情」は借入・返済月を示すが、日次・週次残高を完全には復元できない。したがって、過去データから13週forecastそのものを作ったと誤認せず、今後実務で13週予測を構築するためのseasonality evidenceとして使う。

## 9.3 不確実性：政策buffer・災害・財源不足・施設更新を単純合算しない

県財政運営基本方針は財源対策用基金400億円規模の安定確保を目標とする。また、西日本豪雨183億円、H16～18地方交付税減少407億円、R6～R8の機械的財源不足見込み333億円、県有施設更新費平均約180億円／年等が公表されている（出典：`EHIME-POLICY-2023`）。

これらは同じ種類のliabilityではない。

- **400億円**：政策上の財政buffer。
- **183億円・407億円**：stress testの規模感。
- **333億円**：短中期の財源圧力。
- **180億円／年**：予定されたcapital need。

これらを400億円に足し上げて「必要現金」とすると二重計上になり得る。適切なのは、400億円相当について必要時点までの流動化可能性を確認し、別途183億円・407億円規模でstress testし、予定支出は1～5年maturityへ織り込むことである。

## 9.4 Liquidity architecture：cash / bondsの二択をやめ、5層で管理する

| Layer | 想定期間 | 主な役割 | 主な管理方法 |
|---|---|---|---|
| immediate cash | 即時～数週 | 日々の支払、forecast error、急変 | 13週forecast、minimum cash |
| near-cash | 数週～数か月 | 予定支払・季節需要 | 短期預金等、満期分散 |
| <=1y maturity | 年度内 | 4・5月、8月、11月、年度末等の予測可能需要 | 支払日より前に満期設定 |
| 1–3y | 中期 | 退職、確度の高い事業pipeline等 | fund-level maturity matching |
| 3y+ core | 中長期 | 使用予定の低い残余 | ladder、issuer分散、MTM |

重要なのは、1年以内債を「長期投資」とみなさず、流動性管理の一部として位置付けることである。途中売却に依存せず、必要日前に満期が来る限り、現金を過剰に保有することなくliquidityを確保できる。

## 9.5 外部best practiceも「固定比率」よりcash-flow起点を支持する

OECDはcash bufferに単一の最適値はなく、forecast、market access、risk tolerance、governanceに依存すると整理する。IMFはcash-flow uncertaintyとfunding riskをcostとのtrade-offでbuffer設計することを推奨し、World Bankはforecastとtarget cash balanceを統合する。GFOAはrolling 12か月forecastを基本とし、複雑な政府では週次・日次まで細分化し、actual-vs-forecastで更新することを推奨する（出典：`OECD-CASH`, `IMF-BUFFER`, `WB-CASH`, `GFOA-CASH`）。

これらは日本法・愛媛県規程ではないが、「先に必要流動性を測り、残余を投資する」という本報告書の設計原則を外部best practiceとして補強する。

## 9.6 Decision / Action：愛媛県に必要なのは現金比率ではなく13週・1年・3～5年のliquidity architectureである

管理職が決めるべき最初の数値は「債券比率」ではなく、①13週minimum cash、②12か月内に満期が必要な額、③1～3年pipeline、④3～5年pipeline、⑤stress bufferである。R3～R7の季節性は設計の初期値を与えるが、実務導入後はforecast errorをbacktestし、minimum liquidityを毎年度更新する。

---

# 第10章　債券運用可能額は435.32億円を中心に検討できるが、bottom-up確認前のpolicy envelopeである

## 10.1 三つのケースは「適正比率」ではなく、流動性をどこまで厚く持つかという政策選択である

R6基金総額1,302.27675億円を共通分母として、基金繰替分布とstressを用いた三つのpolicy envelopeを置く。

| ケース | 即時現金 | near-cash | <=1y債 | 1–3y債 | 3–5y債 | 5y+債 | 債券合計 | 債券比率 | <=1y流動性による最大繰替coverage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 保守 | 968.01 | 183.00 | 0.00 | 90.76 | 45.38 | 15.13 | 151.27 | 11.6% | 118.9% |
| 標準 | 765.91 | 101.05 | 101.05 | 133.71 | 116.99 | 83.57 | 435.32 | 33.4% | 100.0% |
| 積極 | 659.18 | 68.39 | 205.18 | 110.86 | 129.33 | 129.33 | 574.70 | 44.1% | 96.4% |

出典：`ehime_liquidity_bond_scenarios.csv`; 本調査Python再計算。coverageは即時現金＋near-cash＋1年以内債を最大968.01億円で除したもの。

![三つのケースは収益性の優劣ではなく、流動性をどこまで厚く残すかという政策選択である](../charts/fig7_liquidity_three_cases.svg)

## 10.2 Standard 435.32億円のロジック：P75近傍を即時現金に置き、最大までの差を短期資産で埋める

標準ケースの即時現金765.91億円は16期間分布のP75に相当する。通常より高い需要まで即時現金で対応し、P75から最大968.01億円までの約202.10億円をnear-cash 101.05億円と1年以内満期債101.05億円へ二分する。これにより、最大実績を1年以内の流動性資産で100％coverしながら、435.32億円を中長期を含む債券へ振り向ける余地を置く。

この分割自体は統計的最適化の結果ではない。**安全性・流動性を先に確保し、その外側を投資可能域とする管理原則を数値化した中心ケース**である。

## 10.3 なぜ保守151.27億円ではないのか — 情報・制度が未整備なら合理的だが、流動性の過剰保有コストが大きい

保守ケースは過去最大968.01億円を即時現金、さらに西日本豪雨183億円相当をnear-cashとして同時に確保する。cash-flow forecastが未整備、現行eligible assets・年限limitが不明、基金別pipelineが読めない、pilot運用体制がない場合には、この厚いliquidityは合理的である。

一方、通常時でも1,151.01億円をcash / near-cashとして保持する設計は、金利正常化下では期間対価を放棄する可能性が高い。Stage7の市場参考値でも、2026年8月の1年大口定期0.447％と約1年T-Bill1.4332％には98.62bpの差があった。これは実現可能収益ではないが、流動性を過剰保有する機会費用が無視できないことを示す。

したがって保守ケースは「安全だから常に望ましい」のではなく、**Data Ready / Policy Readyになるまでの移行ケース**として位置付ける。

## 10.4 なぜ積極574.70億円ではないのか — 過去最大を完全coverせず、forecast能力への依存が高まる

積極ケースは即時現金を中央値659.18億円に置き、短期債205.18億円を活用して1年以内流動性を932.76億円とする。最大968.01億円に対するcoverageは96.4％であり、残差約35.26億円は、他の歳計現金、短期調達、予測精度等に依存する。

したがって、13週forecastが十分にbacktestされていない段階で積極ケースを採用すると、流動性不足時の途中売却又は別途資金調達を招く可能性がある。積極ケースは、forecast errorが小さく、基金別1～5年pipelineとmaturity matchingが定着し、現行policyで短期・中期債を十分利用できることが確認された後のscale-up optionである。

## 10.5 Bottom-up validation：基金別cash balanceから積み上げて初めて「実行可能額」になる

基金別には次式を適用する。

`Core investable_i = cash balance_i - statutory/policy floor_i - approved 12m withdrawals_i - committed 1-3y pipeline_i - stress reserve_i - revolving/non-cash requirements_i`

Stage6で上位15基金のliability classと主要な支出horizonまでは把握した。しかしR7末/R8期首の基金別cash balanceは、2026年9月16日時点で詳細決算の公表を確認できない。したがって、435.32億円を「現時点で購入できる金額」とは書かない。

## 10.6 Standard caseを棄却・修正すべき条件を先に定める

次のいずれかが確認された場合、435.32億円を下方又は上方修正する。

- R7末/R8期首の基金別cash balanceがR6総額ベースの想定より大幅に少ない。
- 主要基金の1～3年committed pipelineが想定以上に大きい。
- 財源対策用基金400億円について、より高い即時流動性を政策上求める必要がある。
- 13週forecastの誤差が大きく、P75をminimum cashとする設計が不安定。
- 現行公金管理方針で想定商品・年限が利用できない。
- 公開後の実保有債券が既に相当額あり、新規購入余地が小さい。
- 逆に、基金別cash balanceと3～5年pipeline確認後、長期使用予定のない残余が435.32億円を上回る。

モデルに棄却条件を持たせることで、シナリオを固定目標ではなく更新可能なdecision toolにする。

## 10.7 Decision / Action：当面の管理上限はstandard caseを中心に置き、実行額はGate 1～3を通過した基金だけを積み上げる

現段階では、435.32億円を中心ケースとしてportfolio architectureと収益・リスクを検討することは合理的である。ただし実行時は、基金別bottom-upで投資可能と確認できた額だけを積み上げ、合計がstandard envelopeを超えないよう管理する。R7詳細決算公表後、主要15基金から順に再計算する。

---

# 第11章　最大繰替を1年以内流動性で覆ったうえで、残余を満期分散すれば途中売却リスクを抑えられる

> **本章は愛媛県の現在の実際の運用状況を示すものではない。公開資料だけから構築したtarget portfolio architectureである。現行公金管理方針上のeligible assets・maturity・issuer limitを確認してから実装する。**

## 11.1 6つのbucketは商品分類ではなくliabilityへの対応表である

標準ケースの1,302.28億円を次の6層へ分ける。

| Bucket | 金額（億円） | liability-side rationale |
|---|---:|---|
| immediate cash | 765.91 | P75相当までの通常・高需要、forecast error |
| near-cash | 101.05 | P75超の数週～数か月需要 |
| <=1y maturity | 101.05 | 最大繰替までの差を満期対応 |
| 1–3y | 133.71 | 退職、財源圧力、確度の高いprogram pipeline |
| 3–5y | 116.99 | 学校・施設更新等のcapital pipeline |
| 5y+ | 83.57 | 使用予定が低く、満期まで保有可能なcore |

この構造の中心は「435.32億円を債券で持つこと」ではなく、**最初の968.01億円を1年以内に現金化できる状態にすること**である。

## 11.2 初期ladderはfront-loadedとし、均等配分より短中期へ厚く置く

標準ケースのモデル満期は次のとおりである（出典：`ehime_model_ladder_standard_case.csv`）。

| 満期 | モデル額（億円） |
|---|---:|
| <=1年 | 101.05 |
| 2年 | 66.85 |
| 3年 | 66.85 |
| 4年 | 58.50 |
| 5年 | 58.50 |
| 6年 | 16.71 |
| 7年 | 16.71 |
| 8年 | 16.71 |
| 9年 | 16.71 |
| 10年 | 16.71 |
| **合計** | **435.32** |

![最大繰替を1年以内流動性で覆い、中長期資金を年次分散すれば、特定年度の途中売却リスクを抑制できる](../charts/fig11_standard_case_maturity_ladder.svg)

これはequal ladderではなく、短中期へ厚いfront-loaded ladderである。理由は、愛媛県では3～5年までの基金事業pipelineが存在し、R7末cash balanceも未確定だからである。将来、使用予定の低いcore資金がbottom-upで確認されれば、5～10年部分を厚くする余地がある。

## 11.3 1年以内101.05億円は「1年満期1本」ではなく、季節需要に合わせて月・四半期へ分散する

R3～R7の資金繰りは4・5月、8月、11月、年度末に節目がある。したがって1年以内bucketは、単一満期へ集中させず、支払需要日前に複数回償還されるよう設計する。具体的配分は13週・12か月forecast完成後に決める。

この設計により、短期債は収益目的だけでなくliquidity instrumentとなる。途中売却を前提にせず、必要日前の満期償還でcashを作る。

## 11.4 Peer comparison：愛媛モデルは東京・熊本・兵庫の考え方を組み合わせるが、年限・上限は移植しない

- **東京**：短期<=2年、中期2～5年、長期5～10年を基金目的・取崩予定に対応させる複合ラダー。愛媛のbucket designに最も近い。
- **熊本**：21年以内、定額ラダー、原則満期保有、債券購入総額上限1,000億円。policy architectureの明文化が参考になる。
- **兵庫**：歳計現金への繰替を優先しつつ2～30年へ満期分散。Treasury liquidityと中長期運用の共存例である。

愛媛県は東京の10年、熊本の21年、兵庫の30年を推奨年限として採用しない。採用するのは、**fund purpose → maturity bucket → ladder → monitoring**の順序である。

## 11.5 Product allocation：国債60％等はillustrativeであり、security typeよりmaturity matchを優先する

既存モデルでは債券435.32億円の例として国債60％、地方債20％、政府保証債・JFM債・財投機関債等20％を置いていた。これは最適配分ではなく、国債をcoreとして発行体・商品を分散する説明用モデルである。

実務では次の順で判断する。

1. 支払予定から年限を決める。
2. 現行公金管理方針上のeligible assetsを確認する。
3. 同年限の商品間で信用力・流動性・yield・取引条件を比較する。
4. issuer / category concentrationを確認する。
5. 購入後のmark-to-marketと満期管理が可能か確認する。

この順序なら、利回りが高い商品があってもliabilityに合わなければ採用しない。

## 11.6 10年超は初期対象外とし、5年超からdocumented liability matchを要求する

GFOAのmarket-risk guidanceは、長期資産についてspecific cash requirementとのmatchを重視する。愛媛県では基金繰替規模が大きく、主要基金pipelineの公開情報も3～5年程度が中心であるため、初期設計では10年以内とする。5年超についても、使用予定が低いことを基金別台帳で文書化できる資金に限定する（出典：`GFOA-MARKET`）。

10年超を将来検討する条件は、①R7以降のfund-level cash history、②長期liabilityの安定、③mark-to-market、④governance、⑤forced-sale実績の蓄積である。

## 11.7 Execution：金利予測より時間分散を優先する

新規投資を一時点へ集中させず、rolling purchase、staggered execution、maturity reinvestmentで購入時期を分散する。金利が上昇すれば順次高い水準へ再投資でき、低下すれば既保有債の利回りを一定期間維持できる。目的は相場を当てることではなく、**予想が外れても支払能力と運用継続性を維持すること**である。

---

# 第12章　追加収益は「債券利回り」ではなく、同程度の拘束期間を持つ代替資産との差で評価する

## 12.1 Value caseの基本式

追加収益は次式で測る。

`Incremental income = Additional bond allocation × (bond yield - alternative deposit yield)`

預金にも収益があるため、債券利回り全体を増収とするのは誤りである。また、10年国債と1年定期預金の差を「債券の追加収益」とするのも年限が違うため不適切である。

## 12.2 同年限に近い1年referenceでは98.62bpの市場差が観察されたが、実現可能収益ではない

2026年8月の日本銀行「1,000万円以上・1年定期」平均金利0.447％に対し、2026年8月19日の約1年T-Billの募入平均利回りは1.4332％であり、near-date reference差は98.62bpである（出典：`BOJ-IR02`, `MOF-TBILL-1401`; 本調査Python計算）。

ただし、預金側は店頭表示平均で自治体入札金利ではなく、国債側はprimary auction yieldである。実行時には、同日の実際の預金引合いと購入候補債券yieldを比較する必要がある。したがって98.62bpをstandard caseの収益前提には使わない。

## 12.3 2・5・10・20年の国債利回りはterm-extension referenceであり、same-tenor spreadではない

直近primary auctionの参考値は、2年1.708％、5年2.239％、10年2.995％、20年3.856％である。一方、同じBOJ標準系列で2年・3年・5年の大口定期平均を確認できなかった。このため、1年定期0.447％との差126.10bp、179.20bp、254.80bp、340.90bpは「期間延長参考差」であり、同年限比較とは記載しない（出典：`MOF-JGB2-488`, `MOF-JGB5-187`, `MOF-JGB10-383`, `MOF-JGB20-197`; Stage7 market analysis）。

この制約は結論を弱めるものではない。むしろ、長期利回りが高いから長期化するのではなく、cash-flowで年限を決めた後に同年限の代替資産を比較するという原則を明確にする。

## 12.4 Sensitivity：standard caseでは10bpのspreadでも年間約4,353万円、50bpなら約2.18億円の差となる

| ケース | 債券額（億円） | +0.1pt | +0.2pt | +0.3pt | +0.5pt |
|---|---:|---:|---:|---:|---:|
| 保守 | 151.27 | 15.1百万円 | 30.3百万円 | 45.4百万円 | 75.6百万円 |
| 標準 | 435.32 | 43.5百万円 | 87.1百万円 | 130.6百万円 | 217.7百万円 |
| 積極 | 574.70 | 57.5百万円 | 114.9百万円 | 172.4百万円 | 287.4百万円 |

![追加収益は絶対利回りではなく代替預金とのspreadに比例する](../charts/fig9_income_sensitivity.svg)

この表は将来収益予測ではなく、spread sensitivityである。実行判断では実際の入札・購入条件を使う。

## 12.5 Value beyond interest：cash visibilityとgovernance改善自体が運用価値を持つ

ALM導入の便益は利息だけではない。基金別cash-flowの可視化、満期日による支払予定の予見性、idle cashの把握、forced sale回避、投資判断の記録、引継ぎ可能性、監査可能性が改善する。これらは金額換算せず、operating modelの改善としてKPI化する。

---

# 第13章　リスク管理は「リスク名の列挙」ではなく、Exposure → Metric → Trigger → Responseまで設計する

## 13.1 最重要リスクは、市場価格そのものより「必要時に売らざるを得ない」ことである

固定利付債券は市場金利上昇時に時価が下落する。信用力の高い債券を満期保有すれば額面償還が期待できても、資金需要が満期より先に来れば途中売却が必要となり、評価損が実現損になる可能性がある。

したがって「満期保有だから含み損は関係ない」は不正確である。正しくは、**満期まで保有できる資金だけを債券へ配分し、別途十分な流動性を確保している限り、時価下落を実現損へ変える必要を抑えられる**ということである。

GFOAは全securityのmarket valueを少なくとも四半期ごとに信頼できるsourceで把握し、oversight bodyへ報告することを推奨している。これは日本の会計処理を規定するものではないが、リスク管理上のmark-to-market benchmarkとして有用である（出典：`GFOA-MTM`）。

## 13.2 Risk-control matrix

| Risk | Exposure | Candidate metric | Trigger / review point | Response |
|---|---|---|---|---|
| Liquidity | 支払前に満期が来ない | 13-week coverage、minimum liquidity compliance | coverage低下、stress不足 | 新規長期購入停止、短期化、cash積増し |
| Forecast | 予測と実績が乖離 | weekly/monthly forecast error | 誤差拡大、peak miss | buffer再推計、forecast driver見直し |
| Interest-rate | 金利上昇で時価下落 | WAM、duration proxy、maturity concentration | 長期bucket集中 | 新規購入を短中期へshift |
| Market value | 未実現損益の拡大 | book vs market、unrealized P/L | MTM変動、説明必要性 | 原因分析、liquidity再確認、不要な売却回避 |
| Reinvestment | 特定年度に大量償還 | annual maturity share、largest maturity-year share | 満期集中 | ladder再配分、購入時期分散 |
| Credit | 発行体信用悪化 | issuer exposure、eligible-list compliance | 格付・信用条件変化 | 新規停止、policyに従う対応 |
| Concentration | 発行体・商品・年限偏重 | max issuer/category/bucket share | 上限接近 | 新規分散、購入見送り |
| Forced sale | 資金不足で満期前売却 | pre-maturity sale count、実現損 | 1件でも原因分析 | forecast・bucket再設計 |
| Operational | trade/settlement/reconciliation不備 | exception count、未照合件数 | 未処理・例外増加 | segregation、手順改訂 |
| Governance | review・承認が形骸化 | review timeliness、breach closure time | 遅延・未解消 | escalation、policy review |

数値limitは現行愛媛県規程と実cash-flowを確認するまで設定しない。

## 13.3 Liquidity risk：最大968.01億円とP90 841.26億円を別のstressとして使う

最大値だけを恒常bufferにすると過剰流動性になりやすく、平均だけではtail riskを過小評価する。実務上は、base caseを13週forecast、high-demand caseをP75/P90、severe caseを過去最大・災害等とし、各caseで満期前売却なしに対応できるかを確認する。

## 13.4 Interest-rate / reinvestment risk：長期化と短期化の双方にリスクがある

短期だけに集中すれば金利低下時の再投資リスクが高まり、長期に集中すれば金利上昇時に低利回り資産が長く残り、時価変動も大きくなる。ladderは両者を分散する。WAMやduration proxyは収益最大化指標ではなく、portfolioの金利感応度を可視化するcontrolとして使う。

## 13.5 Decision / Action：risk limitは購入前に決め、違反時のactionまで年度計画へ書く

投資可能商品、最長年限、maturity bucket、issuer/category、例外売却、mark-to-market、breach escalationを年度運用計画に明記する。limitは購入後の評価基準ではなく、購入前のdecision ruleである。

---

# 第14章　運用高度化の中核は債券比率ではなく、policy・forecast・execution・monitoringを分離したgovernanceである

## 14.1 現行愛媛県「公金管理方針」は存在を確認できるが、最新本文の具体limitは公開確認できない

R8当初予算編成方針は、基金・歳計現金について「公金管理方針」を踏まえ一層効率的な運用に努めることを求めているため、方針が現行行政実務の参照枠組みであることは確認できる。一方、2026年9月16日時点の公開検索では、現行最新版本文を独立文書として確認できなかった（出典：Stage6 `public_funds_policy_public_status.md`）。

H23包括外部監査に引用された当時の方針では、安全性、流動性、効率性、資金計画、元本安全性、原則満期保有、やむを得ない場合の中途解約・売却等が確認できる。ただし、本報告書はこれを現行の具体的年限・商品・権限limitとして代用しない。

## 14.2 Target operating modelは5層で設計する

1. **Policy layer**：目的、安全性・流動性・効率性の優先順位、eligible assets、authority、custody、reporting、exception。
2. **Cash visibility layer**：13週forecast、12か月forecast、actual-vs-forecast。
3. **Fund-level ALM layer**：cash/non-cash、floor、12m withdrawal、1～5y pipeline、stress、sunset。
4. **Execution layer**：maturity bucket、issuer/category、purchase timing、ladder、settlement。
5. **Monitoring layer**：liquidity compliance、forecast error、WAM/duration proxy、MTM、exceptions、income uplift。

GFOAはwritten investment policyをgoverning bodyが採択し少なくとも年1回reviewすること、yieldだけでなくsafety・liquidity・returnを少なくとも四半期で評価することを推奨している。これは外部benchmarkであり、日本法や愛媛県現行ルールそのものではない（出典：`GFOA-INV-POLICY`, `GFOA-PERF`）。

## 14.3 モデルRACI：意思決定・執行・牽制を同一人に集中させない

実在部署の現行権限を推定せず、roleとして次の分離を提案する。

| Role | 主な責任 | RACIイメージ |
|---|---|---|
| finance / fiscal planning | 中期財政・基金用途・stress前提 | Consulted / Accountable on fiscal assumptions |
| accounting / treasury | cash forecast、execution、settlement、maturity管理 | Responsible |
| fund owner | 12m withdrawal、1～5y pipeline、事業変更 | Responsible for liability input |
| governance body | policy、limits、例外、四半期review | Accountable |
| independent confirmation / audit function | reconciliation、policy compliance、記録 | Consulted / assurance |

実装前に現行決裁規程へマッピングし、役割の重複・空白を確認する。

## 14.4 Management forum：月次・四半期・年次で扱う論点を分ける

### Monthly

- 13週・12か月forecast更新
- 直近満期・取崩・国庫入金・起債等の確認
- minimum liquidityとmaturity calendar確認
- forecast error更新

### Quarterly

- safety / liquidity / returnのperformance review
- mark-to-market、unrealized gain/loss
- maturity / issuer / category concentration
- forced sale、exception、breachの有無
- 補正予算・事業変更によるALM再計算

### Annual

- 公金管理方針・年度運用計画review
- eligible assets・maturity・issuer limits
- stress scenario
- strategic bucket allocation
- 次年度pilot / scale decision

## 14.5 情報開示：収益だけでなく安全性・流動性を説明できる形式にする

最低限、基金平均残高、預金・債券平均残高、運用収入、実効利回り、主要商品区分、満期構成又は平均年限、market value情報、途中売却の有無を年度で整理する。公開範囲は現行制度に従うが、内部reviewでは同じformatを継続する。これにより、人事異動があっても「なぜその年限・商品を選んだか」を再現できる。

---

# 第15章　実施は5つのGateで進め、最初の90日は購入額ではなくデータ・流動性モデルを完成させる

## Gate 1 — Data Ready：基金別cashとliabilityを同じ台帳で見られる状態にする

必須項目は、fund cash、non-cash、法定・政策floor、12か月withdrawal、1～3年pipeline、3～5年pipeline、stress/contingency、sunset、現行投資制約である。Stage6で上位15基金の公表pipelineはかなり整理済みであり、R7詳細決算公表後にcash balanceを接続する。

**Gate通過条件**：主要基金について「何円を何年まで拘束可能か」の根拠を台帳で追跡できる。

## Gate 2 — Liquidity Model Validated：13週forecastを実績でbacktestする

13週forecastと12か月maturity calendarを運用し、actual-vs-forecast error、P90、過去最大968.01億円、政策buffer、災害stressを確認する。

**Gate通過条件**：minimum liquidityを説明でき、stress時も途中売却に依存しない見通しがある。

## Gate 3 — Policy Ready：商品・年限・issuer・例外・reportingを購入前に承認する

現行公金管理方針最新版を確認し、必要なら年度運用計画で、eligible assets、最長年限、maturity bucket、issuer/category、purchase authority、custody、exception sale、MTM、reporting、breach escalationを明文化する。

**Gate通過条件**：誰が何を決め、どのlimitで止め、例外を誰が承認するかが明確である。

## Gate 4 — Pilot Ready：少額・短中期のladderで制度とデータを試す

初期pilotは、fund-level liabilityが明確で、満期まで保有可能性を説明できる資金から開始する。購入を複数時点へ分散し、短中期bucket中心にmonitoringする。

**Gate通過条件**：settlement、maturity、forecast、MTM、reportingが一巡し、重大なexceptionなしに運用できる。

## Gate 5 — Scale Decision：expand / maintain / reduceをKPIで判断する

評価するのは、

- liquidity compliance
- 13-week / monthly forecast error
- forced-sale count
- maturity / issuer concentration
- incremental income vs comparable deposit
- operational burden / exception count
- policy review timeliness

である。利回りだけで拡大を決めない。

## 最初の90日deliverables

| 時期 | Deliverable | 目的 |
|---|---|---|
| 0–30日 | 主要15基金ALM台帳、現行policy gap list、maturity calendar | Data Ready |
| 31–60日 | 13週forecast、12か月forecast、stress test、forecast error定義 | Liquidity Model |
| 61–90日 | 年度運用計画案、risk-control matrix、pilot候補、reporting template | Policy / Pilot Ready |

R7詳細決算が期間中に公表された場合はcash balanceを即時反映し、standard 435.32億円を再計算する。

## 次年度の意思決定

次年度は、pilot結果とR7/R8実績を用い、①standard envelopeを維持、②conservativeへ縮小、③条件付きでactive側へ拡大、の三択を判断する。固定的な債券購入額を毎年踏襲しない。

---

# 結論

## 1. 愛媛県に債券運用余地はあるか

**ある可能性は高いが、R6基金総額と低い有価証券比率だけでは確定できない。** 基金繰替に強い季節性があり、ピーク968.01億円を365日すべて即時現金で持つ必要性は確認できないため、支払時期に満期を合わせれば中長期運用へ配分できる残余は存在し得る。一方、基金は年度内Treasury liquidityとして実際に使われているため、他県比率の単純模倣は不適切である。

## 2. どの程度か

公開情報だけからのtop-down policy envelopeは、保守151.27億円、標準435.32億円、積極574.70億円である。**標準435.32億円を中心ケースとして検討することは合理的だが、推奨購入額・最適額ではない。** 最大繰替968.01億円を1年以内流動性資産で100％coverする設計だからである。

## 3. 何を先に整備すべきか

最優先は13週・12か月・3～5年のcash-flow forecast、基金別ALM台帳、現行公金管理方針上のeligible assets・maturity・issuer・exception rule確認である。これらを整備する前に長期債購入額を固定しない。

## 4. 何をやってはいけないか

- 高債券比率県の比率を目標にする。
- 基金総額をそのまま投資可能現金とみなす。
- 10年国債と1年預金の利回り差を追加収益とする。
- 満期保有を理由にmark-to-market・流動性リスクを無視する。
- 未公表の愛媛県現行運用・limitを推測する。
- forecast能力がない段階でactive caseへ一括移行する。

## 5. どの条件なら拡大できるか

R7末/R8期首cash balanceと主要基金1～5年pipelineが確認され、13週forecastが安定し、現行policyとrisk limitsが整備され、pilotでforced sale・重大exceptionなく運用できた場合に限り、standardからactive側へのscale-upを検討する。

本報告書の基本原則は一文に集約される。

> **債券比率を先に決めるのではなく、必要流動性を先に測り、その残余だけを、資金需要時期に一致する満期ラダーへ配分する。**

---

# 付録

## 付録A　R7直接比較5県

| 県 | 現預金比率 | 債券比率 | 全体利回り | データ基準 |
|---|---:|---:|---:|---|
| 福島 | 74.9% | 25.1% | 0.291% | 基金年間平均 |
| 埼玉 | 35.0% | 65.0% | 0.609% | 基金年間平均 |
| 千葉 | 39.9% | 60.1% | 0.482% | 基金年間平均 |
| 静岡 | 38.3% | 61.7% | 0.535% | 基金年間平均 |
| 鳥取 | 84.8% | 15.2% | 0.520% | 基金年間平均 |

5県単純平均債券比率45.4％は全国平均ではなく、開示可能な直接比較サンプルの参考値である。

## 付録B　愛媛県基金繰替16期間の分布

| 指標 | 億円 |
|---|---:|
| 最小 | 203.51 |
| 第1四分位 | 461.87 |
| 平均 | 624.39 |
| 中央値 | 659.18 |
| P75 | 765.91 |
| P90 | 841.26 |
| P95 | 874.10 |
| 最大 | 968.01 |

## 付録C　三つのpolicy envelope

| ケース | 債券額（億円） | 債券比率 | <=1y流動性（億円） | 最大968.01億円coverage |
|---|---:|---:|---:|---:|
| 保守 | 151.27 | 11.6% | 1,151.01 | 118.9% |
| 標準 | 435.32 | 33.4% | 968.01 | 100.0% |
| 積極 | 574.70 | 44.1% | 932.76 | 96.4% |

## 付録D　Bottom-up ALM式

`Core investable_i = cash balance_i - statutory/policy floor_i - approved 12m withdrawals_i - committed 1-3y pipeline_i - stress reserve_i - revolving/non-cash requirements_i`

マイナスとなる基金は中長期core運用の対象外とする。非現金資産を含む基金は必ずcash部分へ補正する。

## 付録E　候補KPI

| Objective | Candidate KPI |
|---|---|
| Liquidity | 13-week coverage、minimum liquidity compliance |
| Forecast | weekly/monthly forecast error |
| Interest-rate | WAM、duration proxy、maturity concentration |
| Reinvestment | annual maturity share |
| Credit / concentration | issuer/category exposure |
| Market value | book vs market、unrealized gain/loss |
| Forced sale | pre-maturity sale count、forced-sale realized loss |
| Operational | exception count、unreconciled items |
| Governance | policy review timeliness、breach closure time |
| Value | comparable-deposit対比incremental income |

## 付録F　主な公開情報上の未解消事項

1. R7愛媛県歳入歳出決算書、決算附属書、財産に関する調書等の詳細決算パッケージ。
2. 現行最新版の愛媛県公金管理方針本文と具体的eligible assets / maturity / issuer / authority limits。
3. 1年超について、自治体運用に近い同定義の預金金利と国債利回りを時系列で完全に同年限比較できる公的標準系列。
4. 一部基金のR9以降支出額は資料不足ではなく政策・災害・企業立地等の性質上未確定であり、committed / probable / contingentで管理する必要がある。

---

# 出典・参考資料

以下は本報告書の主要な検証に用いた公表資料である。詳細なsource dictionary、抽出データ、QAは `stage3/`～`stage7/` に保存している。最終確認日は原則2026年9月16日。

## 国・公的機関

- `STAT-R6-MIC` 総務省・e-Stat「地方財政状況調査（都道府県分）基金の状況等」令和6年度末。https://www.e-stat.go.jp/stat-search/files?stat_infid=000040374310
- `LAW-LOCAL-AUTONOMY` e-Gov「地方自治法」。https://elaws.e-gov.go.jp/document?lawid=322AC0000000067
- `DISASTER-RELIEF-ACT` e-Gov「災害救助法」。https://laws.e-gov.go.jp/law/322AC0000000118
- `BOJ-FFA-METHOD` 日本銀行「資金循環統計の作成方法」。https://www.boj.or.jp/statistics/outline/exp/data/exsj02.pdf
- `BOJ-IR02` 日本銀行「預金種類別店頭表示金利の平均年利率等」。https://www.stat-search.boj.or.jp/ssi/mtshtml/ir02_m_1.html
- `MOF-JGB-RATE` 財務省「国債金利情報」。https://www.mof.go.jp/jgbs/reference/interest_rate/index.htm
- `MOF-TBILL-1401` 財務省「国庫短期証券第1401回入札結果」2026年8月19日。https://www.mof.go.jp/jgbs/auction/calendar/tbill/tbill_nyusatsu/resul20260819.htm
- `MOF-JGB2-488` 財務省「2年利付国債第488回入札結果」2026年8月28日。https://www.mof.go.jp/jgbs/auction/calendar/nyusatsu/resul20260828.htm
- `MOF-JGB5-187` 財務省「5年利付国債第187回入札結果」2026年9月8日。https://www.mof.go.jp/jgbs/auction/calendar/nyusatsu/resul20260908.htm
- `MOF-JGB10-383` 財務省「10年利付国債第383回入札結果」2026年9月1日。https://www.mof.go.jp/jgbs/auction/calendar/nyusatsu/resul20260901.htm
- `MOF-JGB20-197` 財務省「20年利付国債第197回入札結果」2026年9月15日。https://www.mof.go.jp/jgbs/auction/calendar/nyusatsu/resul20260915.htm

## 愛媛県

- `EHIME-R6-FISCAL-COMP` 愛媛県「令和6年度都道府県財政比較分析表」。https://www.pref.ehime.jp/uploaded/attachment/176599.pdf
- `EHIME-FUND-R6` 愛媛県「財政状況資料集 令和6年度 基金残高経年分析」。https://www.pref.ehime.jp/uploaded/attachment/176608.pdf
- `EHIME-FS-R3`～`EHIME-FS-R6` 愛媛県「愛媛県の財務書類」各年度決算ベース。基金繰替amount dimensionに使用。
- 愛媛県「財政事情」R3～R7各翌年度5月公表。年度内基金繰替timing dimensionに使用。Index: https://www.pref.ehime.jp/page/8806.html
- `EHIME-POLICY-2023` 愛媛県「財政運営基本方針」等。財源対策用基金400億円規模、stress・中期財政制約に使用。
- `EHIME-BUDGET-R8-EXPLANATION` 愛媛県R8当初予算説明資料。基金取崩・主要事業に使用。
- 愛媛県R8当初予算編成方針。現行「公金管理方針」が参照されていることの確認。https://www.pref.ehime.jp/uploaded/attachment/163824.pdf
- 愛媛県平成23年度包括外部監査「基金の管理と運用について」。歴史的な公金管理方針の原則確認。https://www.pref.ehime.jp/uploaded/attachment/37467.pdf

## Peer自治体

- `SAITAMA-R7` 埼玉県「令和7年度第4四半期・公金の運用状況について」。https://www.pref.saitama.lg.jp/documents/9675/unyoujyokyo7-4.pdf
- `SAITAMA-MGMT` 埼玉県「公金の管理・運用について」。https://www.pref.saitama.lg.jp/documents/9675/koukinkanri-unyo.pdf
- `SHIZUOKA-R7` 静岡県「資金運用・令和7年度実績」。https://www.pref.shizuoka.jp/kensei/zaiseisuito/suito/1030351.html
- `KUMAMOTO-POLICY` 熊本県「熊本県公金管理に関する方針」。https://www.pref.kumamoto.jp/uploaded/attachment/270754.pdf
- `NIIGATA-POLICY` 新潟県「新潟県公金管理方針」。https://www.pref.niigata.lg.jp/sec/suitoukanri/1356775812913.html
- `NIIGATA-R7` 新潟県「令和7年度の公金運用状況」。https://www.pref.niigata.lg.jp/site/suitou/reiwa7nendokoukinunyoujyoukyou.html
- `KAGAWA-FISCAL-155` 香川県「財政事情 第155回」。https://www.pref.kagawa.lg.jp/documents/8155/155_all_zaiseijijyo155.pdf
- `TOKYO-R8-PLAN` 東京都「令和8年度公金管理計画」。https://www.metro.tokyo.lg.jp/information/press/2026/03/2026033034
- `TOKYO-R7-ACTUAL` 東京都「令和7年度公金管理実績」。https://www.metro.tokyo.lg.jp/information/press/2026/05/2026052909
- `HYOGO-R7R8` 兵庫県「令和7年度資金運用実績及び令和8年度資金運用計画」。https://web.pref.hyogo.lg.jp/kk21/documents/r8keikaku.pdf

## 国際機関・best practice

- `OECD-CASH` OECD, *Managing Government Cash: A Review of Practices in OECD Countries* (2025). https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/managing-government-cash_d47b35b7/7675eb58-en.pdf
- `IMF-BUFFER` IMF, *How to Set Up A Cash Buffer*. https://www.imf.org/en/Publications/Fiscal-Affairs-Department-How-To-Notes/Issues/2020/11/17/How-to-Set-Up-A-Cash-Buffer-A-Practical-Guide-to-Developing-and-Implementing-a-Cash-Buffer-49851
- `IMF-SURPLUS` IMF, *How to Develop a Framework for Investment of Temporary Government Cash Surpluses*. https://www.imf.org/en/Publications/Fiscal-Affairs-Department-How-To-Notes/Issues/2020/12/21/How-to-Develop-a-Framework-for-Investment-of-Temporary-Government-Cash-Surpluses-49954
- `WB-CASH` World Bank, *Forecasting and Targeting Government Cash Balances*. https://documents1.worldbank.org/curated/en/625511593411466514/pdf/Forecasting-and-Targeting-Government-Cash-Balances.pdf
- `GFOA-INV-POLICY` GFOA, *Investment Policy*. https://www.gfoa.org/materials/investment-policy
- `GFOA-PROGRAM` GFOA, *Investment Program for Public Funds*. https://www.gfoa.org/materials/investment-program-for-public-funds
- `GFOA-CASH` GFOA, *Using Cash Forecasts for Treasury and Operations Liquidity*. https://www.gfoa.org/materials/using-cash-forecasts-for-treasury-and-operations-liquidity
- `GFOA-PERF` GFOA, *Performance Measures for Government Investment Portfolio Objectives*. https://www.gfoa.org/materials/performance-measures-for-government-investment-portfolio-objectives
- `GFOA-MTM` GFOA, *Mark-to-Market Reporting for Public Investment Portfolios*. https://www.gfoa.org/materials/mark-to-market-reporting-for-public-investment-portfolios
- `GFOA-MARKET` GFOA, *Managing Market Risk in Investment Portfolios*. https://www.gfoa.org/materials/managing-market-risk-in-investment-portfolios
- `GFOA-DIVERSIFY` GFOA, *Diversifying the Investment Portfolio*. https://www.gfoa.org/materials/diversifying-the-investment-portfolio

---

**Canonical report status after Stage 8 rewrite:** Client-ready review対象。最終判定は `stage8/client_ready_rewrite/client_ready_final_review.md` に記録する。
