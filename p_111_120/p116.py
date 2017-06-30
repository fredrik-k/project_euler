#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 115:
A row of five black square tiles is to have a number of its tiles
replaced with coloured oblong tiles chosen from red (length two),
green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

If green tiles are chosen there are three ways.

And if blue tiles are chosen there are two ways.

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways
of replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty
units in length be replaced if colours cannot be mixed and at least
one coloured tile must be used?

NOTE: This is related to Problem 117.

ANSWER : 20492570929
'''

cache = {}


def g(m, n):
    solutions = 0

    if n > m:
        return solutions

    if m in cache:
        return cache[m]

    for startpos in range(0, m - n + 1):
        solutions += 1
        solutions += g(m - startpos - n, n)

    cache[m] = solutions
    return solutions


def main():
    solutions = 0
    solutions += g(50, 2)
    cache.clear()
    solutions += g(50, 3)
    cache.clear()
    solutions += g(50, 4)
    print "The number of solutions are %d" % solutions


if __name__ == "__main__":
    main()
