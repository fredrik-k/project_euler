#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 40: 
An irrational decimal fraction is created by concatenating the positive 
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value 
of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

ANSWER : 120
'''

def split_number(n) :
	numbers = []
	s = int(n)
	while s > 0 : 
		numbers.insert(0, s % 10)
		s = s / 10
	return numbers

def main():
	counts = [1, 10, 100, 1000, 10000, 100000, 1000000]
	count = 0
	index = 0
	s = 1
	while True : 
		for n in split_number(index) : 
			count += 1
			if count in counts	:
				s *= n
		index += 1
		if count >= 1000000 :
			break
	print "The sum is %d" % s 

if __name__ == "__main__":
    main()