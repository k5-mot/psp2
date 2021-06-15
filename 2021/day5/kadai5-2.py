#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import RationalChild as RationalChild


def main():
  x = RationalChild.RationalChild(5, 10)
  print(x)
  x.show()
  print(x ** 2)


if __name__ == "__main__":
  sys.exit(main())
