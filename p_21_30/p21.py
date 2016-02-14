#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 21: 
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are 
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 
20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors 
of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

ANSWER : 31626
'''

amicableMap = {}

def findDivisors(n):
	d = [1]
	for i in range(2, n) :
		if n % i == 0 :
			d.append(i)
	return d

def isAmicable(n) :
	s1 = sum(findDivisors(n))
	s2 = sum(findDivisors(s1))
	if n != s1 and n == s2 :
		return (s1, s2)
	return None

def main():
   	for i in range(1,10000) :
   		amicablePair = isAmicable(i)
   		if amicablePair != None :
   			amicableMap[amicablePair[0]] = 1
   			amicableMap[amicablePair[1]] = 1
   	s = 0
   	for key in amicableMap :
   		s += key
   	print "The sum is ", s

if __name__ == "__main__":
    main()