#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 26: 
A unit fraction contains 1 in the numerator. The decimal 
representation of the unit fractions with denominators 2 
to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring 
cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest 
recurring cycle in its decimal fraction part.

ANSWER : 983
'''


def main():
	number = -1
	longest_recurring = -1
	for i in range(1,1000) :
		i = 1000 - i
		if longest_recurring > i :
			break
		remainders = {}
		value = 1
		position = 0
		while value not in remainders and value != 0 :
			remainders[value] = position
			value *= 10
			value %= i
			position  += 1
		if position - remainders[value] > longest_recurring :
			longest_recurring = position - remainders[value]
			number = i
	print "Number with longes recurring cycle is", number


if __name__ == "__main__":
    main()