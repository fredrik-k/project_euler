#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 17: 
If the numbers 1 to 5 are written out in words: one, two, 
three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
20 letters. The use of "and" when writing out numbers is in compliance with 
British usage.

ANSWER : 21124
'''
s = ["zero","one", "two", "three", "four", "five", "six", "seven", 
"eight", "nine","ten", "eleven", "twelve", "thirteen", "fourteen", 
"fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

t = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
"eighty", "ninety"]


def numberToString(thousands, hundreds, tens, singles) :
	spelledOut = ""
	if thousands == 1 :
		spelledOut = "one thousand"
	if hundreds > 0 :
		spelledOut += s[hundreds] + " hundred "
		if tens > 0 or singles > 0 :
			spelledOut += "and "
	if tens < 2 and tens > 0:
		spelledOut += s[tens * 10 + singles]	
	elif tens > 0 :
		spelledOut += t[tens] 
		if singles > 0 :
			spelledOut += " " + s[singles]
	elif singles > 0 :
		spelledOut += s[singles]
	return spelledOut

def main():
    s = 0
    for number in range(1,1001) :
    	singles = number % 10
    	number = int(number/10)
    	tens = number % 10
    	number = int(number/10)
    	hundreds = number % 10
    	number = int(number/10)
    	thousands = number % 10
    	s += len(numberToString(thousands, hundreds, tens, singles).replace(" ", ""))
    print "Number of letters in all numbers from one to a thousand is", s

if __name__ == "__main__":
    main()