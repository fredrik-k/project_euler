#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 38: 
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
and 5, giving the pandigital, 918273645, which is the concatenated product 
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
the concatenated product of an integer with (1,2, ... , n) where n > 1?

ANSWER : 932718654
'''

def split_number(n) :
	numbers = []
	s = int(n)
	while s > 0 : 
		numbers.insert(0,s%10)
		s = s / 10
	return numbers

def is_pandigital(a) : 
	numbers = range(1,10)
	in_list = map(lambda n : split_number(n), a)
	in_list = [item for sublist in in_list for item in sublist]
	in_list.sort()
	return in_list == numbers

def main():
	largest_pandigital = -1
	for n in range(1, 9999) : 
		s = str(n)
		for i in range(2,9) :
			s = s + str(n * i)
			if len(s) > 9 :
				break
			if is_pandigital(s) :
				if int(s) > largest_pandigital : 
					largest_pandigital = int(s)
	print "Larges 9 digit pandigital number form from concatenated products is %d" % largest_pandigital

if __name__ == "__main__":
    main()