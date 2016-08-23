#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 89: 
For a number written in Roman numerals to be considered valid there are basic rules 
which must be followed. Even though the rules allow some numbers to be expressed in 
more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number 
sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is 
considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one 
thousand numbers written in valid, but not necessarily minimal, Roman numerals; see 
About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four 
consecutive identical units.

ANSWER : 743
'''

roman_to_num_map = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

shortest_map = {1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V', 6 : 'VI', 7 : 'VII', 
				8 : 'VIII', 9 : 'IX', 10 : 'X', 20 : 'XX', 30: 'XXX', 40 : 'XL', 50 : 'L',
				60 : 'LX', 70 : 'LXX', 80 : 'LXXX', 90 : 'XC', 100 : 'C', 200 : 'CC',
				300 : 'CCC', 400 : 'CD', 500 : 'D', 600 : 'DC', 700 : 'DCC', 800 : 'DCCC', 
				900 : 'CM', 1000 : 'M', 2000 : 'MM', 3000 : 'MMM', 4000 : 'MMMM', 5000 : 'MMMMM'}

def roman_to_num(r) : 
	n = 0
	n_part = 0
	i = 0
	while i < len(r) : 
		if i == len(r) - 1 :
			n += n_part + roman_to_num_map[r[i]]
			break
		n1 = roman_to_num_map[r[i]]
		n2 = roman_to_num_map[r[i + 1]]
		if n1 == n2 : 
			n_part += n1
			i += 1
		elif n1 > n2 :
			n += n_part + n1 
			n_part = 0
			i += 1
		elif n1 < n2 :
			n_part += n1 
			n += n2 - n_part 
			n_part = 0
			i += 2
	return n  

def num_to_roman(n) : 
	r = []
	i = 0
	while n > 0 : 
		m = n % 10
		n = n / 10
		if m != 0 : 
			r.insert(0, shortest_map[m * 10 ** i])
		i += 1
	return ''.join(s for s in r)

def plus(x, y) : 
	return x + y

def main():
	with open("data/p089_roman.txt") as f: 
		roman = map(lambda l : l.strip('\n'), f.readlines())
	print "The number of reduced chars is %d" % (reduce(plus, map(len, roman)) - 
		reduce(plus, map(len,map(num_to_roman, map(roman_to_num, roman)))))

if __name__ == "__main__":
	main()