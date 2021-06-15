#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd


def main():
  x = np.array([x for x in range(100)]) / 100

  fig, (axe_alice, axe_bob) = plt.subplots(2, 1)  # Create a figure and an axes.
  axe_alice.plot(x, x, label='linear')            # Plot some data on the axes.
  axe_alice.plot(x, x**2, label='quadratic')      # Plot more data on the axes...
  axe_bob.plot(x, x**3, label='cubic')            # ... and some more.
  axe_alice.set_xlabel('x label')                 # Add an x-label to the axes.
  axe_bob.set_ylabel('y label')                   # Add a y-label to the axes.
  axe_alice.legend()                              # Add a legend.
  axe_bob.set_title("Simple Plot")                # Add a title to the axes.

  plt.show()


if __name__ == "__main__":
  sys.exit(main())
