#!/usr/bin/env python
# coding: utf-8
import sys
import numpy as np


def model1(input, term):
    """
    モデル式

    Parameters
    ----------
    input : floatint
        入力変数x
    term : int
        項の順番

    Returns
    -------
    answer : int
        指定した項の値
    """
    return np.power(input, term)


def model2(input, term):
    """

    """
    return input ** -term


def createPattern(size):
    # pattern_in = np.random.randint(-100, 100, size)
    # pattern_out = np.random.randint(-100, 100, size)
    # pattern_in = np.array(pattern_in, dtype='float')
    # pattern_out = np.array(pattern_out, dtype='float')
    pattern_in = np.array([1, 2, 3, 4], dtype='float')
    pattern_out = np.array([3, 5, 7, 9], dtype='float')
    return pattern_in, pattern_out


def createMatrix(pattern_in, model):
    size = len(pattern_in)
    matrix_in = np.zeros((size, size))
    for i in range(size):
        input = pattern_in[i]
      for j in range(size):
          matrix_in[i][j] = model(input, float(size - j - 1))
    return matrix_in


def learnModel(pattern_in, pattern_out, model):
    matrix_in = createMatrix(pattern_in, model)
    pattern_inv = np.linalg.inv(matrix_in)
    params = np.matmul(pattern_inv, pattern_out)
    return params


def inferModel(params, input, model):
    sum = 0
    for i in range(len(params)):
        sum += params[i] * model(input, float(len(params) - i - 1))
    return sum


def main(argv):
    model = model1
    pattern_in, pattern_out = createPattern(4)
    params = learnModel(pattern_in, pattern_out, model)
    inputa = np.random.randint(-100, 100, 1)
    output = inferModel(params, inputa, model)
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
    print(inputa[0])
    print('output   = ', end='')
    print(output[0])
    print()


if __name__ == "__main__":
    sys.exit(main(sys.argv))

