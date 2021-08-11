#!/usr/bin/env python
# coding: utf-8
import Rational as my


def pow_v1(x, y):
  ret = 1
  while y > 0:
    ret *= x
    y -= 1
  return ret


def pow_v2(x, y):
  ret = 1
  while (y > 0):
    if y & 1:
      ret *= x
    x *= x
    y >>= 1
  return ret


class RationalChild(my.Rational):
  def show(self):
    print('分子=', self.num)
    print('分母=', self.den)

  def __pow__(self, y):
    num = pow_v1(self.num, y)
    den = pow_v1(self.den, y)
    return RationalChild(num, den)
