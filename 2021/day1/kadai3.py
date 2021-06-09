#!/usr/bin/env python
# -*- coding: utf-8 -*-
from turtle import *

kame = Turtle()  # キャンバスを作って，亀kameを召喚

kame.shape('turtle')
kame.pensize(33)  # ペンのサイズを33とする
kame.forward(66 * 2)  # kameを66ピクセル直進させる
kame.left(90)  # kameを左回りに90度回転させる
kame.forward(132 * 2)
kame.left(90)
kame.forward(66 * 2)
kame.left(90)
kame.forward(66 * 2)
kame.left(90)
kame.forward(66 * 2)
done()

# kame.pensize(33) # ペンのサイズを33とする
# kame.forward(66) # kameを66ピクセル直進させる
# kame.left(90) # kameを左回りに90度回転させる
# kame.forward(132)
# kame.left(90)
# kame.forward(66)
# kame.left(90)
# kame.forward(66)
# kame.left(90)
# kame.forward(66)
