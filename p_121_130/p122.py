#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 122:
The most naive way of computing n^15 requires fourteen multiplications:

n × n × ... × n = n^15

But using a "binary" method you can compute it in six multiplications:

n × n = n^2
n^2 × n^2 = n^4
n^4 × n^4 = n^8
n^8 × n^4 = n^12
n^12 × n^2 = n^14
n^14 × n = n^15

However it is yet possible to compute it in only five multiplications:

n × n = n^2
n^2 × n = n^3
n^3 × n^3 = n^6
n^6 × n^6 = n^12
n^12 × n^3 = n^15

We shall define m(k) to be the minimum number of multiplications to compute
n^k; for example m(15) = 5.

For 1 ≤ k ≤ 200, find ∑ m(k).

ANSWER : 1852
'''

paths = [(1, (1,))]


def shortest(n):
    possible = []
    for (m, path) in paths:
        if n - m in path:
            possible.append(path + (n,))
    possible.sort(key=lambda path: len(path))
    i = 0
    while i < len(possible) and len(possible[i]) == len(possible[0]):
        paths.append((n, possible[i]))
        i += 1

    return (len(possible[0]) - 1, possible[0])


def main():
    s = 0
    for i in range(2, 201):
        (m, path) = shortest(i)
        s += m
    print " ∑ m(k) = %d" % s


if __name__ == "__main__":
    main()
