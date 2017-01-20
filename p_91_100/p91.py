#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 91:
There are exactly fourteen triangles containing a right angle
that can be formed when each co-ordinate lies between 0 and 2
inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.


Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles
can be formed?

ANSWER : 14234
'''

SIZE = 50

def gcd(a, b) :
    divisor = 1
    for n in range(2, min(a,b) + 1) :
        if a % n == 0 and b % n == 0 :
            divisor = n
    return divisor

def main():
    res = SIZE * SIZE * 3
    for x in range(1, SIZE + 1):
        for y in range(1, SIZE + 1):
            fact = gcd(x,y)
            res += min(y*fact/x, (SIZE - x) * fact /y) * 2

    print "The number of triangels is %d" % res
if __name__ == "__main__":
    main()