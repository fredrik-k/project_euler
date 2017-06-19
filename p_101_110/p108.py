#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 108:
In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n
For n = 4 there are exactly three distinct solutions:

1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8 = 1/4
What is the least value of n for which the number of distinct solutions exceeds one-thousand?

ANSWER : 180180
'''

primes = {}
factor_map = {}


def find_primes(n):
    ps = []
    for i in range(2, n + 1):
        prime = True
        for p in ps:
            if i % p == 0:
                prime = False
                break
            if p ** 2 > i:
                break
        if prime:
            ps.append(i)
    for p in ps:
        primes[p] = True


def factorize(n, fmap):
    if n == 1:
        return
    if n in primes:
        if n not in fmap:
            fmap[n] = 0
        fmap[n] += 1
        return
    if n in factor_map:
        other = factor_map[n]
        for i in other:
            if i not in fmap:
                fmap[i] = 0
            fmap[i] += other[i]
        return
    for p in primes:
        if n % p == 0:
            if p not in fmap:
                fmap[p] = 0
            fmap[p] += 1
            factorize(n / p, fmap)
            break
    if n not in factor_map:
        factor_map[n] = fmap
    return


def find_number_of_solutions(fmap):
    solutions = 1
    for n in fmap:
        solutions *= (2 * fmap[n] + 1)
    return solutions


def main():
    find_primes(10**6)
    for i in range(2, 10**6):
        fmap = {}
        factorize(i, fmap)
        if (find_number_of_solutions(fmap) + 1) / 2 > 10000:
            print "The number is %d" % i
            break


if __name__ == "__main__":
    main()
