#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 133:
A number consisting entirely of ones is called a repunit. We shall define R(k)
to be a repunit of length k; for example, R(6) = 111111.

Let us consider repunits of the form R(10n).

Although R(10), R(100), or R(1000) are not divisible by 17, R(10000) is
divisible by 17. Yet there is no value of n for which R(10n) will divide by
19. In fact, it is remarkable that 11, 17, 41, and 73 are the only four primes
below one-hundred that can be a factor of R(10n).

Find the sum of all the primes below one-hundred thousand that will never be a
factor of R(10n).

ANSWER : 453647705
'''
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
    while p < 10 ** 5:
        if isPrime(p):
            divisible = False
            for k in range(1, 100):
                if pow(10, 10 ** k, p * 9) == 1:
                    divisible = True
                    break
            if not divisible:
                s += p
        p += 1
    print "The sum is %d" % s

if __name__ == "__main__":
    main()