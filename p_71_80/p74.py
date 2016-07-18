#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 74: 
The number 145 is well known for the property that the sum of the factorial of 
its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers 
that link back to 169; it turns out that there are only three such loops that 
exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck 
in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest 
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty 
non-repeating terms?

ANSWER : 402
'''

factorial_loop_map = {}

def split(n) :
	if n == 0 :
		return [] 
	l = split(n/10)
	l.append(n%10)
	return l

def factorial(n) :
	if n == 0 :
		return 1
	return n * factorial(n - 1)

def digit_factorial(n) :
	return sum(map(factorial, split(n)))

def factorial_loop_length(n) :
	if n in factorial_loop_map :
		return factorial_loop_map[n]
	factorials = [n]
	l = 1
	m = n
	while True :
		m = digit_factorial(m)
		if m in factorial_loop_map : 
			return (factorials, l + factorial_loop_map[m])
		if m in factorials :
			break
		factorials.append(m)
		l += 1
	return factorials, l

def main():
	count = 0
	for n in range(2, 10**6) :
		l = 0
		if n in factorial_loop_map :
			l = factorial_loop_map[n]
		else :
			factorials, l = factorial_loop_length(n)
			for i in range(0, len(factorials)) :
				factorial_loop_map[factorials[i]] = l - i
		if l == 60 :
			count += 1
		
	print "The count is %d" % count

if __name__ == "__main__":
    main()