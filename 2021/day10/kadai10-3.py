#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
# from matplotlib import pyplot as plt
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

# 色の指定
pR = np.array([255, 0, 0])      # 真っ赤
pG = np.array([0, 255, 0])      # 真緑
pB = np.array([0, 0, 255])      # 真っ青
pW = np.array([255, 255, 255])  # 白
pK = np.array([0, 0, 0])        # 黒

# 画像の指定
G = np.array([[pR, pG, pB, pW, pK, pR],
              [pG, pB, pW, pK, pR, pG],
              [pB, pW, pK, pR, pG, pB],
              [pW, pK, pR, pG, pB, pW]])

# 画像の表示
# plt.imshow(G, vmin=0, vmax=255)
# plt.show()

# 画像を表に変換
G = np.reshape(G, (24, 3))
idx = np.indices((4, 6))
G = np.concatenate([idx[0].reshape(24, -1), idx[1].reshape(24, -1), G], 1)

# データフレームに変換
label = ['行番号', '列番号', '赤明度', '緑明度', '青明度']
df = pd.DataFrame(data=G, columns=label)
print(df.to_string(index=False))
