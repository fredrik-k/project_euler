#!/usr/bin/env python
# -*- coding: utf-8 -*-
''''
PROBLEM 14: 
Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

ANSWER : 137846528820
'''

mapping = {}

def move(right, down):
	if mapping.get(str(right) + "," + str(down), -1) != -1 :
		return mapping[str(right) + "," + str(down)]
	if right == 20 or down == 20 : 
		return 1 
	else :
		s = move(right + 1, down) + move(right, down + 1)
		mapping[str(right) + "," + str(down)] = s
		return s

def main():

    print "The number of routes is" , move(0,0)

if __name__ == "__main__":
    main()