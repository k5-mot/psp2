import sys
import numpy as np


def model1(input, term):
  return np.power(input, term)


def model2(input, term):
  return np.power(input, -term)


def createPattern(size):
  pattern_in = np.random.randint(-100, 100, size)
  pattern_out = np.random.randint(-100, 100, size)
  # pattern_in = np.array([1, 2, 3, 4])
  # pattern_out = np.array([3, 5, 7, 9])
  return pattern_in, pattern_out


def createMatrix(pattern_in, model):
  size = len(pattern_in)
  matrix_in = np.zeros((size, size))
  for i in range(size):
    input = pattern_in[i]
    for j in range(size):
      matrix_in[i][j] = model(input, size - j - 1)
  return matrix_in


def learnModel(pattern_in, pattern_out, model):
  matrix_in = createMatrix(pattern_in, model)
  pattern_inv = np.linalg.inv(matrix_in)
  params = np.matmul(pattern_inv, pattern_out)
  return params


def inferModel(params, input, model):
  sum = 0
  for i in range(len(params)):
    sum += params[i] * model(input, len(params) - i - 1)
  return sum


def main(argv):
  model = model1
  pattern_in, pattern_out = createPattern(4)
  params = learnModel(pattern_in, pattern_out, model)
  input = np.random.randint(0, 100, 1)
  output = inferModel(params, input, model)

  print('pattern1 = ', end='')
  print(pattern_in)
  print('pattern2 = ', end='')
  print(pattern_out)
  print('matrix1  = ')
  print(createMatrix(pattern_in, model))
  print('params   = ', end='')
  print(params)
  print()
  print('input    = ', end='')
  print(input[0])
  print('output   = ', end='')
  print(output[0])
  print()


if __name__ == "__main__":
  sys.exit(main(sys.argv))
