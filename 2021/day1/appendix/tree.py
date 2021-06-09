from turtle import *
import math

kame = Turtle() # キャンバスを作って，亀kameを召喚

#initializeTurtle(initial_speed=10)
#kame.setup(1400, 1300, None, None)
kame.speed(10000000)
kame.color('red', 'black')
bgcolor('black')
kame.shape('turtle')
#min_length=20
min_length=10

def draw_branch(l, w):
  kame.left(15)
  draw_stick(l, w)
  kame.right(30)
  draw_stick(l, w)
  kame.left(15)

def draw_stick(l, w):
  kame.width(w)
  kame.forward(l)
  if min_length < l:
    draw_branch(math.ceil(l*0.8), math.ceil(w*0.6))
  kame.backward(l)

kame.penup()
#kame.sety(470)
kame.sety(-200)
kame.pendown()
draw_branch(100, 10)
done()
