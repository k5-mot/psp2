#!/usr/bin/env python
# coding: utf-8
import turtle
import math


def come(x, y):
  """
  座標(x, y)の方向の途中まで亀を動かす
  """
  (xx, yy) = kame.position()
  newxy = ((xx + x) / 2, (yy + y) / 2)  # 中間座標
  kame.goto(newxy)  # newxyまで動かす


def look(x, y):
  """
  亀の向きを変えてマウスクリック方向に途中まで移動する
  """
  # カメの位置
  (xx, yy) = kame.position()
  # カメの位置とクリックした位置の角度
  rad = math.atan2((y - yy), (x - xx))
  deg = math.degrees(rad)
  # カメの方向転換
  kame.setheading(deg)
  # カメの移動
  distance = math.sqrt((x - xx) ** 2 + (y - yy) ** 2)
  kame.forward(distance)


kame = turtle.Turtle()
turtle.hideturtle()
kame.shape('turtle')

turtle.onscreenclick(look)

ts = turtle.getscreen()
tc = ts.getcanvas()
tc.postscript(file="./images/look.eps", colormode='color')

turtle.done()
