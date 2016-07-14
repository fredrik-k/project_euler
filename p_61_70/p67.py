#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 67: 
By starting at the top of the triangle below and moving to adjacent numbers on the 
row below, the maximum total from top to bottom is 23.

			3
		   7 4
		  2 4 6
		 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 
'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred 
rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try 
every route to solve this problem, as there are 299 altogether! If you could check 
one trillion (1012) routes every second it would take over twenty billion years to 
check them all. There is an efficient algorithm to solve it. ;o)

ANSWER : 7273
'''

mapping = {}

def findMaxPath(row, collumn, triangle):
	if str(row) + "," + str(collumn) in mapping :
		return mapping[str(row) + "," + str(collumn)]
	if row is len(triangle) - 1 :
		return triangle[row][collumn]
	else :
		m1 = triangle[row][collumn] + findMaxPath(row + 1, collumn, triangle) 
		m2 = triangle[row][collumn] + findMaxPath(row + 1, collumn + 1, triangle)
		if m1 > m2 :
			mapping[str(row) + "," + str(collumn)] = m1 
			return m1 
		else :
			mapping[str(row) + "," + str(collumn)] = m2
			return m2

def main():
	triangle = []
	with open('data/p067_triangle.txt', 'rb') as f:
		for line in f.readlines() :
			triangle.append(map(int, line.split('\n')[0].split(' ')))
	print "The maximal sum is %d" % findMaxPath(0,0,triangle)

if __name__ == "__main__":
    main()