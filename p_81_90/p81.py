#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 81: 

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."),
 a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right 
 by only moving right and down.

ANSWER : 427337
'''
smallest_map = {}
limit = 79

def find_smallest_sum(matrix, n,m) :
	if n == limit and m == limit : 
		return matrix[limit][limit]
	if (n,m) in smallest_map :
		return smallest_map[(n,m)]
	s = matrix[n][m]
	if n == limit : 
		s += sum(matrix[limit][m+1:])
		smallest_map[(n,m)] = s
		return s 
	if m == limit :
		s += sum(map(lambda l : l[limit], matrix[n+1:]))
		smallest_map[(n,m)] = s
		return s
	s_down = find_smallest_sum(matrix,n+1,m)
	s_right = find_smallest_sum(matrix,n,m+1)
	s += min(s_down, s_right)
	smallest_map[(n,m)] = s
	return s


def main():
	with open("data/p081_matrix.txt") as f: 
		matrix = f.readlines()
	matrix = map(lambda l : map(int,l.split('\n')[0].split(',')), matrix)
	print "The smallest sum is %d" % find_smallest_sum(matrix,0,0)

if __name__ == "__main__":
    main()