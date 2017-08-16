#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 139:
Let (a, b, c) represent the three sides of a right angle triangle with
integral length sides. It is possible to place four such triangles together to
form a square with length c.

For example, (3, 4, 5) triangles can be placed together to form a 5 by 5
square with a 1 by 1 hole in the middle and it can be seen that the 5 by 5
square can be tiled with twenty-five 1 by 1 squares.


However, if (5, 12, 13) triangles were used then the hole would measure 7 by
7 and these could not be used to tile the 13 by 13 square.

Given that the perimeter of the right triangle is less than one-hundred
million, how many Pythagorean triangles would allow such a tiling to take
place?

ANSWER : 10057761

'''

import numpy as np

def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
            for (a,b,c) in m:
                if a + b + c < limit:
                    if c % (b - a) == 0:
                        yield 10 ** 8 / (a + b + c)
        m = np.dot(m, uad)

def main():
    print ("The number of pythagorean triangles are %s" %
        sum(list(gen_prim_pyth_trips(10**8))))


if __name__ == "__main__":
    main()