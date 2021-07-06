#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import myMontyHall as my


def main(argv):
  n_trial = 1000
  tactics_list = [0, 1]  # 1ならKeep, 0ならChange

  Prob = [0, 0]

  for tactics in tactics_list:
    p = 0
    for i in range(n_trial):
      p += my.MontyHall(tactics)

    Prob[tactics] = p / n_trial

  print('Keep戦略:', Prob[1])
  print('Change戦略:', Prob[0])
  return 0


if __name__ == "__main__":
  sys.exit(main(sys.argv))
