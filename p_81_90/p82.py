#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 82: 
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left 
column and finishing in any cell in the right column, and only moving up, down, and 
right, is indicated in red and bold; the sum is equal to 994.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), 
a 31K text file containing a 80 by 80 matrix, from the left column to the right column.

ANSWER : 260324
'''

smallest_map = {}
limit = 79

def find_smallest_sum(matrix, n,m, heading = None) :
	if m == limit : 
		return matrix[n][limit]
	if (n,m, heading) in smallest_map :
		return smallest_map[(n,m, heading)]
	s = matrix[n][m]
	s_right = find_smallest_sum(matrix,n,m+1)
	s_down = s_right
	s_up = s_right
	if n < limit and heading != "up": 
		s_down = find_smallest_sum(matrix,n+1,m, "down")
	if n > 0 and heading != "down":
		s_up = find_smallest_sum(matrix,n-1,m, "up")
	s += min([s_down, s_right, s_up])
	smallest_map[(n,m,heading)] = s
	return s

def main() :
	with open("data/p082_matrix.txt") as f: 
		matrix = f.readlines()
	matrix = map(lambda l : map(int,l.split('\n')[0].split(',')), matrix)
	
	min_s = find_smallest_sum(matrix, 0, 0)
	for i in range(1,limit + 1) :
		smallest_map = {}
		s = find_smallest_sum(matrix, i, 0)
		if s < min_s :
			min_s = s
	print "The smallest sum is %d" % min_s

if __name__ == "__main__":
    main()