#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM (X): 
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and 
each line adding to nine.


Working clockwise, and starting from the group of three with the numerically 
lowest external node (4,3,2 in this example), each solution can be described 
uniquely. For example, the above solution can be described by the set: 4,3,2; 
6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 
12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum 
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 
16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon 
ring?

ANSWER : 6531031914842725
'''
import itertools 

line_node_map = [[1,2,3], [4,3,5], [6,5,7], [8,7,9], [10,9,2]]

sum_map = [0,1,2,3,2,4,5,4,6,7,6,8,9,8,1]

def check_line(l) : 
	if 10 in [l[1], l[2], l[4], l[6], l[8]] :
		return False
	if l[0] > min([l[3], l[5], l[7], l[9]]) : 
		return False
	s = sum(l[0:3])
	if s != sum(l[2:5]) or s != sum(l[4:7]) or s != sum(l[6:9]) or s != l[8] + l[9] +  l[1] :
		return False
	return True

def main():
	max_sum = 0
	for itr in itertools.permutations([1,2,3,4,5,7,8,9,10]) :
		itr = list(itr) 
		itr.insert(0, 6)
		if check_line(itr) :
			s = int("".join(str(n) for n in map(lambda i: itr[i], sum_map)))
			if s > max_sum :
				max_sum = s
	print "The maximal is %d" % max_sum

if __name__ == "__main__":
    main()