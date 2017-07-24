#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 120:
Let r be the remainder when (a−1)^n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And
as n varies, so too will r, but for a = 7 it turns out that r_max = 42.

For 3 ≤ a ≤ 1000, find ∑ r_max.

ANSWER : 333082500
'''


def r(a, n):
    return ((a - 1) ** n + (a + 1) ** n) % (a ** 2)


def main():
    rmax = 0
    for a in range(3, 1001):
        rmax += 2 * a * ((a - 1) / 2)
    print "The sum is %d" % rmax


if __name__ == "__main__":
    main()
