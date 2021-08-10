#!/usr/bin/env python
# coding: utf-8
import turtle


def polygon(N):
  interior_angle = 180 * (N - 2) / N
  turn_angle = 180.0 - interior_angle
  (x, y) = kame.position()
  while True:
    kame.forward(100)
    kame.left(turn_angle)

    (xx, yy) = kame.position()
    if (xx - x)**2 + (yy - y)**2 < 1:
      break


kame = turtle.Turtle()
turtle.hideturtle()
kame.pensize(10)

polygon(5)

ts = turtle.getscreen()
tc = ts.getcanvas()
tc.postscript(file="./images/pentagon.eps", colormode='color')

turtle.done()
