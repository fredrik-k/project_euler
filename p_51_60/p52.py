#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 52: 
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, 
and 6x, contain the same digits.

ANSWER : 142857
'''

def split_number(n) :
	numbers = []
	while n > 0 : 
		numbers.insert(0, n % 10)
		n = n / 10
	return numbers

def check_digits(n) :
	s = sorted(split_number(n))
	for i in range(2,6) : 
		if s != sorted(split_number(i * n)) :
			return False
	return True

def main():
	n = 1 
	while True :
		if check_digits(n) :
			break
		n += 1
	print "The number is %d" % n

if __name__ == "__main__":
    main()