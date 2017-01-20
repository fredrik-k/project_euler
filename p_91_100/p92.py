#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 92:
A number chain is created by continuously adding the square of
the digits in a number to form a new number until it has been
seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck
in an endless loop. What is most amazing is that EVERY starting
number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

Answer:

ANSWER : 8581146
'''

end_map = {}

def to_sqr_digit_sum(n):
    digits = []
    while n > 0:
        digits.append((n % 10) ** 2)
        n /= 10
    return sum(digits)

def find_end_number(n):
    if n == 1 or n == 89:
        return n
    if n in end_map:
        return end_map[n]
    m = find_end_number(to_sqr_digit_sum(n))
    end_map[n] = m
    return m



def main():
    count = 0
    for n in range(1, 10**7):
        if n % 100000 == 0:
            print n
        if find_end_number(n) == 89:
            count += 1
    print "The count is %d" % count



if __name__ == "__main__":
    main()