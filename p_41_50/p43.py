#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 43: 
The number, 1406357289, is a 0 to 9 pandigital number because it 
is made up of each of the digits 0 to 9 in some order, but it also 
has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, 
we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

ANSWER : 16695334890
'''
from itertools import permutations

def main():
	s = 0
	primes = [2,3,5,7,11,13,17]
	n = ''.join(map(lambda n : str(n), range(0,10)))
	perms = [''.join(p) for p in permutations(n)]
	for p in perms :
		if p[3] not in ['0', '2', '4', '6', '8'] :
			continue
		if int(p[2:5]) % 3 != 0 :
			continue
		if p[5] not in ['0', '5'] : 
			continue
		if sum(map(lambda i : int(p[1+i:4+i]) % primes[i] 
			,range(3, len(primes)))) == 0 :
			s += int(p)
	print "The sum is %d" % s


if __name__ == "__main__":
    main()