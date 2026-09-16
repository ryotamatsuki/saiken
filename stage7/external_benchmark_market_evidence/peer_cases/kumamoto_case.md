# 熊本県ケース — 明示的な年限上限・ラダー・購入総額上限

**基準時点:** 現行公金管理方針（令和6年4月24日改定） / 2026-09-16確認  
**位置づけ:** risk limitとportfolio ruleが最も具体的に公開されるケース

## Fact

熊本県の公金管理方針は、歳計現金、歳入歳出外現金、基金に属する現金を対象とする。預金は当座・普通・1年以内の定期性預金。債券は国債、地方債、政府保証債、地方公共団体金融機構債、財投機関債、国立大学法人債、高速道路会社債を対象とし、後三者は国債と同等以上の格付を1つ以上有することを条件とする。

債券の購入年限は21年以内、原則満期保有、定期的に一定額を購入するラダー型運用を基本とし、購入総額上限は1,000億円。預金解約又は債券売却は、資金保全が必要な場合又は総運用収益向上のために行える。会計管理者は毎年度、預金先・預金種類、債券商品・運用期間・購入予定額等を定めた運用計画を策定する。

公金運用実績の公表資料では、歳計現金等と基金を一体的に管理し、ラダー型を用いる運用体系が確認できる。

## Interpretation

熊本の特徴は「高い債券比率」ではなく、eligible assets、max maturity、hold-to-maturity、ladder、aggregate cap、exception sale、annual planが一つのpolicyに接続されている点にある。これはportfolio architectureとgovernanceを同時に設計している例である。

## Ehime implication

愛媛県の第11・13・14章では、熊本を「数値limitをそのまま採用する対象」ではなく、`対象商品→年限→購入上限→売却例外→年度計画`を一体で規定する制度設計のbenchmarkとして使える。愛媛で具体的な年限・上限を設定するには、13週・1～5年cash-flowと現行規程の確認が先行する。

## Limitation

21年及び1,000億円は熊本固有のpolicy limitであり、愛媛県へ直接移植できない。また公表実績の利回り・残高には歳計現金等を含むものがあり、基金単独のR7 allocationと同一視しない。

## Sources

- 熊本県「熊本県公金管理に関する方針」 https://www.pref.kumamoto.jp/uploaded/attachment/270754.pdf
- 熊本県「公金運用実績・公金管理方針」 https://www.pref.kumamoto.jp/soshiki/118/68486.html
- Existing structured data: `stage3/processed/management_features.csv`
