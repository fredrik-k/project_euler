#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 102:
Three distinct points are plotted at random on a Cartesian plane, for
which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas
triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'),
a 27K text file containing the co-ordinates of one thousand "random"
triangles, find the number of triangles for which the interior
contains the origin.

NOTE: The first two examples in the file represent the triangles in
the example given above.

ANSWER : 228
'''


def area(A, B, C):
    return abs((A[0] - C[0]) * (B[1] - A[1]) -
            (A[0] - B[0]) * (C[1] - A[1]))


def origin_in_triangle((A, B, C)):
    P = (0, 0)
    a1 = area(A, B, C)
    a2 = area(A, B, P)
    a3 = area(A, P, C)
    a4 = area(P, B, C)
    print a1, a2 + a3 + a4
    return a1 == (a2 + a3 + a4)

def string_to_triangel(s):
    s = s.strip('\n')
    coords = map(int, s.split(','))
    return ((coords[0], coords[1]), (coords[2], coords[3]),
            (coords[4], coords[5]))


def main():
    with open("data/p102.txt") as f:
        triangels = map(string_to_triangel, f.readlines())

    count = len(filter(origin_in_triangle, triangels))

    print "The number of triangels containing {0,0} is %d" % count

if __name__ == "__main__":
    main()