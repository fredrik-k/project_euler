#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 95:
The proper divisors of a number are all the divisors excluding
the number itself. For example, the proper divisors of 28 are
1, 2, 4, 7, and 14. As the sum of these divisors is equal to
28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and
the sum of the proper divisors of 284 is 220, forming a chain
of two numbers. For this reason, 220 and 284 are called an
amicable pair.

Perhaps less well known are longer chains. For example, starting
with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an
amicable chain.

Find the smallest member of the longest amicable chain with no
element exceeding one million.

ANSWER : 14316
'''

sum_of_factors = {}
numbers = {}


def generateFactors(limit):
    for i in range(1, limit / 2 + 1):
        for j in range(i * 2, limit, i):
            if j not in sum_of_factors:
                sum_of_factors[j] = 0
            sum_of_factors[j] += i


def is_amicable_chain(n):
    if n in numbers:
        return numbers[n]
    chain = []
    an = n
    amicable = False
    while an not in chain:
        chain.append(an)
        an = sum_of_factors[an]
        if an == n :
            amicable = True
            break
        if an > 1000000 or an == 1:
            amicable = False
            break
    for m in chain:
        numbers[n] = (amicable, chain)
    return amicable, chain


def main():
    max_len = 0
    m = 0
    generateFactors(1000000)
    for n in range(2, 1000000):
        amicable, chain = is_amicable_chain(n)
        if amicable and len(chain) > 0:
            if len(chain) > max_len:
                max_len = len(chain)
                m = min(chain)
    print "The smallest number in the longes chain is %d" % m


if __name__ == "__main__":
    main()