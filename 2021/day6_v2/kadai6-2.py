#!/usr/bin/env python
# coding: utf-8
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# CSVファイルを読み込み
df = pd.read_csv('csv/mydata2.csv', index_col=0, skipinitialspace=True)

# 所持金を計算(1:増加前、2:増加後)
df['moneyTotal1'] = df['moneyIncreaseDiff'] / (df['moneyIncreaseRatio'] - 1)
df['moneyTotal2'] = df['moneyTotal1'] + df['moneyIncreaseDiff']

# 所持金の平均を計算
means_lion = df[df['favoriteAnimal'] == 'Lion']['moneyTotal2'].mean()
means_nook = df[df['favoriteAnimal'] == 'Tanuki']['moneyTotal2'].mean()

# 所持金の平均を表示
print('"Lion" の所持金平均   : ' + str(means_lion))
print('"Tanuki" の所持金平均 : ' + str(means_nook))
print()

# 判定
if means_lion < means_nook:
  print('「favoriteAnimal」が「Tanuki」の人の所持金の平均が多い')
else:
  print('「favoriteAnimal」が「Lion」の人の所持金の平均が多い')
