#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 51: 
By replacing the 1st digit of the 2-digit number *3, it turns out that 
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 
5-digit number is the first example having seven primes among the ten 
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 
56773, and 56993. Consequently 56003, being the first member of this family, 
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number 
(not necessarily adjacent digits) with the same digit, is part of an eight 
prime value family.

ANSWER : 121313
'''
from itertools import *
from sets import Set

def is_prime(n) :
	if n % 2 == 0 :
		return False
	for i in range(3, int(n ** 0.5) + 1, 2) :
		if n % i == 0 :
			return False
	return True

def swap(s, c, n) : 
	l = list(s)
	for i in c : 
		l[i] = n
	return int(''.join(str(i) for i in l))

def substitute(n) :
	subs = []
	s = str(n)
	l = len(s)
	for i in range(3,l) : 
		for c in combinations(range(0,l), i) :
			nbrs = list(Set(map(lambda i: s[i], c)))
			if len(nbrs) > 1 :
				continue
			perms = []
			for k in range(0, 10) :
				if k == 0 and 0 in c : 
					continue
				perms.append(swap(s,c,k))
			subs.append(perms)
	return subs

def main():
	n = 9
	while True :
		n += 1
		if not is_prime(n) : 
			continue
		subs = substitute(n)
		if 8 in map(lambda s : len(filter(is_prime, s)),subs) :
			break
	print "The prime is %d" % n

if __name__ == "__main__":
    main()