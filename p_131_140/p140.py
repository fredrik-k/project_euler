#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 140:
Consider the infinite polynomial series AG(x) = xG1 + x2G2 + x3G3 + ..., where
Gk is the kth term of the second order recurrence relation Gk = Gk−1 + Gk−2,
G1 = 1 and G2 = 4; that is, 1, 4, 5, 9, 14, 23, ... .

For this problem we shall be concerned with values of x for which AG(x) is a
positive integer.

The corresponding values of x for the first five natural numbers are shown
below.

x               AG(x)
(√5−1)/4        1
2/5             2
(√22−2)/6       3
(√137−5)/14     4
1/2             5
We shall call AG(x) a golden nugget if x is rational, because they become
increasingly rarer; for example, the 20th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.

ANSWER : 5673835352990
'''

def main():
    init = [(0, -1),
            (0, 1),
            (-3, -2),
            (-3, 2),
            (-4, -5),
            (-4, 5),
            (2, 7),
            (2, -7)]
    nuggets =  []

    for (k, b) in init:
        for _ in range(0,30):
            knew = -9 * k + -4 * b + -14
            bnew = -20 * k + -9 * b + -28
            k = knew
            b = bnew

            if k > 0 and k not in nuggets:
                nuggets.append(k)
    nuggets.sort()
    print "The sum is %d" % sum(nuggets[:30])

if __name__ == "__main__":
    main()