#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 50: 
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime 
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds 
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?

ANSWER : 997651
'''

primes = [2,3,5,7]
cum_sum = [2,5,10,17]

def is_prime(n) :
	for p in primes :
		if p ** 2 > n :
			break 
		if n % p == 0 :
			return False
	for i in range(primes[-1], int(n ** 0.5)) :
		if n % p : 
			return False
	primes.append(n)
	cum_sum.append(cum_sum[-1] + n)
	return True

def find_longest() :
	n_primes = 0
	res = 0
	for i in range(n_primes, len(cum_sum)) : 
		for k in range(i - n_primes - 1, 0, -1) : 
			if cum_sum[i] - cum_sum[k] > 10 ** 6 :
				break
			if cum_sum[i] - cum_sum[k] in primes : 
				n_primes = i - k
				res = cum_sum[i] - cum_sum[k]
	return res

def main():
	max_sum = 0
	prime = 0
	for n in range(9, 10**6, 2) :
		is_prime(n)
	l = find_longest()
	print "The prime is %d" % l

if __name__ == "__main__":
	main()