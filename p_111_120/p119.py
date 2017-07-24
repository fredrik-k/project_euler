#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 119:
The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number
with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and insist that a
number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.

ANSWER : 248155780267521
'''


def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    return s


def main():
    a = []
    for i in range(2, 100):
        for j in range(1, 10):
            s = i ** j
            if s > 10 and digit_sum(s) == i:
                a.append(s)
    print "a30 is %d" % sorted(a)[29]


if __name__ == "__main__":
    main()
