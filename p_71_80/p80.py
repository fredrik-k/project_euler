#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 80: 
It is well known that if the square root of a natural number is not an integer, 
then it is irrational. The decimal expansion of such square roots is infinite 
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the 
first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of 
the first one hundred decimal digits for all the irrational square roots.

ANSWER : 40886
'''

def split(n) :
	if n == 0: 
		return []
	l = split(n / 10)
	l.append(int(n % 10))
	return l

def squareroot(n, digits) :
	 limit = 10 ** (digits + 1)
	 a = 5 * n
	 b = 5
 
	 while b < limit :
		  if a >= b :
				a -= b
				b += 10
		  else :
				a *= 100
				b = (b/10) * 100 + 5
 
	 return b/100;

def is_square(n) :
	k = n ** 0.5
	return int(k) == k

def main():
	s = 0
	for i in range(1,100) :
		if not is_square(i) : 
			l = len(split(int(i ** 0.5)))
			s += sum(split(squareroot(i, 100)))
	print "The sum is %d" % s

if __name__ == "__main__":
	 main()