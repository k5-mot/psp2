#!/usr/bin/env python
# coding: utf-8
import sys
import myMontyHall as my


def main(argv):
  n_trial = 1000
  tactics_list = [0, 1]  # 1ならKeep, 0ならChange
  prob = [0, 0]

  for tactics in tactics_list:
    p = 0
    for i in range(n_trial):
      p += my.MontyHall(tactics)
    prob[tactics] = p / n_trial

  print('Keep戦略   : ', prob[1])
  print('Change戦略 : ', prob[0])
  return 0


if __name__ == "__main__":
  sys.exit(main(sys.argv))
