#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 93:
By using each of the digits from the set, {1, 2, 3, 4},
exactly once, and making use of the four arithmetic
operations (+, −, *, /) and brackets/parentheses, it is
possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are
not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain
thirty-one different target numbers of which 36 is the
maximum, and each of the numbers 1 to 28 can be obtained
before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for
which the longest set of consecutive positive integers,
1 to n, can be obtained, giving your answer as a string: abcd.

ANSWER : 1258
'''
import itertools

def longestConsecutive(numbers) :
    l = map(lambda (a,b): b-a, zip(numbers[:-2], numbers[1:]))
    return max(sum(1 for _ in l) for n, l in itertools.groupby(l))


def numbers(n1, n2, n3, n4):
    n = {}
    for (a,b,c,d) in itertools.permutations([n1,n2,n3,n4]):
        for o1 in ['+', '-', '*', '/']:
            for o2 in ['+', '-', '*', '/']:
                for o3 in ['+', '-', '*', '/']:
                    n1 = "%f%s%f%s%f%s%f" % (a, o1, b, o2, c, o3, d)
                    n2 = "%f%s(%f%s%f)%s%f" % (a, o1, b, o2, c, o3, d)
                    n3 = "%f%s(%f%s%f%s%f)" % (a, o1, b, o2, c, o3, d)
                    n4 = "%f%s%f%s(%f%s%f)" % (a, o1, b, o2, c, o3, d)
                    n5 = "(%f%s%f)%s(%f%s%f)" % (a, o1, b, o2, c, o3, d)
                    n6 = "(%f%s%f)%s%f%s%f" % (a, o1, b, o2, c, o3, d)
                    n7 = "(%f%s%f%s%f)%s%f" % (a, o1, b, o2, c, o3, d)
                    try:
                        n[(eval(n1))] = 1
                    except ZeroDivisionError:
                        ""
                    try:
                        n[(eval(n2))] = 1
                    except ZeroDivisionError:
                        ""
                    try:
                        n[(eval(n3))] = 1
                    except ZeroDivisionError:
                        ""
                    try:
                        n[(eval(n4))] = 1
                    except ZeroDivisionError:
                        ""
                    try:
                        n[(eval(n5))] = 1
                    except ZeroDivisionError:
                        ""
                    try:
                        n[(eval(n6))] = 1
                    except ZeroDivisionError:
                        ""
                    try:
                        n[(eval(n7))] = 1
                    except ZeroDivisionError:
                        ""
    return filter(lambda k : k > 0 and k.is_integer(), sorted(list(n)))



def main():
    maxNums = []
    maxNumbers = -1
    for d in range(3, 10):
        for c in range(2, d):
            for b in range(1, c):
                for a in range(0, b):
                    n = longestConsecutive(numbers(float(a), float(b), float(c), float(d)))
                    if n > maxNumbers:
                        maxNumbers = n
                        maxNums = (a,b,c,d)

    print "The maximum length of consecutive integers is %d, and is obtained from" % maxNumbers, maxNums



if __name__ == "__main__":
    main()