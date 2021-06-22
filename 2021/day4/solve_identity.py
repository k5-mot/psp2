#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import myfunc


def FuncOne(x):
  return x ** 2 - 3


def FuncTwo(x):
  return x ** 2 - 10


def main():
  xList = [-3, 3]     # 初期値のリスト
  nLoop = int(1e4)    # 繰り返し回数
  errorLimit = 1e-10  # 解の収束判定条件

  print('x^2 - 3 = 0')
  print('x = ', end='')
  x_ans = list()
  for x_0 in xList:
    x = myfunc.NewtonSolver(TargetFunc=FuncOne, x=x_0, n_loop=nLoop, error_limit=errorLimit)
    x_ans.append(x)
  x_ans = [str(x) for x in x_ans]
  x_ans = ', '.join(x_ans)
  print(x_ans)
  print()

  print('x^2 - 10 = 0')
  print('x = ', end='')
  x_ans = list()
  for x_0 in xList:
    x = myfunc.NewtonSolver(TargetFunc=FuncTwo, x=x_0, n_loop=nLoop, error_limit=errorLimit)
    x_ans.append(x)
  x_ans = [str(x) for x in x_ans]
  x_ans = ', '.join(x_ans)
  print(x_ans)


if __name__ == "__main__":
  sys.exit(main())
