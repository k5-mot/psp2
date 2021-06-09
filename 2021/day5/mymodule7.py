# mymodule6.py

import mymodule4 as my


def pow(x, y):
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
  def __str__(self):
    return str(self.num) + '÷' + str(self.den)

  def show(self):
    print('分子=', self.num)
    print('分母=', self.den)

  def __pow__(self, y):
    num = self.num ** y
    den = self.den ** y
    return RationalChild(num, den)
