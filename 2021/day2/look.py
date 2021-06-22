#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle
import math


def look(x, y):
  # カメの向きの角度
  kame_dir = kame.heading()
  if (kame_dir > 180):
    kame_dir = kame_dir - 360
  # カメの位置
  (xx, yy) = kame.position()
  # カメの位置とクリックした位置の角度
  rad = math.atan2((y - yy), (x - xx))
  degree = math.degrees(rad)
  # カメを向かせる
  if (degree - kame_dir) > 0:
    angle = degree - kame_dir
    kame.left(angle)
  else:
    angle = kame_dir - degree
    kame.right(angle)


kame = turtle.Turtle()
turtle.hideturtle()
kame.shape('turtle')
kame.pensize(33)

turtle.onscreenclick(look)

ts = turtle.getscreen()
tc = ts.getcanvas()
tc.postscript(file="./images/look.eps", colormode='color')

turtle.done()
