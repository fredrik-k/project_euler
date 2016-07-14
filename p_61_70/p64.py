#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 64: 
All square roots are periodic when written as continued fractions and can be 
written in the form:

√N = a0 + / (a1 + 1 / (a2 + 1 / (a3 + 1/(...))))

For example, let us consider √23:

√23 = 4 + √23 - 4 = 4 + 1 / (1 / (√23 -4)) = 4 + 1 / (1 + (√23 -  3) / 7)

If we continue we would get the following expansion:

√23 = 4 + / (1 + 1 / (3 + 1 / (1 + 1 / (8 + ...))))

It can be seen that the sequence is repeating. For conciseness, we use the notation 
23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots 
are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?

ANSWER : 1322
'''

def is_square(n) : 
	k = n ** 0.5
	return k == int(k) 

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
		if len(seq) > 1000 :
			print seq
	return seq

def main():
	count = 0
	for n in range(2, 10000) :
		if not is_square(n) :
			seq = find_period(n) 
			if len(seq) % 2 == 1 :
				count +=1
	print "The count is %d" % count

if __name__ == "__main__":
    main()