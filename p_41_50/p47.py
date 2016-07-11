#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 47: 
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?

ANSWER : 
'''

primes = [2,3,5,7,11,13]

def unique_factors(n):  
	factors = []
	for p in primes : 
		if n % p == 0 :
			factors.append(p)
			n = n / p
		if p ** 2 > n :
			break
	if n > primes[-1] :
		primes.append(n)
	if n > 1 and n not in factors :
		factors.append(n)
	return factors   
    
def main():
	index = 13
	consecutives = 0
	not_found = True
	while not_found:
		index += 1
		f = unique_factors(index)
		if len(f) > 3 : 
			consecutives += 1
			if consecutives == 4 : 
				not_found = False
		else :
			consecutives = 0
	print "The number is %d" % (index - 3)
if __name__ == "__main__":
    main()