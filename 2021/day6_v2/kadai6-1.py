#!/usr/bin/env python
# coding: utf-8
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# CSVファイルを読み込み
df = pd.read_csv('csv/mydata2.csv', index_col=0, skipinitialspace=True)
# cerelyFavorの大小関係を定義
listCelery = list(['extremelyHate', 'Hate', 'Regular', 'Like', 'extremelyLike'])
df['cerelyFavor'] = pd.Categorical(df['cerelyFavor'], categories=listCelery, ordered=True)
# cerelyFavorの大小を数値(cerelyFavor度値)に変換
df['cerelyFavor度値'] = df['cerelyFavor'].cat.codes

# cerelyFavor度値の第1四分位数と第3四分位数を計算
iqr25_lion = df[df['favoriteAnimal'] == 'Lion']['cerelyFavor度値'].quantile(0.25)
iqr75_lion = df[df['favoriteAnimal'] == 'Lion']['cerelyFavor度値'].quantile(0.75)
iqr25_nook = df[df['favoriteAnimal'] == 'Tanuki']['cerelyFavor度値'].quantile(0.25)
iqr75_nook = df[df['favoriteAnimal'] == 'Tanuki']['cerelyFavor度値'].quantile(0.75)

# cerelyFavor度値の第1四分位数と第3四分位数を表示
print('Lion ')
print('  第 1 四分位数 ( 25 % ) = ' + str(iqr25_lion))
print('  第 3 四分位数 ( 75 % ) = ' + str(iqr75_lion))
print('Tanuki ')
print('  第 1 四分位数 ( 25 % ) = ' + str(iqr25_nook))
print('  第 3 四分位数 ( 75 % ) = ' + str(iqr75_nook))
print()

# 判定
if iqr25_lion < iqr25_nook and iqr25_nook < iqr75_lion:
  print('四分位範囲が重なっている。差があるとは言えない。')
elif iqr25_lion < iqr75_nook and iqr75_nook < iqr75_lion:
  print('四分位範囲が重なっている。差があるとは言えない。')
else:
  print('四分位範囲が重なっていない。差がある。')
