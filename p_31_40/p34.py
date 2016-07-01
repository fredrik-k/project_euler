#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 34: 
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

ANSWER : 40730
'''

def split_number(n) :
	numbers = []
	s = int(n)
	while s > 0 : 
		numbers.insert(0,s%10)
		s = s / 10
	return numbers

def factorial(n) :
	if n == 0 :
		return 1
	return reduce(lambda x,y : x * y, range(1, n + 1)) 

def main():
    s = 0
    for i in range(3, factorial(9) * 8)  : 
    	factorial_sum = sum(map(lambda n : factorial(n), split_number(i)))
    	if factorial_sum == i : 
    		s += i
    print "The sum is %d" % s

if __name__ == "__main__":
    main()