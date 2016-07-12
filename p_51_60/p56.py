#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 46: 
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is 
the maximum digital sum?

ANSWER : 972
'''

def dig_sum(n) :
	if n == 0 :
		return 0
	return n%10 + dig_sum(n/10) 

def main():
	max_sum = 0
	for a in range(2, 100) :
		for b in range(2,100) :
			s = dig_sum(a**b)
			if s > max_sum :
				max_sum = s

	print "The maximal sum is %d" % max_sum

if __name__ == "__main__":
    main()