#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Rational as Rational


def main():
  x = Rational.Rational(1, 10)
  print('x = ', end='')
  print(x)

  y = Rational.Rational(2, 10)
  print('y = ', end='')
  print(y)

  print('x + y = ', end='')
  print(x + y)

  print('x - y = ', end='')
  print(x - y)

  print('x * y = ', end='')
  print(x * y)

  print('x / y = ', end='')
  print(x / y)


if __name__ == "__main__":
  sys.exit(main())
