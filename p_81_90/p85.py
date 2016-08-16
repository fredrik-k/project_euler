#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 85: 
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
contains eighteen rectangles

Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution.

ANSWER : 2772
'''

def compute_number_of_rectangles(length, heigth) : 
	count = 0
	for i in range(1, heigth + 1) :
		for k in range(1, length + 1) : 
			row_count = (length + 1) - k 
			height_count = (heigth + 1) - i 
			count += row_count * height_count
	return count

def main():
	min_diff = 2000000
	size = 0
	for length in range(1, 100) :
		for heigth in range(1, length + 1) :
			count = compute_number_of_rectangles(length, heigth)
			if abs(2000000 - count) < min_diff : 
				min_diff = abs(2000000 - count)
				size = length * heigth
	print "The size generating the count closest to 2 000 000 is %d" % size

if __name__ == "__main__":
	main()