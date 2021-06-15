#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from turtle import *
import math


def come(x, y):
  """
  座標（x,y）を向いて，その方向に距離を半分だけ縮める
  """
  # カメの位置
  (xx, yy) = kame.position()
  # カメの現在向いている角度
  kame_head_angle = kame.heading()
  if (kame_head_angle > 180):
    kame_head_angle = kame_head_angle - 360
  # 水平方向と、カメの位置-クリックした位置のなす角度
  rad = math.atan2((y - yy), (x - xx))
  degree = math.degrees(rad)
  # カメを動かす距離
  length = math.sqrt((xx - x) ** 2 + (yy - y) ** 2) / 2
  # カメをクリックした点に近づかせる処理
  angle = degree - kame_head_angle
  kame.left(angle)
  kame.forward(length)


# キャンバスを作って，亀kameを召喚
kame = Turtle()
kame.shape('turtle')
kame.color('red', 'yellow')
kame.pensize(10)

onscreenclick(come)
done()
