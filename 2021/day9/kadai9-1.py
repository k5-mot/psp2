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
  fig, axes = plt.subplots(2, 2)
  # Setup figure
  fig.suptitle("Score", fontsize=16)
  # Setup axes.
  axes[0, 0].set_title("Heights of Male")
  axes[0, 0].set_xlabel("height[cm]")
  axes[0, 0].set_ylabel("frequency")
  axes[0, 0].hist(df[df['gender'] == 0]['height'])
  axes[0, 0].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)

  axes[0, 1].set_title("Heights of Female")
  axes[0, 1].set_xlabel("height[cm]")
  axes[0, 1].set_ylabel("frequency")
  axes[0, 1].hist(df[df['gender'] == 1]['height'])
  axes[0, 1].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)

  # axes[0, 1].set_title("Gender")
  # axes[0, 1].set_xlabel("height[cm]")
  # axes[0, 1].set_ylabel("frequency")
  # #axes[0, 1].hist(df[['height']])
  # df[['gender']].value_counts().plot(kind='bar', ax=axes[0, 1])
  # axes[0, 1].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)
  # Display graph
  plt.tight_layout()
  plt.savefig("./images/kadai9-1.png")
  plt.show()


if __name__ == "__main__":
  sys.exit(main())
