import myfunc


def FuncOne(x):
  return x ** 2 - 3


def FuncTwo(x):
  return x ** 2 - 10


xList = [-3, 3]     # 初期値のリスト
nLoop = int(1e4)    # 繰り返し回数
errorLimit = 1e-10  # 解の収束判定条件

print('kadai4-2')
print()

print('x^2 - 3 = 0')
for x_0 in xList:
  x = myfunc.NewtonSolver(TargetFunc=FuncOne, x=x_0, n_loop=nLoop, error_limit=errorLimit)
  print(x)

print('x^2 - 10 = 0')
for x_0 in xList:
  x = myfunc.NewtonSolver(TargetFunc=FuncTwo, x=x_0, n_loop=nLoop, error_limit=errorLimit)
  print(x)
