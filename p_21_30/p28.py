#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 28: 
Starting with the number 1 and moving to the right in a 
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the 
diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 
by 1001 spiral formed in the same way?

ANSWER : 669171001
'''

def find_heading(heading, nbr_in_circle, circle_number) :
	if nbr_in_circle % (circle_number * 2) != 0 :
		return heading
	return (-heading[1], heading[0])

def create_spiral(size) : 
	spiral = []
	if size % 2 == 0 :
		return 0
	for i in range(0, size) :
		spiral.append(range(0,size))
	x = int(size/2)
	y = int(size/2)
	nbr_in_circle = 1
	i = 1
	circle_number = 0
	heading = (0,1)
	while i < size ** 2 :
		while True :
			spiral[y][x] = i
			i += 1
			nbr_in_circle -= 1
			if nbr_in_circle == 0 :
				break
			heading = find_heading(heading, nbr_in_circle, circle_number)
			x += heading[0]
			y += heading[1]
		circle_number += 1
		nbr_in_circle = 8 * circle_number 
		heading = (0,1)
		x += 1
	return spiral

def main():
    spiral = create_spiral(1001)
    s1 = sum(map(lambda x : spiral[x][x], range(0,1001)))
    s2 = sum(map(lambda x : spiral[1000 - x][x], range(0,1001)))

    s = s1 + s2 - 1 

    print "The sum of the diagonals is ", s

if __name__ == "__main__":
    main()