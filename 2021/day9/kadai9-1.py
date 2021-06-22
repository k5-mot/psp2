#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import matplotlib.pyplot as plt
import pandas as pd


def main():
  # Prepare data
  df = pd.read_csv('./csv/score.csv')
  # Categorize database
  listScore = list(['D', 'C', 'B', 'A'])
  df['score'] = pd.Categorical(df['score'], categories=listScore, ordered=True)
  df['scoreValue'] = df['score'].cat.codes
  df = df.sort_values('score', ascending=False)
  df['age'].astype('int')
  # Prepare graph
  fig, axes = plt.subplots(2, 2)
  # Setup figure
  fig.suptitle("kadai9-1", fontsize=16)
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

  axes[1, 0].set_title("Heights & Scores of Male & Female")
  axes[1, 0].set_xlabel("score")
  axes[1, 0].set_ylabel("height")
  axes[1, 0].scatter(x=df[df['gender'] == 0]['score'], y=df[df['gender'] == 0]['height'], label='Male')
  axes[1, 0].scatter(x=df[df['gender'] == 1]['score'], y=df[df['gender'] == 1]['height'], label='Female')
  axes[1, 0].legend()
  axes[1, 0].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)

  axes[1, 1].set_title("Ages & heights of Male & Female")
  axes[1, 1].set_xlabel("age")
  axes[1, 1].set_xticks([17, 18, 19, 20])
  axes[1, 1].set_ylabel("height")
  axes[1, 1].scatter(x=df[df['gender'] == 0]['age'], y=df[df['gender'] == 0]['height'], label='Male')
  axes[1, 1].scatter(x=df[df['gender'] == 1]['age'], y=df[df['gender'] == 1]['height'], label='Female')
  axes[1, 1].legend()
  axes[1, 1].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)

  # Display graph
  plt.tight_layout()
  plt.savefig("./images/kadai9-1.png")
  plt.show()


if __name__ == "__main__":
  sys.exit(main())
