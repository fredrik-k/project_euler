#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 106:
Let S(A) represent the sum of elements in set A of size n. We shall
call it a special sum set if for any two non-empty disjoint subsets,
 and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For this problem we shall assume that a given set contains n strictly
increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained
from a set for which n = 4, only 1 of these pairs need to be tested
for equality (first rule). Similarly, when n = 7, only 70 out of the
966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained
need to be tested for equality?

NOTE: This problem is related to Problem 103 and Problem 105.

ANSWER : 21384
'''

import itertools


def generate_guess(seed):
    n = seed[len(seed)/2]
    guess = [n]
    for i in seed:
        guess.append(n + i)
    return guess


def all_disjoint_subsets(s):
    subsets = {}
    l = len(s) / 2 + 1 if len(s) % 2 == 0 else len(s) / 2 + 2
    for i in range(1, l):
        for s1 in itertools.combinations(s, i):
            s1 = tuple(sorted(s1))
            s2 = tuple(sorted(tuple(s - set(s1))))
            if (s1, s2) not in subsets and (s2, s1) not in subsets :
                subsets[(s1, s2)] = 1
            for k in range(1, len(s)):
                for s3 in itertools.combinations(s2, k):
                    s3 = tuple(sorted(s3))
                    if ((s1, s3) not in subsets and
                        (s3, s1) not in subsets) :
                        subsets[(s1, s3)] = 1
    return list(subsets.iterkeys())

def is_special_sum_set(s):
    set_map = {}
    subsets = all_disjoint_subsets(s)
    c = 0
    for (s1, s2) in subsets:
        if len(s1) == 1 and len(s2) == 1:
            continue
        if len(s1) == len(s2):
            diff = filter(lambda n: n,
                          map(lambda (a,b): a > b, zip(s1,s2)))
            if len(diff) == 0 or len(diff) == len(s1):
                continue
            c += 1
    return c


def main():
    seed = [1]
    for i in range(1, 12):
        seed = generate_guess(seed)
    s = is_special_sum_set(set(seed))
    print "The number of set pairs needs checking is %d" % s

if __name__ == "__main__":
    main()
