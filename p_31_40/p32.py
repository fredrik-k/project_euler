#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 32: 
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

ANSWER : 45228
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
    prods = []
    for a in range(2,100) :
    	beg = 123 if a > 9 else 1234
    	end = 10000 / a + 1 
    	for b in range(beg, end) :
    		if is_pandigital([a, b, a * b]) :
    			if a * b not in prods : 
    				prods.append(a * b)
    print '''The sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital is %d''' % sum(prods)


if __name__ == "__main__":
    main()