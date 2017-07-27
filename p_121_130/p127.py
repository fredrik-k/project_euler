#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 127:
The radical of n, rad(n), is the product of distinct prime factors of n. For
example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit
if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one
abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.

ANSWER : 18407904
'''

primes = [2]


def gen_primes(n):
    m = 3
    while m <= n:
        is_prime = True
        for p in primes:
            if m % p == 0:
                is_prime = False
                break
            if p ** 2 > m:
                break
        if is_prime:
            primes.append(m)
        m += 1


def unique_factors(n):
    factors = set()
    for p in primes:
        if n % p == 0:
            factors.add(p)
            n = n / p
        if p > n:
            break
    if n > 1 and n not in factors and n in primes:
        factors.add(n)
    return factors


def has_same_factor(a, b):
    return len(a) > len(a - b)


def prod(l):
    p = 1
    for n in l:
        p *= n
    return p


def main():
    s = 0
    factors = [(1, set([1]))]
    limit = 120000
    gen_primes(limit)
    for n in range(2, limit + 1):
        factors.append((n, unique_factors(n)))
    for (b, bf) in factors:
        for (a, af) in filter(lambda (n, nf): n < b and
                              not has_same_factor(bf, nf) and
                              n + b < limit, factors[:b]):
            c = a + b
            cf = factors[c - 1][1]
            if has_same_factor(af, cf) or has_same_factor(bf, cf):
                continue
            if prod(af) * prod(bf) * prod(cf) < c:
                s += c
    print "The su is %d" % s


if __name__ == "__main__":
    main()