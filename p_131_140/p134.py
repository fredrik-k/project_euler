#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 134:
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
1219 is the smallest number such that the last digits are formed by p1 whilst
also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of
consecutive primes, p2 > p1, there exist values of n for which the last digits
are formed by p1 and n is divisible by p2. Let S be the smallest of these
values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

ANSWER : 18613426663617118
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
        m += 2

def DigitCountFactor(number):
    factor = 1

    while number > 0:
        factor *= 10
        number /= 10

    return factor

def extended_gcd(a, b):
    x = 0
    lastx = 1
    y = 1
    lasty = 0
    while (b != 0):
        quotient = a / b

        temp = b
        b = a % b
        a = temp

        temp = x
        x = lastx - quotient * x
        lastx = temp

        temp = y
        y = lasty - quotient * y
        lasty = temp

    return (lastx, lasty, a)


def main():
    limit = 1000000
    gen_primes(limit + 100)
    result = 0
    i = 0
    global primes
    primes = primes[2:]

    while primes[i] <= limit:
        p1 = primes[i]
        p2 = primes[i + 1]

        a = DigitCountFactor(p1)
        b = p2 - p1
        n = p2

        rs = extended_gcd(a, n)
        x  = rs[0] * b % n

        if (x < 0):
            x = n + x

        result += x * a + p1
        i += 1
    print "The sum is %d" % result

if __name__ == "__main__":
    main()
