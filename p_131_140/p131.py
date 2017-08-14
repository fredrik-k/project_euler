#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 131:
There are some prime values, p, for which there exists a positive integer, n,
such that the expression n^3 + n^2p is a perfect cube.

For example, when p = 19, 83 + 82×19 = 123.

What is perhaps most surprising is that for each prime with this property the
value of n is unique, and there are only four such primes below one-hundred.

How many primes below one million have this remarkable property?

ANSWER : 173

n^3(n + p) = m ^ 3

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
    count = 0
    for i in range(1, 578):
        if isPrime((i + 1) ** 3 - i ** 3):
            count += 1
    print "The count is %d" % count


if __name__ == "__main__":
    main()