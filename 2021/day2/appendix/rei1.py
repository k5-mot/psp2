from turtle import *

kame = Turtle() # キャンバスを作って，亀kameを召喚

kame.shape('turtle')
kame.pensize(33) # ペンのサイズを33とする

for k in range(6):
    kame.forward(200)
    kame.left(60)

done()
