# day6 

pandas

## kadai6-1

### 問題

「favoriteAnimal」が「Lion」の人と「Tanuki」の人でCerelyFavor度は差があると言えるか調べよ。
調べるためのコード実行例を示せ。
一般的に双方の四分位範囲が重ならない場合「差がある」と言う。
重なっている場合は「差があると言えない」と言う。

四分位範囲(IQR, Inter Quantile Range)とは，25%-75%の広さである。

### 回答

```powershell
$ python kadai6-1.py
Lion
  第 1 四分位数 ( 25 % ) = 1.0
  第 3 四分位数 ( 75 % ) = 1.0
Tanuki
  第 1 四分位数 ( 25 % ) = 0.75
  第 3 四分位数 ( 75 % ) = 2.25

四分位範囲が重なっていない。差がある。
```

## kadai6-2

### 問題

「favoriteAnimal」が「Lion」の人と「Tanuki」の人では、
どちらが平均的に今日の所持金が多いか?
(どちらが増加が大きいかではない)

### 回答

```powershell
$ python3 kadai6-2.py
"Lion" の所持金平均   : 299700.0
"Tanuki" の所持金平均 : 28500.0

「favoriteAnimal」が「Lion」の人の所持金の平均が多い
```
