#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 77: 
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five 
thousand different ways?

ANSWER : 71
'''

def prime_sieve(n) : 
	primes = [2]
	for i in range(3, n + 1, 2) :
		for p in primes :
			if p ** 2 > i :
				primes.append(i)
				break
			if i % p == 0 : 
				break
	return primes
 
def main():
	target = 2
	primes = prime_sieve(100)
	while True :
		ways = map(lambda a : 0, range(0,target + 1))
		ways[0] = 1
		for p in primes :
			for j in range(p, target + 1) :
				ways[j] += ways[j-p]
		if ways[target] > 5000 :
			break
		target += 1
	print "The number is %d" % target

if __name__ == "__main__":
    main()