from turtle import *

kame = Turtle() # キャンバスを作って，亀kameを召喚
kame.color('red', 'yellow')
kame.shape('turtle')
kame.begin_fill()
while True:
    kame.forward(200)
    kame.left(170)
    if abs(kame.pos()) < 1:
        break
kame.end_fill()
done()
