#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle

kame = turtle.Turtle()

radius = 33
raster_9 = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

startx = -radius * (len(raster_9[0]) // 2)
starty = radius * (len(raster_9) // 2)

kame.pensize(radius)
kame.penup()

for i in range(len(raster_9)):
  for j in range(len(raster_9[i])):
    if raster_9[i][j] == 1:
      kame.goto(startx + radius * j, starty - radius * i)
      kame.dot(radius)
      kame.penup()

turtle.done()
