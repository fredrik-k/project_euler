#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 66: 
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is 
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the 
following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained 
when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value 
of x is obtained.

ANSWER : 661
'''

def find_period(n) :
	seq = []
	k = n ** 0.5
	a = int(k)
	d =1
	a0 = a
	m = 0
	while a != 2 * a0 : 
		m = d * a - m
		d = (n - m * m) / d
		a = (a0 + m) /d
		seq.append(a)
	return seq

def next_hk(a, h2, h1, k2, k1) : 
	h = a * h1 + h2
	k = a * k1 + k2 
	return (h, k)

def find_min_diophantine_x(D) :
	seq = find_period(D)
	a = int(D ** 0.5)
	h2 = 0
	h1 = 1
	k2 = 1
	k1 = 0
	while True:
		for s in seq : 
			(h,k) = next_hk(a, h2, h1, k2, k1)
			if h**2 - D*k**2 == 1 : 
				return (h, D)
			h2 = h1 
			h1 = h
			k2 = k1 
			k1 = k
			a = s

def is_not_square(n) :
	k = n ** 0.5
	return int(k) != k

def main():
	max_x = 0
	xs = map(find_min_diophantine_x, filter(is_not_square, range(2, 1001)))
	print "The maximal value of x is %d" % max(xs, key = lambda (x,d) : x)[1]

if __name__ == "__main__":
    main()