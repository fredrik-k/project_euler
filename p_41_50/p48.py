#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 48: 
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

ANSWER : Fill in answer when solved
'''

def main():
    s = 0 
    for i in range(1,1001) :
    	s += (i ** i) % (10 ** 10)
    	s = s % (10 ** 10)
    print "The last ten digits are %d" % s 

if __name__ == "__main__":
    main()