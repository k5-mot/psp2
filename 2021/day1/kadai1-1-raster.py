#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle

kame = turtle.Turtle()
turtle.hideturtle()

radius = 33
raster_6 = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

startx = -radius * (len(raster_6[0]) - 1) / 2
starty = radius * (len(raster_6) - 1) / 2

kame.pensize(radius)
kame.penup()

for i in range(len(raster_6)):
  for j in range(len(raster_6[i])):
    if raster_6[i][j] == 1:
      kame.goto(startx + radius * j, starty - radius * i)
      kame.dot(radius)
      kame.penup()

ts = turtle.getscreen()
tc = ts.getcanvas()
tc.postscript(file="images/raster_6.eps", colormode='color')

turtle.done()
