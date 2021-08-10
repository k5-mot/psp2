#!/usr/bin/env python
# coding: utf-8
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# Read database.
df = pd.read_csv('csv/mydata2.csv', index_col=0)

# Categorize database
df['所持金額1'] = df['所持金の増加（差）'] / (df['所持金の増加（比）'] - 1)
df['所持金額2'] = df['所持金額1'] + df['所持金の増加（差）']

# Print results
means_lion = df[df['好きな動物'] == 'ライオン']['所持金額2'].mean()
means_nook = df[df['好きな動物'] == 'たぬき']['所持金額2'].mean()

print('「ライオン」の所持金平均: ' + str(means_lion))
print('「たぬき」の所持金平均  : ' + str(means_nook))
print()

if means_lion < means_nook:
  print('「好きな動物」が「たぬき」の人の所持金の平均が多い')
else:
  print('「好きな動物」が「ライオン」の人の所持金の平均が多い')
