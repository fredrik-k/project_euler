#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 104:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first
Fibonacci number for which the last nine digits are 1-9 pandigital
(contain all the digits 1 to 9, but not necessarily in order).
And F2749, which contains 575 digits, is the first Fibonacci number
for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine
digits AND the last nine digits are 1-9 pandigital, find k.

ANSWER : 329468
'''



pan = range(1,10)
tailcut = 1000000000

def is_pandigital(n):
    s = []
    for _ in range(0, 9):
        s.append(n%10)
        n /= 10
    return sorted(s) == pan


def main():
    f1 = 1
    f2 = 1
    k = 2
    while True:
        k += 1
        ft = (f1 + f2) % tailcut
        f1 = f2
        f2 = ft
        if is_pandigital(f2):
            t = (k * 0.20898764024997873 - 0.3494850021680094)
            if (is_pandigital(int(10.0 ** (t - int(t) + 8)))):
                break

    print ("The first Fibonacci number to have the descired"
           "properties is %d" % k)


if __name__ == "__main__":
    main()