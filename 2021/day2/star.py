#!/usr/bin/env python
# coding: utf-8
import turtle


def star(edge_len):
  for k in range(5):
    kame.forward(edge_len)
    kame.right(144)
    kame.forward(edge_len)
    kame.left(72)


kame = turtle.Turtle()
turtle.hideturtle()
kame.pensize(10)

star(100)

ts = turtle.getscreen()
tc = ts.getcanvas()
tc.postscript(file="./images/star.eps", colormode='color')

turtle.done()
