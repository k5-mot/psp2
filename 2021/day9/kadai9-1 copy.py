#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


def main():
  # Prepare data
  df = pd.read_csv('./csv/score.csv')
  # Prepare graph
  fig, axes = plt.subplots(1, 1)
  # Setup figure
  fig.suptitle("Main Title", fontsize=16)
  # Setup axes.
  axes.set_title("Graph Title")
  axes.set_xlabel("t")
  axes.set_ylabel("f(t)")
  axes.hist(df[['height']])
  # axes.plot(t, f, color="blue", label="f(t)")
  axes.grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)
  #axes.legend(loc=0, frameon=True)
  # Display graph
  plt.tight_layout()
  plt.savefig("./images/kadai9-1.png")
  plt.show()


if __name__ == "__main__":
  sys.exit(main())
