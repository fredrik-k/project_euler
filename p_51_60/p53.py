#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 53: 
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, 
are greater than one-million?

ANSWER : 4075
'''

import itertools

def factorial(n) :
	if n == 1 :
		return 1
	else :
		return n * factorial(n-1)

def nCr(n, r) :
	return factorial(n) / factorial(r) / factorial(n-r)

def main():
	count = 0
	for n in range(23, 101) : 
		for r in range(1, n ) :
			if nCr(n, r) > 10 ** 6 : 
				count += 1
	print "The count is %d" % count

if __name__ == "__main__":
	main()