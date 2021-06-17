#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle

kame = turtle.Turtle()

kame.penup()       # ペンを持ち上げておく

kame.goto(0, 132)  # 座標(0,132)に行く
kame.dot(33)       # そこで太さ33のペンを下ろす
kame.penup()

kame.goto(33, 132)
kame.dot(33)
kame.penup()

kame.goto(66, 132)
kame.dot(33)
kame.penup()

kame.goto(0, 99)
kame.dot(33)
kame.penup()

kame.goto(66, 99)
kame.dot(33)
kame.penup()

kame.goto(0, 66)
kame.dot(33)
kame.penup()

kame.goto(33, 66)
kame.dot(33)
kame.penup()

kame.goto(66, 66)
kame.dot(33)
kame.penup()

kame.goto(66, 33)
kame.dot(33)
kame.penup()

kame.goto(0, 0)
kame.dot(33)
kame.penup()

kame.goto(33, 0)
kame.dot(33)
kame.penup()

kame.goto(66, 0)
kame.dot(33)
kame.penup()

turtle.done()
