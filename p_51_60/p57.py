#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 57: 
It is possible to show that the square root of two can be expressed 
as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth 
expansion, 1393/985, is the first example where the number of digits in 
the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator 
with more digits than denominator?

ANSWER : Fill in answer when solved
'''
def n_len(n) :
	return len(str(n))

def main():
	count = 0
	num = 1 
	den = 1
	for i in range(1,1000) :
		old_den = den
		den = num + den 
		num = den + old_den
		if n_len(num) >  n_len(den) :
			count += 1
	print "The number of fractions are %d" % count

if __name__ == "__main__":
    main()