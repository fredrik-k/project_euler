#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 41: 
We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. For example, 2143 is a 
4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

ANSWER : 7652413
'''
from itertools import permutations

def is_prime(n) :
	for i in range(2, int(n ** 0.5)) :
		if n % i == 0 :
			return False
	return True
def precheck(n) :
	return (n[:-1] not in ['2', '4', '5', '6', '8'])

def main():
	max_prime = -1
	for i in range(2,10) :
		if sum(range(1,i+1)) % 3 == 0 :
			continue
		n = ''.join(map(lambda n : str(n), range(1,i + 1)))
		perms = [''.join(p) for p in permutations(n)]
		for p in perms : 
			if precheck(p) and is_prime(int(p)) :
				if int(p) > max_prime :
					max_prime = int(p)
	print "The largest pandigital prime is %d" % max_prime

if __name__ == "__main__":
    main()