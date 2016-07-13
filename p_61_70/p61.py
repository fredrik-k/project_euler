#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 61: 
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers 
are all figurate (polygonal) numbers and are generated by the following 
formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 		P4,n=n2	 			1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting
properties.

The set is cyclic, in that the last two digits of each number is the first two 
digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal 
(P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each
polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and 
octagonal, is represented by a different number in the set.

ANSWER 28684:
'''

def is_trinagle(n) : 
	k = 1.0 / 2.0 * ((8.0 * n + 1.0) ** 0.5 - 1.0)
	return k == int(k)

def is_square(n) :
	k = n ** 0.5
	return k == int(k)

def is_pentagonal(n) :
	k = 1.0 / 6.0 * ((24.0 * n + 1.0) ** 0.5 + 1.0)
	return k == int(k)

def is_hexagonal(n) :
	k = 1.0/4.0 * ((8.0 * n + 1.0) ** 0.5 + 1.0)
	return k == int(k)

def is_heptagonal(n) :
	k = 1.0/10.0 * ((40.0 * n + 9.0) ** 0.5 + 3.0)
	return k == int(k)

def is_octagonal(n) :
	k = 1.0/3.0 * ((3.0 * n + 1.0) ** 0.5 + 1.0)
	return k == int(k)

def potential_cycles(keys, xagonal_map, last) :
	new = []
	for key in keys : 
		for num in xagonal_map[key] :
			if num / 100 == last : 
				new.append((num,key))
	return new 


def find_cycle(keys, xagonal_map, cycle, last) : 
	if len(keys) == 0 :
		return cycle
	pot = potential_cycles(keys, xagonal_map, last)
	for p in pot :
		if p[0] in cycle :
			continue
		last = p[0] % 100
		if last < 10 : 
			continue
		new_cycle = cycle[:]
		new_cycle.append(p[0])
		new_cycle = find_cycle(filter(lambda key: key != p[1], keys), xagonal_map, new_cycle, last)
		if len(new_cycle) == 6 :
			if new_cycle[0] / 100 == new_cycle[-1] % 100 :
				return new_cycle
	return []



def main():
	xagonal_map = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
	for n in range(1000,10000) :
		if is_trinagle(n) :
			xagonal_map[1].append(n)
		if is_square(n) :
			xagonal_map[2].append(n)
		if is_pentagonal(n) :
			xagonal_map[3].append(n)
		if is_hexagonal(n) :
			xagonal_map[4].append(n)
		if is_heptagonal(n) :
			xagonal_map[5].append(n)
		if is_octagonal(n) :
			xagonal_map[6].append(n)
	nums = xagonal_map[1]
	keys = filter(lambda k : k != 1, xagonal_map.iterkeys())
	for num in nums :
		cycle = [num]
		last = num % 100
		if last < 10 : 
			continue
		cycle = find_cycle(keys, xagonal_map, cycle, last)
		if len(cycle) == 6 :
			print "The sum is %d" % sum(cycle)
			


if __name__ == "__main__":
    main()