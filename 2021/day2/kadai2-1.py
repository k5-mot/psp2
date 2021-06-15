#!/usr/bin/env python
# -*- coding: utf-8 -*-
from turtle import *

kame = Turtle()  # キャンバスを作って，亀kameを召喚

kame.shape('turtle')
kame.color('red', 'yellow')
kame.pensize(33)  # ペンのサイズを33とする

for k in range(5):
  kame.forward(200)
  kame.right(90 + 54)  # 星形の先は36度
  kame.forward(200)
  kame.left(72)

done()
