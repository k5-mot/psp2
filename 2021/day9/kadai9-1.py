#!/usr/bin/env python
# coding: utf-8
import sys
import matplotlib.pyplot as plt
import pandas as pd


def main():
  # CSVファイルを読み込み
  df = pd.read_csv('./csv/score.csv')
  # 成績評価の大小関係を定義
  listScore = list(['D', 'C', 'B', 'A'])
  df['score'] = pd.Categorical(df['score'], categories=listScore, ordered=True)
  # 成績評価の大小を数値に変換
  df['scoreValue'] = df['score'].cat.codes
  df = df.sort_values('score', ascending=False)
  df['age'].astype('int')

  # グラフの用意
  fig, axes = plt.subplots(2, 3)
  # 画像タイトル
  fig.suptitle("kadai9-1", fontsize=16)
  fig.set_figheight(8)
  fig.set_figwidth(12)
  # グラフを用意
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

  axes[0, 2].set_title("Distribution of Heights by gender")
  axes[0, 2].set_xlabel("gender")
  axes[0, 2].set_ylabel("height[cm]")
  axes[0, 2].boxplot([df[df['gender'] == 0]['height'], df[df['gender'] == 1]['height']], labels=['Male', 'Female'])
  axes[0, 2].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)

  axes[1, 0].set_title("Heights & Scores by gender")
  axes[1, 0].set_xlabel("score")
  axes[1, 0].set_ylabel("height")
  axes[1, 0].scatter(x=df[df['gender'] == 0]['score'], y=df[df['gender'] == 0]['height'], label='Male')
  axes[1, 0].scatter(x=df[df['gender'] == 1]['score'], y=df[df['gender'] == 1]['height'], label='Female')
  axes[1, 0].legend()
  axes[1, 0].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)

  axes[1, 1].set_title("Ages & heights by gender")
  axes[1, 1].set_xlabel("age")
  axes[1, 1].set_xticks([17, 18, 19, 20])
  axes[1, 1].set_ylabel("height")
  axes[1, 1].scatter(x=df[df['gender'] == 0]['age'], y=df[df['gender'] == 0]['height'], label='Male')
  axes[1, 1].scatter(x=df[df['gender'] == 1]['age'], y=df[df['gender'] == 1]['height'], label='Female')
  axes[1, 1].legend()
  axes[1, 1].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)

  axes[1, 2].set_title("Distribution of Scores by gender")
  axes[1, 2].set_xlabel("gender")
  axes[1, 2].set_ylabel("score")
  axes[1, 2].boxplot([df[df['gender'] == 0]['scoreValue'], df[df['gender'] == 1]['scoreValue']], labels=['Male', 'Female'])
  axes[1, 2].grid(b=True, which="both", axis="both", color="black", alpha=0.5, linestyle="-", linewidth=1)

  # グラフを保存・表示
  plt.tight_layout()
  plt.savefig("./images/kadai9-1.png")
  plt.show()


if __name__ == "__main__":
  sys.exit(main())
