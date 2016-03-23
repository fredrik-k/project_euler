#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM (X): 
Surprisingly there are only three numbers that can be
written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as 
the sum of fifth powers of their digits.

ANSWER : Fill in answer when solved
'''

def fith_power_sum(n) :
	s = 0
	while n > 0:
		s += (n % 10) ** 5
		n = int(n / 10)
	return s

def main():
	numbers = []
	for i in range(2, 10 ** 6) :
		if i == fith_power_sum(i) :
			numbers.append(i)
	print "The sum is", sum(numbers)


if __name__ == "__main__":
    main()