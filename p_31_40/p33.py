#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 33: 
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than 
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.

ANSWER : 100
'''

def is_digital_canceling(nom, den) : 
	if nom % 10 == den / 10 : 
		nom_canceled = float(nom / 10)
		den_canceled = float(den % 10)
		if den_canceled == 0 :
			return False
		if float(nom) / float(den) == nom_canceled / den_canceled : 
			return True

def gcd(a, b) : 
	divisor = 1
	for n in range(2, min(a,b) + 1) :
		if a % n == 0 and b % n == 0 :
			divisor = n 
	return divisor

def main():
	nom_prod = 1
	den_prod = 1
	for den in range(10, 100) :
		for nom in range(10, den) :
			if den % 10 == 0 and nom % 10 == 0 :
				continue
			if is_digital_canceling(nom, den) :
				nom_prod *= nom
				den_prod *= den
	while gcd(nom_prod, den_prod) > 1 :
		div = gcd(nom_prod, den_prod)
		nom_prod /= div
		den_prod /= div
	print "The denominator is %d" % den_prod
if __name__ == "__main__":
    main()