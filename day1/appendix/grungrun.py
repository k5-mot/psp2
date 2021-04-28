from turtle import *

kame = Turtle() # キャンバスを作って，亀kameを召喚

n = 150
length = 4
angle = 15

kame.speed(0)
kame.color('red','yellow')
kame.begin_fill()
for _ in range(n):
    for _ in range(4):
        kame.forward(length)
        kame.left(90)
    kame.left(angle)
    length = length * 1.03
kame.end_fill()
done()
