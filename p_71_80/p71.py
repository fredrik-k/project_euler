#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 70: 

Consider the fraction, n/d, where n and d are positive integers. If n<d and 
HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order 
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending 
order of size, find the numerator of the fraction immediately to the left of 3/7.

ANSWER : 428570
'''

def main():
	a = 3
	b = 7
	r = 0
	s = 1
	for q in range(10**6 + 1, 2, -1) :
		p = (a * q - 1) / b
		if p * s > r * q :
			s = q 
			r = p
	print "The numerator is %d" % r

if __name__ == "__main__":
    main()