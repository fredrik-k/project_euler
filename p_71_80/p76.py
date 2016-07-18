#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 76: 
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least ¨
two positive integers?

ANSWER : 190569291
'''

def main():
	target = 100
	ways = map(lambda a : 0, range(0,101))
	ways[0] = 1
	for i in range(1, target) :
		for j in range(i, target + 1) :
			ways[j] += ways[j-i]
	print "The number of ways are %d" % ways[100]


if __name__ == "__main__":
    main()