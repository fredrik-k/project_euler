#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 114:
A row measuring seven units in length has red blocks with a minimum
length of three units placed on it, such that any two red blocks
(which are allowed to be different lengths) are separated by at least
one black square. There are exactly seventeen ways of doing this.

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the
possibility, in general it is permitted to mix block sizes. For
example, on a row measuring eight units in length you could use red
(3), black (1), and red (4).

ANSWER : 16475640049
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
    print "The number of ways are %d" % f(50, 3)


if __name__ == "__main__":
    main()
