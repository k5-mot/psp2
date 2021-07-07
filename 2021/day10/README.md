# day10

numpy

## kadai10-1

### 問題

連立方程式

<img src="https://latex.codecogs.com/gif.latex?x&space;&plus;&space;2&space;y&space;=&space;3" />

<img src="https://latex.codecogs.com/gif.latex?5x&space;&plus;&space;7y&space;=&space;9" />

の解となる
<img src="https://latex.codecogs.com/gif.latex?x" />
と
<img src="https://latex.codecogs.com/gif.latex?y" />
を求めよ。
連立方程式は、写像と同じであり、
ベクトル
<img src="https://latex.codecogs.com/gif.latex?\boldsymbol{a}=(x,y)" />
が写像行列
<img src="https://latex.codecogs.com/gif.latex?M=\begin{bmatrix}&space;1&space;&&space;2&space;\\&space;5&space;&&space;7&space;\\&space;\end{bmatrix}" />
によって
ベクトル
<img src="https://latex.codecogs.com/gif.latex?\boldsymbol{b}=(3,9)" />
に移されたことをあらわす。

<img src="https://latex.codecogs.com/gif.latex?M\boldsymbol{a}=\boldsymbol{b}" />


よって、線形代数によると係数行列の逆行列が存在すれば、

<img src="https://latex.codecogs.com/gif.latex?\boldsymbol{a}=M^{-1}\boldsymbol{b}" />

により、解
<img src="https://latex.codecogs.com/gif.latex?\boldsymbol{a}=(x,y)" />
を求めることができる。

numpyには行列を引数に与えると逆行列を求める関数があるので（自分で調べよ）、

「行列
<img src="https://latex.codecogs.com/gif.latex?M" />
と行列
<img src="https://latex.codecogs.com/gif.latex?b" />
を引数に与えると、解
<img src="https://latex.codecogs.com/gif.latex?a" />
を返す関数」を自作し、
それを用いて上記の連立方程式を解くpythonコードを作成せよ。

### 回答

```powershell
$ python kadai10-1.py 
M = 
[[1 2]
 [5 7]]

a =
[-1.  2.]

b =
[3 9]
```

## kadai10-2

### 問題

<img src="https://latex.codecogs.com/gif.latex?1&space;\rightarrow&space;3" />
<img src="https://latex.codecogs.com/gif.latex?2&space;\rightarrow&space;5" />
<img src="https://latex.codecogs.com/gif.latex?3&space;\rightarrow&space;7" />
<img src="https://latex.codecogs.com/gif.latex?4&space;\rightarrow&space;9" />

のとき、10はどうなるか？

<img src="https://latex.codecogs.com/gif.latex?10&space;\rightarrow&space;?" />

まず、入力
<img src="https://latex.codecogs.com/gif.latex?x" />
と出力
<img src="https://latex.codecogs.com/gif.latex?y" />
を繋ぐモデル式（適当な係数と、入出力の使い方）を作る。

今、パターンが４つわかっているので、入力を４つの未知変数に拡張し、４つの未知係数を用いて

<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;a&space;x^{3}&space;&plus;&space;b&space;x^{2}&space;&plus;&space;c&space;x&space;&plus;&space;d" />

などとしてみる。係数
<img src="https://latex.codecogs.com/gif.latex?a,b,c,d" />
の3次式モデルである。未知変数への拡張のしかたは他にもいくらでも考えられる。

<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;a&space;x^{-3}&space;&plus;&space;b&space;x^{-2}&space;&plus;&space;c&space;x^{-1}&space;&plus;&space;d" />

のようなモデル式でもいいだろう。

ひとまず3次式モデルとすると、与えられた４つのパターンは

<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1&1&1&1\\&space;8&4&2&1\\&space;27&9&3&1\\&space;64&16&4&1&space;\end{bmatrix}&space;\begin{bmatrix}&space;a\\b\\c\\d&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;3\\5\\7\\9&space;\end{bmatrix}" />

と書くことができる。よって係数は

<img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;a\\b\\c\\d&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;1&1&1&1\\&space;8&4&2&1\\&space;27&9&3&1\\&space;64&16&4&1&space;\end{bmatrix}^{-1}&space;\begin{bmatrix}&space;3\\5\\7\\9&space;\end{bmatrix}" />

で求めることができ、その係数を使えば、

<img src="https://latex.codecogs.com/gif.latex?10&space;\rightarrow&space;?" />


を推定できる。

実際この方法で、係数は、
<img src="https://latex.codecogs.com/gif.latex?(a,b,c,d)=(0,0,2,1)" />
と推定され、
<img src="https://latex.codecogs.com/gif.latex?y=2x&plus;1" />

すなわち、
<img src="https://latex.codecogs.com/gif.latex?10\rightarrow21" />
と推定される。

この推定値は、あくまで３次式モデルによる推定であり、他にも答えは考えられる。実際、先の逆数のモデルだと答えが異なる。

学習用のパターンを適当に４つ作り、適当にモデル式を作って係数を学習し、学習用パターンにない適当な入力を与えたときの出力を求めよ。（pythonコードで実現せよ）

### 回答

```powershell
$ python kadai10-2.py
pattern1 = [-54 -17  66 -68]
pattern2 = [-42  51 -51 -44]
matrix1  = 
[[-1.57464e+05  2.91600e+03 -5.40000e+01  1.00000e+00]
 [-4.91300e+03  2.89000e+02 -1.70000e+01  1.00000e+00]
 [ 2.87496e+05  4.35600e+03  6.60000e+01  1.00000e+00]
 [-3.14432e+05  4.62400e+03 -6.80000e+01  1.00000e+00]]        
params   = [-5.79629612e-04 -3.40850579e-02  2.48328730e+00  1.00218745e+02]

input    = 67
output   = -60.73997146548365
```

## kadai10-3

### 問題

2次元Numpy配列をデータフレームに変換せよ。

### 回答

```powershell
$ python kadai10-3.py
 行番号  列番号  赤明度  緑明度  青明度
      0       0     255       0       0
      0       1       0     255       0
      0       2       0       0     255
      0       3     255     255     255
      0       4       0       0       0
      0       5     255       0       0
      1       0       0     255       0
      1       1       0       0     255
      1       2     255     255     255
      1       3       0       0       0
      1       4     255       0       0
      1       5       0     255       0
      2       0       0       0     255
      2       1     255     255     255
      2       2       0       0       0
      2       3     255       0       0
      2       4       0     255       0
      2       5       0       0     255
      3       0     255     255     255
      3       1       0       0       0
      3       2     255       0       0
      3       3       0     255       0
      3       4       0       0     255
      3       5     255     255     255
```
