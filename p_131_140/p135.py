#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 135:
Given the positive integers, x, y, and z, are consecutive terms of an
arithmetic progression, the least value of the positive integer, n, for which
the equation, x^2 − y^2 − z^2 = n, has exactly two solutions is n = 27:

34^2 − 27^2 − 20^2 = 12^2 − 9^2 − 6^2 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct
solutions?

ANSWER : 4989
'''

def main():
    n = 1000000
    ns = {}
    for u in range(1, n + 1):
        v = 1
        while u * v <= n:
            if ((u + v) % 4 == 0 and
                (3 * v)  > u and
                (3 * v - u) % 4 == 0):
                    if (u * v) not in ns:
                        ns[u * v] = 0
                    ns[u * v] += 1
            v += 1

    l = len(filter(lambda (k, v): v == 10, list(ns.iteritems())))
    print "The number of values is %d" % l

if __name__ == "__main__":
    main()