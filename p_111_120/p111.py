#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 111:
Considering 4-digit primes containing repeated digits it is clear that
they cannot all be the same: 1111 is divisible by 11, 2222 is
divisible by 22, and so on. But there are nine 4-digit primes
containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated
digits for an n-digit prime where d is the repeated digit, N(n, d)
represents the number of such primes, and S(n, d) represents the sum
of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit
prime where one is the repeated digit, there are N(4, 1) = 9 such
primes, and the sum of these primes is S(4, 1) = 22275. It turns out
that for d = 0, it is only possible to have M(4, 0) = 2 repeated
digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d    M(4, d) N(4, d) S(4, d)
0           2       13      67061
1           3       9       22275
2           3       1       2221
3           3       12      46214
4           3       2       8888
5           3       1       5557
6           3       1       6661
7           3       9       57863
8           3       1       8887
9           3       7       48073
For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).

ANSWER : 612407567715
'''

import itertools

primes = [2]

zero_to_nine = range(0, 10)


def find_primes(n):
    for i in range(3, n + 1, 2):
        if is_prime(i):
            primes.append(i)


def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
        if p ** 2 > n:
            return True
    return True


def to_num(l):
    n = 0
    for i in l:
        n *= 10
        n += i
    return n


class unique_element:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences


def perm_unique(elements):
    eset = set(elements)
    listunique = [unique_element(i, elements.count(i)) for i in eset]
    u = len(elements)
    return perm_unique_helper(listunique, [0] * u, u - 1)


def perm_unique_helper(listunique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d] = i.value
                i.occurrences -= 1
                for g in (perm_unique_helper(listunique,
                                             result_list, d - 1)):
                    yield g
                i.occurrences += 1


def max_repeat_digits(d):
    other = filter(lambda n: n != d, zero_to_nine)
    for i in range(9, 0, -1):
        repeat = [d for i in range(0, i)]
        found_primes = []
        for o in itertools.combinations_with_replacement(other, 9 - i):
            tot = []
            tot.extend(repeat)
            tot.extend(o)
            for comb in perm_unique(tot):
                if comb[0] == 0:
                    continue
                if comb[-1] % 2 == 0:
                    continue
                if is_prime(to_num(comb)):
                    found_primes.append(to_num(comb))
        if len(found_primes) > 0:
            return sum(found_primes)


def main():
    find_primes(int((10**11)**0.5))
    s_10 = sum(map(max_repeat_digits, range(0,10)))
    print "S(10,d) = %d" % s_10

if __name__ == "__main__":
    main()
