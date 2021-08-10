#!/usr/bin/env python
# coding: utf-8
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# Read database.
df = pd.read_csv('csv/mydata2.csv', index_col=0, skipinitialspace=True)

# Categorize database
listCelery = list(['extremelyHate', 'Hate', 'Regular', 'Like', 'extremelyLike'])
df['cerelyFavor'] = pd.Categorical(df['cerelyFavor'], categories=listCelery, ordered=True)
df['cerelyFavor度値'] = df['cerelyFavor'].cat.codes

# Print results
iqr25_lion = df[df['favoriteAnimal'] == 'Lion']['cerelyFavor度値'].quantile(0.25)
iqr75_lion = df[df['favoriteAnimal'] == 'Lion']['cerelyFavor度値'].quantile(0.75)
iqr25_nook = df[df['favoriteAnimal'] == 'Tanuki']['cerelyFavor度値'].quantile(0.25)
iqr75_nook = df[df['favoriteAnimal'] == 'Tanuki']['cerelyFavor度値'].quantile(0.75)

print('Lion ')
print('  第 1 四分位数 ( 25 % ) = ' + str(iqr25_lion))
print('  第 3 四分位数 ( 75 % ) = ' + str(iqr75_lion))
print('Tanuki ')
print('  第 1 四分位数 ( 25 % ) = ' + str(iqr25_nook))
print('  第 3 四分位数 ( 75 % ) = ' + str(iqr75_nook))
print()

if iqr25_lion < iqr25_nook and iqr25_nook < iqr75_lion:
  print('四分位範囲が重なっている。差があるとは言えない。')
elif iqr25_lion < iqr75_nook and iqr75_nook < iqr75_lion:
  print('四分位範囲が重なっている。差があるとは言えない。')
else:
  print('四分位範囲が重なっていない。差がある。')
