#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 103:
Let S(A) represent the sum of elements in set A of size n. We shall
call it a special sum set if for any two non-empty disjoint subsets,
B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
If S(A) is minimised for a given n, we shall call it an optimum
special sum set. The first five optimum special sum sets are given
below.

n = 1: {1}
n = 2: {1, 2}
n = 3: {2, 3, 4}
n = 4: {3, 5, 6, 7}
n = 5: {6, 9, 11, 12, 13}

It seems that for a given optimum set, A = {a1, a2, ... , an}, the
next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where
b is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for n = 6 to
be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not
the optimum set, as we have merely applied an algorithm to provide a
near optimum set. The optimum set for n = 6 is
A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set
string: 111819202225.

Given that A is an optimum special sum set for n = 7, find its set
string.

NOTE: This problem is related to Problem 105 and Problem 106.

ANSWER : 103
'''

import itertools


def generate_guess(seed):
    n = seed[len(seed)/2]
    guess = [n]
    for i in seed:
        guess.append(n + i)
    return guess


def update_pertubation_vector(a) :
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 3:
            continue
        else :
            for j in range(i + 1, len(a)):
                a[j] = -3

            a[i] += 1
        return a
    return a


def is_special_sum_set(guess, pertubation):
    s = set(map(lambda (a,b): a + b, zip(guess, pertubation)))
    if len(filter(lambda n: n <= 0, s)) or len(s) < len(guess):
        return False
    subsets = []
    for i in range(1, len(s) / 2 + 1):
        for s1 in itertools.combinations(s, i):
            s2 = s - set(s1)
            subsets.append((s1, s2))
            for k in range(1, len(s2) + 1):
                for s3 in itertools.combinations(s2, k):
                    subsets.append((s1, s3))
    for (s1, s2) in subsets:
        if sum(s1) == sum(s2):
            return False
        if len(s1) > len(s2) and sum(s2) >= sum(s1):
            return False
        if len(s2) > len(s1) and sum(s1) >= sum(s2):
            return False
    return True


def main():
    seed = [1]
    for _ in range(1,7):
        seed = generate_guess(seed)
        per = []
        for _ in range(0, len(seed)):
            per.append(-3)
        m = 1000000000000000000000;
        s = []
        while True :
            su = sum(seed) + sum(per)
            if su > 0 and su < m:
                if is_special_sum_set(seed, per):
                    s = map(lambda (a,b): a + b, zip(seed, per))
                    m = su
            if sum(per) == 3 * len(per):
                break
            per = update_pertubation_vector(per)
        seed = s
    print "The set string is %s" % ''.join(str(x) for x in seed)



if __name__ == "__main__":
    main()
