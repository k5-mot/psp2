#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle

kame = turtle.Turtle()
turtle.hideturtle()

radius = 33
vector_6 = [
    [0, 2, 2, 2],
    [2, 2, 2, 4],
    [2, 4, 0, 4],
    [0, 4, 0, 0],
    [0, 0, 2, 0]
]

minx = min([row[0] for row in vector_6] + [row[2] for row in vector_6])
maxx = max([row[0] for row in vector_6] + [row[2] for row in vector_6])
miny = min([row[1] for row in vector_6] + [row[3] for row in vector_6])
maxy = max([row[1] for row in vector_6] + [row[3] for row in vector_6])
startx = -(maxx - minx) / 2 * radius
starty = (maxy - miny) / 2 * radius

kame.pensize(radius)
kame.penup()

for i in range(len(vector_6)):
  kame.goto(vector_6[i][0] * radius + startx, -vector_6[i][1] * radius + starty)
  kame.pendown()
  kame.goto(vector_6[i][2] * radius + startx, -vector_6[i][3] * radius + starty)
  kame.penup()

ts = turtle.getscreen()
tc = ts.getcanvas()
tc.postscript(file="images/vector_6.eps", colormode='color')

turtle.done()
