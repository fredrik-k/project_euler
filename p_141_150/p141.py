#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 141:
A positive integer, n, is divided by d and the quotient and remainder are q
and r respectively. In addition d, q, and r are consecutive positive integer
terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be
seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio
3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 102^2, happen to also be
perfect squares.
The sum of all progressive perfect squares below one hundred thousand is
124657.

Find the sum of all progressive perfect squares below one trillion (10^12).

ANSWER : 878454337159
'''

def main():
    limit = 10**12
    l = []
    for a in xrange(2, 10001):
        for b in xrange(1, a):
            if a ** 3 * b + b ** 2 > limit:
                break
            c = 1
            while True:
                n = a ** 3 * b * c ** 2 + b ** 2 * c
                if n > limit:
                    break
                if (n ** 0.5).is_integer() and n not in l:
                    l.append(n)
                c += 1
    print "The sum is %d" % sum(l)




if __name__ == "__main__":
    main()