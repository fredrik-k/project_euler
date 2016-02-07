#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 20: 
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

ANSWER : Fill in answer when solved
'''

def factorial(n) :
	factorial = 1 
	for i in range(1, n + 1) :
		factorial *= i
	return factorial

def main():
	s = 0
	number = factorial(100)
	while number > 0 :
		s  += number % 10
		number = int(number/10)
	print "The sum is", s

if __name__ == "__main__":
    main()