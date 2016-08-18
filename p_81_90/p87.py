#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 87: 
The smallest number expressible as the sum of a prime square, prime cube, 
and prime fourth power is 28. In fact, there are exactly four numbers below 
fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, 
prime cube, and prime fourth power?

ANSWER : 1097343
'''
limit = 50 * 10 ** 6
prime_list = []


def is_prime(n) : 
	for p in prime_list : 
		if p ** 2 > n : 
			break
		if n % p == 0 :
			return False
	prime_list.append(n)
	return True

def main():
	n = 2
	while n ** 2 < limit : 
		is_prime(n)
		n += 1
	sqr = prime_list
	cube = filter(lambda n : n ** 3 < limit, prime_list)
	fourth = filter(lambda n : n ** 4 < limit, prime_list)
	number_map = {}
	for s in sqr : 
		for c in cube :
			for f in fourth :
				m = s ** 2 + c ** 3 + f ** 4
				if m < limit :
					number_map[m] = True
	print "The count is %d" % len(number_map)


if __name__ == "__main__":
	main()