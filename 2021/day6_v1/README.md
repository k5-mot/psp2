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
ライオン
  第 1 四分位数 ( 25% ) = 1.5
  第 3 四分位数 ( 75% ) = 2.5
たぬき
  第 1 四分位数 ( 25% ) = 0.75
  第 3 四分位数 ( 75% ) = 2.25

四分位範囲が重なっている。差があるとは言えない。
```

## kadai6-2

### 問題

「favoriteAnimal」が「Lion」の人と「Tanuki」の人では、
どちらが平均的に今日の所持金が多いか?
(どちらが増加が大きいかではない)

### 回答

```powershell
$ python kadai6-2.py
「ライオン」の所持金平均: 151350.0
「たぬき」の所持金平均  : 28500.0

「好きな動物」が「ライオン」の人の所持金の平均が多い
```

