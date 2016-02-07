#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 16: 
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

ANSWER : 1366
'''

def main():
    number = 2**1000
    s = 0
    while number > 0 :
    	s  += number % 10
    	number = int(number/10)
    print "The sum is", s


if __name__ == "__main__":
    main()