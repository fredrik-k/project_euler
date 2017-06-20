#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 110:
In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n
For n = 4 there are exactly three distinct solutions:

1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8 = 1/4
What is the least value of n for which the number of distinct
solutions exceeds four million?

ANSWER : 9350130049860600
'''

primes = []

exponents = [0 for i in range(0, 14)]


def find_primes(n):
    for i in range(2, n + 1):
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False
                break
            if p ** 2 > i:
                break
        if prime:
            primes.append(i)


def twos(limit):
    exponents[0] = 0
    divisors = 1
    for i in range(0, len(exponents)):
        divisors *= 2 * exponents[i] + 1
    exponents[0] = int((limit / divisors - 1) / 2)
    while divisors * (2 * exponents[0] + 1) < limit:
        exponents[0] += 1


def find_number_of_solutions(exponents):
    solutions = 1
    for n in exponents:
        solutions *= (2 * n + 1)
    return solutions


def num(primes):
    number = 1
    for i in range(0, len(exponents)):
        number *= primes[i] ** exponents[i]
    return number


def set_smaller_exponents(counter):
    e = exponents[counter]
    for i in range(counter - 1, -1, -1):
        exponents[i] = e


def main():
    find_primes(45)
    result = 1
    for i in range(0, len(primes)):
        result *= primes[i]

    limit = 2 * 4000000 - 1
    counter = 1

    while True:
        twos(limit)
        if exponents[0] < exponents[1]:
            counter += 1
        else:
            number = num(primes)
            if (number < result):
                result = number
            counter = 1
        if counter >= len(exponents):
            break
        exponents[counter] += 1
        set_smaller_exponents(counter)
    print "The smnallest number is %d" % result


if __name__ == "__main__":
    main()
