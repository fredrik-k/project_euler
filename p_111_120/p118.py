#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 118:
Using all of the digits 1 through 9 and concatenating them freely to
form decimal integers, different sets can be formed. Interestingly
with the set {2,5,47,89,631}, all of the elements belonging to it are
prime.

How many distinct sets containing each of the digits one through nine
exactly once contain only prime elements?

ANSWER : 44680
'''

perm = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def nextPermuation():

    N = len(perm)
    i = N - 1

    while perm[i - 1] >= perm[i]:
        i = i - 1
        if i == 0:
            return False

    j = N
    while perm[j - 1] <= perm[i - 1]:
        j = j - 1

    swap(i - 1, j - 1)
    i += 1
    j = N

    while i < j:
        swap(i - 1, j - 1)
        i += 1
        j -= 1

    return True


def swap(i, j):
    k = perm[i]
    perm[i] = perm[j]
    perm[j] = k


def CheckPartitions(startIndex, prev):
    count = 0
    for i in range(startIndex, len(perm)):
        number = 0
        for j in range(startIndex, i + 1):
            number = number * 10 + perm[j]

        if number < prev:
            continue

        if not IsPrime(number):
            continue

        if i == (len(perm) - 1):
            return count + 1

        count += CheckPartitions(i + 1, number)

    return count


def IsPrime(n):
    if (n < 2):
        return False
    if (n < 4):
        return True
    if (n % 2 == 0):
        return False
    if (n < 9):
        return True
    if (n % 3 == 0):
        return False
    if (n < 25):
        return True

    s = int(n ** 0.5)
    for i in range(5, s + 1, 6):
        if (n % i == 0):
            return False
        if (n % (i + 2) == 0):
            return False

    return True


def main():
    count = 0

    count += CheckPartitions(0, 0)
    while nextPermuation():
        count += CheckPartitions(0, 0)
    print "There are %d sets" % count


if __name__ == "__main__":
    main()
