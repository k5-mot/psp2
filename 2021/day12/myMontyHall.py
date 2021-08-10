#!/usr/bin/env python
# coding: utf-8
import random


def MontyHall(tactics):
  '''
  入力
  - tactics: 1ならばKeep, 0ならばChange
  出力
  - hit: 宝を当てたら1, 外れたら0
  '''
  box = [1, 2, 3]
  # 答え
  answer = random.choice(box)
  # 最初の選択
  first_choice = random.choice(box)
  box1 = box.copy()
  box1.remove(answer)
  if first_choice == answer:
    open = random.choice(box1)
  else:
    box_tmp = box1.copy()
    box_tmp.remove(first_choice)
    open = box_tmp[0]

  # 二度目の選択
  box2 = box.copy()
  box2.remove(open)
  if tactics == 1:  # Keep
    second_choice = first_choice
  else:             # Change
    box_tmp = box2.copy()
    box_tmp.remove(first_choice)
    second_choice = box_tmp[0]

  # 当たりのカウント
  if second_choice == answer:
    hit = 1
  else:
    hit = 0
  return hit
