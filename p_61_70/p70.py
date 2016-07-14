#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 70: 
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal 
to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, 
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation 
of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the 
ratio n/φ(n) produces a minimum.

ANSWER : 8319823
'''

primes = []

def is_prime(n) :
	for p in primes :
		if p ** 2 > n : 
			break
		if n % p == 0 :
			return False
	primes.append(n)
	return True

def split(n) :
	if n == 0 : 
		return []
	l = split(n / 10)
	l.append(n % 10)
	return l

def is_permutation(n, m) :
	return sorted(split(n)) == sorted(split(m))

def main():
	best = 0
	min_ratio = 10**7
	for n in range(2, 5000) : 
		is_prime(n)
	candidates = filter(lambda p : p > 2000, primes)
	for i in range(0, len(candidates)) : 
		for j in range(i + 1, len(candidates)) : 
			n = candidates[i] * candidates[j]
			if n > 10 ** 7 : 
				break
			phi = (candidates[i] - 1) * (candidates[j] - 1)
			ratio = float(n) / float(phi)
			if is_permutation(n, phi) and ratio < min_ratio : 
				min_ratio = ratio
				best = n
	print "The value is %d" % best


if __name__ == "__main__":
    main()