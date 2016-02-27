#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 25: 
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

ANSWER : 4782
'''
def next_fibonacci(n1, n2) : 
	return n1 + n2

def main():
    i = 2
    n1 = 1
    n2 = 1
    while n2 < 10**999 :
    	i += 1
    	n3 = next_fibonacci(n1, n2)
    	n1 = n2 
    	n2 = n3
    print "The index of the first Fibonacci number greater than 10^1000 is", i

if __name__ == "__main__":
    main()