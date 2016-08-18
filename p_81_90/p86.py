#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 86: 
A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, 
F, sits in the opposite corner. By travelling on the surfaces of the room the shortest 
"straight line" distance from S to F is 10 and the path is shown on the diagram.

However, there are up to three "shortest" path candidates for any given cuboid and the 
shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with 
integer dimensions, up to a maximum size of M by M by M, for which the shortest route 
has integer length when M = 100. This is the least value of M for which the number of 
solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds one million.

ANSWER : 1818
'''

def find_shortest_path(a, b, c) : 
	return (a ** 2 + b ** 2 + c ** 2 + 2 * b * c) ** 0.5

def main():
	M = 1 
	count = 0
	while True : 
		a = M 
		for b in range(1, a + 1) : 
			for c in range(1, b + 1) : 
				dist = find_shortest_path(a, b, c)
				if dist.is_integer() : 
					count += 1
		if count > 10 ** 6 : 
			break
		M += 1 
	print "The value of M is %d" % M

if __name__ == "__main__":
	main()