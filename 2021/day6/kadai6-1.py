#!/usr/bin/env python
# coding: utf-8
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# Read database.
df = pd.read_csv('csv/mydata2.csv', index_col=0)

# Categorize database
listCelery = list(['超嫌い', '嫌い', 'ふつう', '好き', '超好き'])
df['セロリ嗜好'] = pd.Categorical(df['セロリ嗜好'], categories=listCelery, ordered=True)
df['セロリ嗜好度値'] = df['セロリ嗜好'].cat.codes

# Print results
iqr25_lion = df[df['好きな動物'] == 'ライオン']['セロリ嗜好度値'].quantile(0.25)
iqr75_lion = df[df['好きな動物'] == 'ライオン']['セロリ嗜好度値'].quantile(0.75)
iqr25_nook = df[df['好きな動物'] == 'たぬき']['セロリ嗜好度値'].quantile(0.25)
iqr75_nook = df[df['好きな動物'] == 'たぬき']['セロリ嗜好度値'].quantile(0.75)

print('ライオン ')
print('  第 1 四分位数 ( 25% ) = ' + str(iqr25_lion))
print('  第 3 四分位数 ( 75% ) = ' + str(iqr75_lion))
print('たぬき ')
print('  第 1 四分位数 ( 25% ) = ' + str(iqr25_nook))
print('  第 3 四分位数 ( 75% ) = ' + str(iqr75_nook))
print()

if iqr25_lion < iqr25_nook and iqr25_nook < iqr75_lion:
  print('四分位範囲が重なっている。差があるとは言えない。')
elif iqr25_lion < iqr75_nook and iqr75_nook < iqr75_lion:
  print('四分位範囲が重なっている。差があるとは言えない。')
else:
  print('四分位範囲が重なっていない。差がある。')
