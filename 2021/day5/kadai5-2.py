#!/usr/bin/env python
# coding: utf-8
import sys
import RationalChild as RationalChild


def main():
  x = RationalChild.RationalChild(5, 10)
  print('x = ', end='')
  print(x)

  y = 2
  print('y = ', end='')
  print(y)
  print("x ** y = " + str(x ** y))


if __name__ == "__main__":
  sys.exit(main())
