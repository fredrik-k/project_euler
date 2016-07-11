#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 46: 
It was proposed by Christian Goldbach that every odd composite 
number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the 
sum of a prime and twice a square?

ANSWER : 5777
'''

primes = [2,3,5,7,]

def is_prime(n) :
	for p in primes :
		if n % p == 0 :
			return False
		if p ** 0.5 > n :
			break
	primes.append(n) 
	return True

def is_goldbach(n) : 
	for p in primes :
		s = ((n - p) / 2.0) ** 0.5
		if s == int(s) :
			return True
	return False

def main():
	n = 9 
	while True :
		if not is_prime(n) and not is_goldbach(n) :
			break
		n += 2
	print "The number is %d " % n

if __name__ == "__main__":
    main()