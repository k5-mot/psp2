# d03.py
from turtle import *
import math


def come(x, y):
  """
  座標（x,y）を向いて，その方向に距離を一割だけ縮める
  """

  (xx, yy) = position()
  val_tan = (yy - y) / (xx - x)
  theta = math.atan(val_tan)
  head = heading()
  new_head = theta * 180 / math.pi - head
  walk = math.sqrt((xx - x)**2 + (yy - y)**2) / 10
  left(new_head)
  forward(walk)


MyList = [1, 2, 3]
NowPos = 5
try:
  NowVal = MyList[NowPos]
except IndexError:
  print('MyListから取り出せないので，とりあえず99入れときます．')
  NowVal = 99
else:
  pass


onscreenclick(come)

done()
