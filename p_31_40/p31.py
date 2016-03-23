#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 31: 
In England the currency is made up of pound, £, and pence, p, 
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

ANSWER : 73682
'''

def find_sum(decs_sorted_set, limit) :
	if limit < 0 : 
		return 0
	if limit == 0 : 
		return 1
	s = 0
	for i in range(0, len(decs_sorted_set)) :
		s += find_sum(decs_sorted_set[i:], limit - decs_sorted_set[i])
	return s

def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    limit = 200
    s = find_sum(coins, limit)
    print "The number of ways are", s


if __name__ == "__main__":
    main()