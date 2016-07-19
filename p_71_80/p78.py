#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 78: 
Let p(n) represent the number of different ways in which n coins can be separated 
into piles. For example, five coins can be separated into piles in exactly seven 
different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.

ANSWER : 55374
'''

def main():
	p = []
	p.append(1)
	n = 1
	while True :
		i = 0
		penta = 1
		p.append(0)
		while penta <= n :
			sign = -1 if i % 4 > 1 else 1
			p[n] += sign * p[n - penta]
			p[n] %= 1000000
			i += 1
			j = i / 2 + 1 if (i % 2 == 0) else -(i / 2 + 1)
			penta = j * (3 * j - 1) / 2
		if p[n] == 0 : 
			break
		n += 1
	print "The number is %d" % n

if __name__ == "__main__":
    main()