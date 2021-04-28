from turtle import *

def come(x,y):
    #座標(x,y)の方向の途中まで亀を動かす
    (xx, yy) = kame.position() 
    newxy = ((xx+x)/2, (yy+y)/2) # 中間座標
    kame.goto(newxy) # newxyまで動かす

kame = Turtle() # キャンバスを作って，亀kameを召喚

kame.shape('turtle')
kame.color('red','yellow')
kame.pensize(33) # ペンのサイズを33とする

onscreenclick(come)

done()

