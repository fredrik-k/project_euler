#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 63: 
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit 
number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

ANSWER : Fill in answer when solved
'''

def main():
	n = 1
	count = 0
	l = 1 
	while True :
		length = len(str(n**l))
		if  length == l : 
			count += 1
		if length > l : 
			if l == 21 : 
				break
			l += 1 
			n = 0
		n += 1 
	print "The count is %d" % count

if __name__ == "__main__":
    main()