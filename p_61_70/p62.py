#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 62: 
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (4053). In fact, 41063625 is the smallest 
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits 
are cube.

ANSWER : Fill in answer when solved
'''

from itertools import permutations
from sets import Set

cubes = []

def makeLargestPerm(n) :
	k = n
	digits = [0,0,0,0,0,0,0,0,0,0]
	retVal = 0
 
	while (k > 0) :
		digits[k % 10] += 1
		k /= 10
 
	for i in range(9, -1, -1) :
		for j in range(0, digits[i]) :
			retVal = retVal * 10 + i
	return retVal;

def main():
	n = 11
	cubes = {}
	while True : 
		max_perm = makeLargestPerm(n**3)
		if max_perm not in cubes : 
			cubes[max_perm] = (n,0)
		cube = cubes[max_perm]
		cubes[max_perm] = (cube[0], cube[1] + 1)
		if cubes[max_perm][1] == 5 :
			print "The smalest cube is %d" % cubes[max_perm][0] ** 3
			break
		n += 1
	

if __name__ == "__main__":
    main()