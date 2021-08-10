#!/usr/bin/env python
# coding: utf-8
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# CSVファイルを読み込み
df = pd.read_csv('csv/mydata2.csv', index_col=0)

# 所持金額を計算(1:増加前、2:増加後)
df['所持金額1'] = df['所持金の増加（差）'] / (df['所持金の増加（比）'] - 1)
df['所持金額1'] = df['所持金額1'].round().astype('int')
df['所持金額2'] = df['所持金額1'] + df['所持金の増加（差）']

# 所持金額の平均を計算
means_lion = df[df['好きな動物'] == 'ライオン']['所持金額2'].mean()
means_nook = df[df['好きな動物'] == 'たぬき']['所持金額2'].mean()

# 所持金の平均を表示
print('「ライオン」の所持金平均: ' + str(means_lion))
print('「たぬき」の所持金平均  : ' + str(means_nook))
print()

# 判定
if means_lion < means_nook:
  print('「好きな動物」が「たぬき」の人の所持金の平均が多い')
else:
  print('「好きな動物」が「ライオン」の人の所持金の平均が多い')
