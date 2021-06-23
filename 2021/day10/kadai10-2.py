import sys
import numpy as np


def learnModel(M, b):
  Mi = np.linalg.inv(M)
  a = np.matmul(Mi, b)
  return a


def inferModel(a, s):
  return a[0] * (s ** 3) + a[1] * (s ** 2) + a[2] * (s ** 1) + a[3] * s


def main(argv):
  M = np.array(
      [[1, 1, 1, 1],
       [8, 4, 2, 1],
       [27, 9, 3, 1],
       [64, 16, 4, 1]])
  b = np.array([3, 5, 7, 9])
  a = learnModel(M, b)
  d = inferModel(a, 10)

  print('M = ')
  print(M)
  print('a = ', end='')
  print(a)
  print('b = ', end='')
  print(b)
  print('d = ', end='')
  print(d)
  print()
  print()

  for i in range(4):
    M = np.random.randint(0, 100, (4, 4))
    b = np.random.randint(0, 100, 4)
    a = learnModel(M, b)
    d = inferModel(a, 10)

    print('M = ')
    print(M)
    print('a = ', end='')
    print(a)
    print('b = ', end='')
    print(b)
    print('d = ', end='')
    print(d)
    print()


if __name__ == "__main__":
  sys.exit(main(sys.argv))
