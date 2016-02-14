#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 22: 
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working 
out the alphabetical value for each name, multiply this value 
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
ANSWER : 871198282
'''

letterPlacementMap = {
	'a' : 1, 
	'b' : 2,
	'c' : 3,
	'd' : 4,
	'e' : 5,
	'f' : 6,
	'g' : 7,
	'h' : 8,
	'i' : 9,
	'j' : 10,
	'k' : 11, 
	'l' : 12,
	'm' : 13,
	'n' : 14,
	'o' : 15,
	'p' : 16,
	'q' : 17,
	'r' : 18,
	's' : 19,
	't' : 20,
	'u' : 21,
	'v' : 22,
	'w' : 23,
	'x' : 24,
	'y' : 25,
	'z' : 26,
}  

def main():
    totalSum = 0
    file = open('p022_names.txt', 'r')
    names = file.read().split(',')
    names = sorted(names)
    names = map(lambda name : name.replace('\"', '').lower(), names)
    for i in range(0, len(names)) :
        s = 0
        for c in names[i] :
            s += letterPlacementMap[c]
        totalSum += s * (i + 1)
    print "The sum is", totalSum

if __name__ == "__main__":
    main()