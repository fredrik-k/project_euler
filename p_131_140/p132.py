#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 132:
A number consisting entirely of ones is called a repunit. We shall define R(k)
to be a repunit of length k.

For example, R(10) = 1111111111 = 11×41×271×9091, and the sum of these prime
factors is 9414.

Find the sum of the first forty prime factors of R(109).

ANSWER : 843296
'''
import math

def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    if n < 25:
        return True
    m = 5
    while True:
        if m ** 2 > n:
            break
        if n % m == 0:
            return False
        if n % (m + 2) == 0:
            return False
        m += 6
    return True


def main():
    s = 0
    p = 2
    count = 0
    while count < 40:
        if isPrime(p):
            if pow(10, 10 ** 9, p * 9) == 1:
                count += 1
                s += p
        p += 1
    print "The sum is %d" % s


if __name__ == "__main__":
    main()