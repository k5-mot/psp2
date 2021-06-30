import sys
import numpy as np


def learnModel(M, b):
  Mi = np.linalg.inv(M)
  a = np.matmul(Mi, b)
  return a


def inferModel(a, s):
  return a[0] * (s ** 3) + a[1] * (s ** 2) + a[2] * (s ** 1) + a[3] * s


def main(argv):
  M = np.random.randint(0, 100, (4, 4))
  b = np.random.randint(0, 100, 4)
  a = learnModel(M, b)
  c = np.random.randint(0, 100, 1)
  d = inferModel(a, c)

  print('M = ')
  print(M)
  print('b = ', end='')
  print(b)
  print('a = M^-1 b = ', end='')
  print(a)
  print('c = ', end='')
  print(c[0])
  print('d = f(a, c) = ', end='')
  print(d[0])
  print()


if __name__ == "__main__":
  sys.exit(main(sys.argv))
