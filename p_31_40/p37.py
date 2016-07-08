#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 37: 
The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, and remain prime at each stage: 
797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 
3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

ANSWER : 748317
'''

primes = [2,3,5,7]

def is_truncatable(n, itr) :
	if len(n) == itr and is_prime(int(n)):
		return True
	elif is_prime(int(n[itr:])) and is_prime(int(n[:-itr])) :
		return is_truncatable(n, itr + 1)
	else :
		return False

def is_prime(n) :
	if n == 1 :
		return False
	for p in primes : 
		if p ** 2 > n : 
			break 
		if n % p == 0 :
			return False
	primes.append(n)
	return True

def is_candidate(n) : 
	return n[0] not in ['1','9'] and n[-1] not in ['1', '9'] and not any(i in n[1:-1] for i in '02468')

def main():
	t_primes = []
	current = 11
	while len(t_primes) < 11 : 
		n = str(current)
		if is_prime(current) and is_candidate(n) :
			if is_truncatable(n, 1) :
				t_primes.append(current)
		current += 1
	print "The sum is %d" % sum(t_primes)

if __name__ == "__main__":
    main()