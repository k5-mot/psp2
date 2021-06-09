from turtle import *
import math


def look(x,y):
  # カメの向きの角度
  kame_dir = kame.heading()
  if (kame_dir > 180):
    kame_dir = kame_dir - 360
  #print("KAME_DIR: " + str(kame_dir))
  # カメの位置
  (xx, yy) = kame.position()
  # カメの位置とクリックした位置の角度 
  rad = math.atan2((y - yy), (x - xx))
  degree = math.degrees(rad)
  #print("NEXT_DIR: " + str(degree))
  # カメを向かせる
  if (degree - kame_dir) > 0:
    angle = degree - kame_dir
    #print("ANGLE: " + str(angle))
    #print()
    kame.left(angle)
  else:
    angle = kame_dir - degree
    #print("ANGLE: " + str(-angle))
    #print()
    kame.right(angle)


kame = Turtle() # キャンバスを作って，亀kameを召喚

kame.shape('turtle')
kame.color('red','yellow')
kame.pensize(33) # ペンのサイズを33とする

onscreenclick(look)

done()
