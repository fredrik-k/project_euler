#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 39: 
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

ANSWER : 840
'''
import math 
def number_of_triangles(n) :
	num = 0 
	for a in range(1,n / 2) :
		for b in range(a + 1, n / 2) : 
			c = (a**2 + b**2) ** 0.5
			if a + b + c > n :
				break
			if math.ceil(c) == c and a + b + c == n:
				num += 1
				print n, " : ", a, b, c 
	return num

def main():
	max_triangels = 0
	max_number = 0
	for n in range(3, 1000) : 
		triangles =  number_of_triangles(n)
		if triangles > max_triangels :
			max_triangels = triangles
			max_number = n
	print "The solution is maximised for n=%d" % max_number

if __name__ == "__main__":
    main()