#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 112:
Working from left-to-right if no digit is exceeded by the digit to its
left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just
over half of the numbers below one-thousand (525) are bouncy. In fact,
the least number for which the proportion of bouncy numbers first
reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the
time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is
exactly 99%.

ANSWER : 1587000
'''


def split(n):
    split = []
    while n > 0:
        split.insert(0, n % 10)
        n /= 10
    return split


def is_bouncy(l):
    decreasing = False
    increasing = False
    for i in range(1, len(l)):
        if l[i - 1] < l[i]:
            increasing = True
        if l[i - 1] > l[i]:
            decreasing = True
        if  decreasing and increasing:
            return True
    return False


def main():
    in_count = 0
    i = 1
    while True:
        if is_bouncy(split(i)):
            in_count += 1
        if 100 * in_count == i * 99:
            break
        i += 1
    print "The number is %d" % i


if __name__ == "__main__":
    main()
