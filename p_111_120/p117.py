#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 117:
Using a combination of black square tiles and oblong tiles chosen
from: red tiles measuring two units, green tiles measuring three
units, and blue tiles measuring four units, it is possible to tile a
row measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116.

ANSWER : 100808458960497
'''

cache = {}


def f(m, nmin, nmax):
    solutions = 1

    if nmin > m:
        return solutions

    if m in cache:
        return cache[m]

    for bs in range(nmin, nmax + 1):
        for startpos in range(0, m - bs + 1):
            solutions += f(m - startpos - bs, nmin, nmax)

    cache[m] = solutions
    return solutions


def main():
    print "The number of solutions are %d" % f(50, 2, 4)


if __name__ == "__main__":
    main()
