#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 88: 
A natural number, N, that can be written as the sum and product of a given set of at 
least two natural numbers, a1, a2, ... , ak is called a product-sum number: 
N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal 
product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, 
and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30 note 
that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is 4, 6, 8, 12, 
15, 16, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
ANSWER : 7587457
'''
import math
import sys

def main() : 
	maxK = 12000
	maxNumber = 2 * maxK
 
	numFactors = int(math.log10(maxNumber) / math.log10(2))
	factors = [0 for i in range(0, numFactors)]
	 
	k = range(0, 24001, 2)
	k[1] = 0
	 
	factors[0] = 1
	curMaxFactor = 1
	j = 0
	 
	while True :
		if (j == 0) :
			if (curMaxFactor == numFactors) :
				break
	 
			if (factors[0] < factors[1]) :
				factors[0] += 1
			else :
				curMaxFactor += 1
				factors[curMaxFactor - 1] = sys.maxint
				factors[0] = 2
			
	 
			j += 1
			factors[1] = factors[0]-1
		elif(j == curMaxFactor-1) :
			factors[j] += 1
			s = 0
			prod = 1
			for i in range(0, curMaxFactor) :
				prod *= factors[i]
				s += factors[i]
			
			if (prod > maxNumber) :
				j -= 1
			else :
				pk = prod - s+ curMaxFactor
				if (pk <= maxK and prod < k[pk]) : 
					k[pk] = prod
				
			
		elif (factors[j] < factors[j + 1]) :
			factors[j] += 1
			factors[j+1] = factors[j]-1
			j += 1
		elif(factors[j] >= factors[j + 1]) :
			j -= 1
	
	print "The sum is %d" % sum(set(k))

if __name__ == "__main__":
	main()