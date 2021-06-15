#!/usr/bin/env python
# -*- coding: utf-8 -*-
from turtle import *


def polygon(N):
  naikaku = 180 * (N - 2)
  angle = naikaku / N
  angleL = 180.0 - angle
  (x, y) = kame.position()
  while True:
    # Nを用いた角度で進行方向を変えて，動かす
    kame.forward(100)
    kame.left(angleL)

    (xx, yy) = kame.position()
    if (xx - x)**2 + (yy - y)**2 < 1:
      break


kame = Turtle()  # キャンバスを作って，亀kameを召喚

kame.shape('turtle')
kame.color('red', 'yellow')
kame.pensize(33)  # ペンのサイズを33とする

polygon(5)


done()
