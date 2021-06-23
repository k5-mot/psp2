import sys
import numpy as np


def calcMatrix(M, b):
  Mi = np.linalg.inv(M)
  a = np.matmul(Mi, b)
  return a


def main():
  M = np.array(
      [[1, 2],
       [5, 7]])
  b = np.array([3, 9])
  a = calcMatrix(M, b)

  print('M = ')
  print(M)
  print()
  print('a = ')
  print(a)
  print()
  print('b = ')
  print(b)


if __name__ == "__main__":
  sys.exit(main())
