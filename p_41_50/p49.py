#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 49: 
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms 
increases by 3330, is unusual in two ways: (i) each of the three terms 
are prime, and, (ii) each of the 4-digit numbers are permutations of one
 another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit 
primes, exhibiting this property, but there is one other 4-digit increasing 
sequence.

What 12-digit number do you form by concatenating the three terms in this 
sequence?

ANSWER : 296962999629
'''

from itertools import permutations
from sets import Set

def is_prime(n) :
	for i in range(2,int(n ** 0.5)) :
		if n % i == 0 :
			return False
	return True

def main():
	for n in range(1000,10000) :
		perms = map(lambda s: int(s), [''.join(p) for p in permutations(str(n))])
		perms = filter(lambda i : i > 1000 and is_prime(i), perms)
		if len(perms) < 3 : 
			continue
		perms = list(Set(perms))
		perms.sort()
		d = list(map(lambda (a,b) : b - a,zip(perms, perms[1:])))
		if len(filter(lambda i : i == 3330, d)) == 2 :
			seq = ""
			for i in range(0, len(perms)-1) :
				if perms[i+1] - perms[i] == 3330 : 
					if str(perms[i]) in seq : 
						seq += str(perms[i])
					seq += str(perms[i+1])
			print "The number is %s" % (seq)
			break

if __name__ == "__main__":
	main()