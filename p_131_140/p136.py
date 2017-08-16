#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 136:
The positive integers, x, y, and z, are consecutive terms of an arithmetic
progression. Given that n is a positive integer, the equation,
x2 − y2 − z2 = n, has exactly one solution when n = 20:

132 − 102 − 72 = 20

In fact there are twenty-five values of n below one hundred for which the
equation has a unique solution.

How many values of n less than fifty million have exactly one solution?

ANSWER : 2544559
'''

def main():
    n = 50000000
    ns = {}
    u = 1
    while u <= n:
        v = 1
        while u * v <= n:
            if ((u + v) % 4 == 0 and
                (3 * v)  > u and
                (3 * v - u) % 4 == 0):
                    if (u * v) not in ns:
                        ns[u * v] = 0
                    ns[u * v] += 1
            v += 1
        u += 1

    l = len(filter(lambda (k, v): v == 1, list(ns.iteritems())))
    print "The number of values is %d" % l

if __name__ == "__main__":
    main()