#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 130:
A number consisting entirely of ones is called a repunit. We shall define R(k)
to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that
there always exists a value, k, for which R(k) is divisible by n, and let A(n)
be the least such value of k; for example, A(7) = 6 and A(41) = 5.

You are given that for all primes, p > 5, that p − 1 is divisible by A(p). For
example, when p = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the
first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of n for which
GCD(n, 10) = 1 and n − 1 is divisible by A(n).
ANSWER : 149253
'''

def is_prime(n):
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
    count = 0
    s = 0
    n = 9

    while count < 25:
        if not is_prime(n) and n % 5 != 0:
            if (n - 1) % A(n) == 0:
                count += 1
                s += n
        n += 2
    print "The sum is %d" % s


if __name__ == "__main__":
    main()