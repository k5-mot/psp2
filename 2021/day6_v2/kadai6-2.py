#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# Read database.
df = pd.read_csv('csv/mydata2.csv', index_col=0, skipinitialspace=True)

# Categorize database
df['moneyTotal'] = df['moneyIncreaseDiff'] / (df['moneyIncreaseRatio'] - 1)

# Print results
means_lion = df[df['favoriteAnimal'] == 'Lion']['moneyTotal'].mean()
means_nook = df[df['favoriteAnimal'] == 'Tanuki']['moneyTotal'].mean()

print('"Lion" の所持金平均   : ' + str(means_lion))
print('"Tanuki" の所持金平均 : ' + str(means_nook))
print()

if means_lion < means_nook:
  print('「favoriteAnimal」が「Tanuki」の人の所持金の平均が多い')
else:
  print('「favoriteAnimal」が「Lion」の人の所持金の平均が多い')
