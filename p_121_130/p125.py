#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 125:
The palindromic number 595 is interesting because it can be written as the sum
of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as
consecutive square sums, and the sum of these palindromes is 4164. Note that
1 = 0^2 + 1^2 has not been included as this problem is concerned with the
squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and
can be written as the sum of consecutive squares.

ANSWER : 2906969179
'''
pal_sqares = []


def is_palindrome(n):
    num = n
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num / 10
    return n == rev


def main():
    limit = 10 ** 8
    sqrLimit = int(limit ** 0.5)
    pal_sum = 0
    for i in range(1, sqrLimit + 1):
        s = i ** 2
        for j in range(i + 1, sqrLimit + 1):
            s += j ** 2
            if s >= limit:
                break
            if is_palindrome(s) and s not in pal_sqares:
                pal_sum += s
                pal_sqares.append(s)
    print "The sum off palindromes is %d" % pal_sum


if __name__ == "__main__":
    main()
