#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve_sqrt(num):
  x = num
  n_loop = 10000
  error_limit = 0.001
  for n in range(n_loop):
    try:
      epsilon = (x ** 2 - num) / (2 * x)
    except ZeroDivisionError:
      x = 'stopped'
      break
    else:
      x_next = x - epsilon
      if (x_next - x) ** 2 < error_limit:
        break
      x = x_next
    finally:
      pass
  return x


def Differential(TargetFunc, x):
  h = 1e-4
  return (TargetFunc(x + h) - TargetFunc(x)) / h


def NewtonSolver(TargetFunc, x, n_loop=10000, error_limit=0.001):
  for n in range(n_loop):
    try:
      epsilon = TargetFunc(x) / Differential(TargetFunc, x)
    except ZeroDivisionError:
      x = 'stopped'
      break
    else:
      x_next = x - epsilon
      if (x_next - x)**2 < error_limit:
        break
      x = x_next
    finally:
      pass
  return x
