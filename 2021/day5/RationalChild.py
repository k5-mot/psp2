#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Rational as Rational


# def pow(x, y):
#   ret = 1
#   while y > 0:
#     ret *= x
#     y -= 1
#   return ret


def pow(x, y):
  ret = 1
  while (y > 0):
    if y & 1:
      ret *= x
    x *= x
    y >>= 1
  return ret


class RationalChild(Rational.Rational):
  def show(self):
    print('分子=', self.num)
    print('分母=', self.den)

  def __pow__(self, y):
    num = pow(self.num, y)
    den = pow(self.den, y)
    return RationalChild(num, den)
