#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 97:
The first known prime found to exceed one million digits was
discovered in 1999, and is a Mersenne prime of the form 26972593−1; it
contains exactly 2,098,960 digits. Subsequently other Mersenne primes,
of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which
contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.


ANSWER : 8739992577
'''


def last_ten(n):
    return n % 10 ** 10


def main():
    n = 1
    for _ in range(1, 7830458):
        n = last_ten(n * 2)
    n = last_ten(n * 28433 + 1)
    print "The last ten digit are %d" % n


if __name__ == "__main__":
    main()
