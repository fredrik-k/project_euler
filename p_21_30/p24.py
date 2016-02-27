#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 24: 
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The 
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 
6, 7, 8 and 9?

ANSWER : 
'''

all_possible = []

def create_all_possible(n, numbers) :
	if len(numbers) == 1 :
		all_possible.append(n * 10 + numbers[0])
	else :
		for i in numbers :
			new_numbers = filter(lambda x : x != i, numbers)
			create_all_possible(n * 10 + i, new_numbers)

def main():
	create_all_possible(0, range(0,10))
	print "The millonth lexicographic permutation is", all_possible[1000000 - 1]

if __name__ == "__main__":
	main()