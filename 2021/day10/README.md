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
M = 
[[ 1  1  1  1]
 [ 8  4  2  1]
 [27  9  3  1]
 [64 16  4  1]]
a = [ 0.00000000e+00 -3.55271368e-15  2.00000000e+00  1.00000000e+00]  
b = [3 5 7 9]
d = 29.999999999999716


M =
[[81 31 72 76]
 [18 46 31 78]
 [10 32 28 91]
 [81 54 18 32]]
a = [ 2.01212992 -3.14995061 -2.51646929  2.41910176]
b = [68  2 69 25]
d = 1696.161188367155

M =
[[90 94 69 22]
 [56 68 18 16]
 [43 59 16 99]
 [26 28 98 69]]
a = [-4.47804827  4.83095182  0.14800343 -0.14988017]
b = [58 78 80 23]
d = -3994.9718529977263

M =
[[75 98 92 16]
 [12 18 31 55]
 [74  3 43 99]
 [55  1  7 68]]
a = [-0.36963362 -1.07032138  1.72645677  0.54874961]
b = [35 60 98 28]
d = -453.9136966544332

M =
[[70 79 36 53]
 [48 30  3 81]
 [33 17 28 80]
 [67 91 70 92]]
a = [-1.19281333 -0.00468058  1.3580861   0.90519999]
b = [13 20 71 98]
d = -1170.6485312674238
```
