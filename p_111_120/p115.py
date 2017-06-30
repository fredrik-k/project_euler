#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 115:
NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length
of m units placed on it, such that any two red blocks (which are
allowed to be different lengths) are separated by at least one black
square.

Let the fill-count function, F(m, n), represent the number of ways
that a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value
for which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that
F(10, 56) = 880711 and F(10, 57) = 1148904, so n = 57 is the least
value for which the fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count
function first exceeds one million.

ANSWER : 168
'''

cache = {}


def f(m, n):
    solutions = 1

    if n > m:
        return solutions

    if m in cache:
        return cache[m]

    for startpos in range(0, m - n + 1):
        for blocklength in range(n, m - startpos + 1):
            solutions += f(m - startpos - blocklength - 1, n)

    cache[m] = solutions
    return solutions


def main():
    m = 49
    while f(m, 50) < 10 ** 6:
        m += 1
    print "The smallest value of m is %d" % m


if __name__ == "__main__":
    main()
