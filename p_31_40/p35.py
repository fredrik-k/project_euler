#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 35 : 
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
73, 79, and 97.

How many circular primes are there below one million?

ANSWER : 55
'''
def rotate(n):
	rotlist = []
	m = str(n)
	counter = 0
	while counter < len(str(n)):
		m = m[1:] + m[0]
		rotlist.append(int(m))
		counter += 1
	return rotlist

def isprime(n) :
	if n < 2 :
		return False 
	for i in range(2, int(n ** 0.5 + 1 )) :
		if n % i == 0 :
			return False
	return True

def iscircularprime(n):
	np = [0,2,4,5,6,8]
	y = str(n)
	for j in y:
		if int(j) in np:
			return False
	if isprime(n)==False:
		return False
	m = rotate(n)

	# new code here
	is_circ_prime = True
	for i in m:
		if not isprime(i):
			is_circ_prime = False
	return is_circ_prime

def main():
	count = 2
	for i in range(3, 10**6) :
		if iscircularprime(i) :
			count += 1
	print "The number is %d" % count

if __name__ == "__main__":
    main()