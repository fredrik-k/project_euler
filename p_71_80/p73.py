#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 73: 
Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order 
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper 
fractions for d ≤ 12,000?

ANSWER : 7295372
'''
primes = [2, 3]

def is_prime(n) :
	for p in primes :
		if p ** 2 > n :
			break
		if n % p == 0 :
			return False
	primes.append(n)
	return True

def find_divs(n) :
	divs = []
	for p in primes :
		if p > n :
			return divs
		if n % p == 0 :
			divs.append(p)
			n /= p
	return divs

def main():
	count = 0
	for d in range(5, 12001) :
		divs = []
		if not is_prime(d) :
			divs = find_divs(d)
		for n in range(d / 3, d / 2) :
			if len(filter(lambda d : n % d == 0, divs)) == 0 :
				count += 1 
	print "The number of fractions are %d" % count
			


if __name__ == "__main__":
    main()