#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 60: 
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two 
primes and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of 
these four primes, 792, represents the lowest sum for a set of four primes 
with this property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.

ANSWER : 
'''
import itertools 
import sys

primes = [2,3,5,7]
prime_pairs = {}

def is_concatenated_prime(p1, p2) :
	if not is_prime(int(str(p1) + str(p2))) :
		return False
	if not is_prime(int(str(p2) + str(p1))) :
		return False
	return True

def is_prime(n) :
	for p in primes :
		if p ** 2 > n :
			break
		if n % p == 0 :
			return False
	for i in range(primes[-1] + 2, int(n ** 0.5) + 1, 2) :
		if n % i == 0 :
			return False
	return True

def create_pairs(a) :
	l = []
	for b in range(a+1, len(primes)) :
		if is_concatenated_prime(primes[a], primes[b]) :
			 l.append(b)
	prime_pairs[a] = l

def main():
	for n in range(11, 30000, 2) :
		if is_prime(n) : 
			primes.append(n)
	result = sys.maxint
	for a in range(1, len(primes)) :
		if primes[a] * 5 > result :
			break
		if a not in prime_pairs :
			create_pairs(a)
		for b in prime_pairs[a] :
			if primes[a] + 4 * primes[b] > result :
				break
			if b not in prime_pairs :
				create_pairs(b)
			for c in prime_pairs[b] :
				if primes[a] + primes[b] + 3 * primes[c] > result : 
					break
				if c not in prime_pairs[a] : 
					continue
				if c not in prime_pairs :
					create_pairs(c)
				for d in prime_pairs[c] :
					if primes[a] + primes[b] + primes[c] + 2 * primes[d] > result : 
						break
					if d not in prime_pairs[a] or d not in prime_pairs[b] : 
						continue
					if d not in prime_pairs :
						create_pairs(d)
					for e in prime_pairs[d] :
						if (primes[a] + primes[b] + primes[c] + primes[d] + 
							primes[e] > result) : 
							break
						if (e not in prime_pairs[a] or e not in prime_pairs[b] 
							or e not in prime_pairs[c]) : 
							continue
						if e not in prime_pairs :
							create_pairs(e)
						if result > primes[a] + primes[b] + primes[c] + primes[d] + primes[e] :
							result = primes[a] + primes[b] + primes[c] + primes[d] + primes[e]
							break
	print "The sum of the primes are %d" % result

if __name__ == "__main__":
	main()