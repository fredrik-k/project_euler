#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 36: 
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)

ANSWER : 872187
'''

def is_palindrome(n) :
	if n[-1] == '0' :
		return False
	rev = n[::-1]
	return rev == n 

def main():
	s = 0
	for n in range(1,10**6) :
		if is_palindrome(str(n)) :
			if is_palindrome(bin(n)[2:]) :
				s += n
	print "The sum is %d" % s
    	

if __name__ == "__main__":
    main()