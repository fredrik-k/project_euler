#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 105:
Let S(A) represent the sum of elements in set A of size n. We shall
call it a special sum set if for any two non-empty disjoint subsets,
B and C, the following properties are true:

S(B) ≠ S(C); that is, sums of subsets cannot be equal.
If B contains more elements than C then S(B) > S(C).
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set
because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79,
159, 161, 139, 158} satisfies both rules for all possible subset pair
combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text
file with one-hundred sets containing seven to twelve elements (the
two examples given above are the first two sets in the file), identify
all the special sum sets, A1, A2, ..., Ak, and find the value of
S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to Problem 103 and Problem 106.

ANSWER : 73702
'''
import itertools


def is_special_sum_set(s):
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
    with open("data/p105.txt") as f:
        candidates = map(set,
                     map(lambda s: map(int, s.strip('\n').split(',')),
                         f.readlines()))
    s = 0
    for c in candidates:
        if is_special_sum_set(c):
            s += sum(c)

    print "The sum is %d" % s

if __name__ == "__main__":
    main()
