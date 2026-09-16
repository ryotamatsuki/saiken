# Consulting Report Benchmark Library

## 目的

本ディレクトリは、愛媛県の基金・公金・債券運用に関する調査レポートを、単に情報量の多い文書ではなく、クライアントの意思決定に直接使える **client-ready consulting report** に引き上げるための外部ベンチマークである。

現行canonicalレポート：

`stage4/reports/ehime_fund_bond_management_consulting_report_R7_R8.md`

Stage 5では、公開されている主要コンサルティングファームのレポート・調査記事・PDFを比較し、次の問いに答える。

1. 一流のコンサルティングレポートは、どのように問いを設定しているか。
2. Executive Summaryは何を、どの順序で示しているか。
3. データ・ベンチマーク・ケーススタディ・図表は、どのように主張を支えているか。
4. 事実の提示から解釈、示唆、提言、実装へどう接続しているか。
5. どの程度の留保・不確実性・反証を扱っているか。
6. 愛媛県レポートをclient-readyへ引き上げるため、どこを改稿すべきか。

## 収録物

- `benchmark_catalog.md`：公開ベンチマークの書誌・URL・利用目的・主要特徴
- `benchmark_case_notes.md`：各レポートの構造・文章・図表・分析の詳細観察
- `report_quality_framework.md`：100点満点の品質評価フレームとclient-ready gate
- `ehime_report_gap_assessment.md`：現行愛媛県レポートの初回Senior Manager Review
- `client_ready_review_checklist.md`：改稿・最終QAに使うチェックリスト

## 著作権・保存方針

公開されているPDFやWebレポートであっても、公開されていることと再配布可能であることは同義ではない。このため本ライブラリでは、原則として第三者レポートのPDF原本をGitHubへ複製しない。

保存するのは、原則として次の情報である。

- 公式配布元URL
- タイトル、発行主体、発行年月、ページ数・読了時間等の書誌情報
- 調査母集団、データ範囲、分析手法の要約
- レポート構造・図表・ストーリーラインの分析メモ
- 愛媛県レポートへ転用可能な編集・分析上の原則

原本を将来保存する場合は、Creative Commons等の再配布条件が明示されているかを個別確認する。

## Benchmark philosophy

本ベンチマークは「一流ファームの文体を模倣する」ためのものではない。公開thought leadershipと実際の有償クライアント納品物は異なるため、公開資料から学ぶのは主に以下である。

- 問いの切り方
- Executive Summaryの設計
- evidence-to-insightのつなぎ方
- exhibit-led communication
- benchmarkの使い方
- recommendationとimplementationへの落とし込み

一方、自治体レポートとして必要な出典透明性、制度・法令への整合、時点の厳密な区別、データ制約の明示、公金運用における安全性・流動性の優先順位は、コンサル資料以上に厳格に扱う。

## Stage 5の判定

現行レポートは、データ収集・論点設定・初期モデル設計の観点では十分な骨格を持つ。一方、各章における「事実 → 解釈 → 愛媛県への含意 → 意思決定」の展開、ケーススタディの深さ、モデル数値のdecision logic、実装・ガバナンスの具体性には補強余地がある。

したがってStage 5の目的は文章量の機械的増加ではなく、**重要論点について分析の深度を上げ、読み手の判断を前に進めること**とする。
