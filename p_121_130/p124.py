#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 124:
The radical of n, rad(n), is the product of the distinct prime factors of n.
For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting
on n if the radical values are equal, we get:

Unsorted        Sorted

n    rad(n)     n    rad(n)    k
1    1          1    1         1
2    2          2    2         2
3    3          4    2         3
4    2          8    2         4
5    5          3    3         5
6    6          9    3         6
7    7          5    5         7
8    2          6    6         8
9    3          7    7         9
10   10         10   10        10

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and
E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

ANSWER : 21417
'''

primes = [2]


def prod(l):
    p = 1
    for n in l:
        p *= n
    return p


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
    i = n
    factors = []
    for p in primes:
        if n % p == 0:
            factors.append(p)
            n = n / p
        if p > n:
            break
    if n > 1 and n not in factors and n in primes:
        factors.append(n)
    return (i, prod(factors))


def main():
    gen_primes(100000)
    E = map(unique_factors, range(1, 100001))
    E.sort(key=lambda (i, p): p)
    print "E(10000) is %d" % E[9999][0]


if __name__ == "__main__":
    main()
