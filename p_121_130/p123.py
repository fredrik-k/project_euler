#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 123:
Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when
(pn−1)^n + (pn+1)n is divided by p_n^2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 1010.

ANSWER : 21035
'''

primes = [2]


def find_next_prime():
    n = primes[-1]
    while True:
        n += 1
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
            if p ** 2 > n:
                break
        if is_prime:
            primes.append(n)
            return n


def f(n, p):
    return ((p - 1) ** n + (p + 1) ** n) % (p ** 2)


def main():
    while find_next_prime() ** 2 < 5.5 * 10 ** 10:
        continue
    m = 0
    while True:
        m = f(len(primes), primes[-1])
        if m > 10 ** 10:
            break
        find_next_prime()
    print "The value of n is %d" % len(primes)


if __name__ == "__main__":
    main()
