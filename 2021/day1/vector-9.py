#!/usr/bin/env python
# coding: utf-8
import turtle

kame = turtle.Turtle()
turtle.hideturtle()

radius = 33
vector_9 = [
    [2, 2, 0, 2],
    [0, 2, 0, 0],
    [0, 0, 2, 0],
    [2, 0, 2, 4],
    [2, 4, 0, 4]
]

minx = min([row[0] for row in vector_9] + [row[2] for row in vector_9])
maxx = max([row[0] for row in vector_9] + [row[2] for row in vector_9])
miny = min([row[1] for row in vector_9] + [row[3] for row in vector_9])
maxy = max([row[1] for row in vector_9] + [row[3] for row in vector_9])
startx = -(maxx - minx) / 2 * radius
starty = (maxy - miny) / 2 * radius

kame.pensize(radius)
kame.penup()

for i in range(len(vector_9)):
  kame.goto(vector_9[i][0] * radius + startx, -vector_9[i][1] * radius + starty)
  kame.pendown()
  kame.goto(vector_9[i][2] * radius + startx, -vector_9[i][3] * radius + starty)
  kame.penup()

ts = turtle.getscreen()
tc = ts.getcanvas()
tc.postscript(file="./images/vector_9.eps", colormode='color')

turtle.done()
