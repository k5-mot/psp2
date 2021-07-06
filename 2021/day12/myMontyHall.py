#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def MontyHall(tactics):
  '''
  入力
  - tactics: 1ならばKeep, 0ならばChange
  出力
  - hit: 宝を当てたら1, 外れたら0
  '''
  # Box Setup
  box = [1, 2, 3]
  answer = random.choice(box)
  first_choice = random.choice(box)

  # First Open
  box1 = box.copy()
  box1.remove(answer)
  if first_choice == answer:
    open = random.choice(box1)
  else:
    box_tmp = box1.copy()
    box_tmp.remove(first_choice)
    open = box_tmp[0]

  # Second Open
  box2 = box.copy()
  box2.remove(open)
  if tactics == 1:  # Keep
    second_choice = first_choice
  else:             # Change
    box_tmp = box2.copy()
    box_tmp.remove(first_choice)
    second_choice = box_tmp[0]

  # Hit Count
  if second_choice == answer:
    hit = 1
  else:
    hit = 0
  return hit
