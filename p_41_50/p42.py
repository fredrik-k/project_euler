#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 42: 
The nth term of the sequence of triangle numbers is given by, 
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to 
its alphabetical position and adding these values we form a word 
value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a 
triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K 
text file containing nearly two-thousand common English words, 
how many are triangle words?

ANSWER 162: 
'''
import csv

alphabetical_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 
					'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 
					'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 
					'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 
					'Y': 25, 'Z': 26}

triangle_numbers = map(lambda n : n*(n+1)/2, range(1,400))

def main():
	data = []
	count = 0
	with open('data/p042_words.txt', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			data = list(row)
	for word in data : 
		s = 0
		for c in word :
			s += alphabetical_map[c]
		if s in triangle_numbers : 
			count += 1
	print "The number of triangle words are %d" % count

if __name__ == "__main__":
    main()