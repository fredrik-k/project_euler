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

As n increases, the proportion of bouncy numbers below n increases
such that there are only 12951 numbers below one-million that are not
bouncy and only 277032 non-bouncy numbers below 10^10.

How many numbers below a googol (10^100) are not bouncy?

ANSWER : 51161058134250
'''
import math


def ncr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


def main():
    print "The number is %d" % (ncr(110, 10) + ncr(109, 9) - 2 - 1000)


if __name__ == "__main__":
    main()
