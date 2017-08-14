#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 129:
A number consisting entirely of ones is called a repunit. We shall define R(k)
to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that
there always exists a value, k, for which R(k) is divisible by n, and let A(n)
be the least such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.

ANSWER : 1000023
'''

def A(n) :
    if n % 5 == 0:
        return 1

    x = 1
    k = 1

    while x != 0 :
        x = (x * 10 + 1) % n
        k += 1
    return k


def main():
    limit = 10 ** 6 + 1
    n = limit
    while A(n) < limit:
        n += 2
    print "The smallest value of A(n) is %d" % n

if __name__ == "__main__":
    main()