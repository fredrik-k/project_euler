#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 79: 
A common security method used for online banking is to ask the user for three 
random characters from a passcode. For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file 
so as to determine the shortest possible secret passcode of unknown length.

ANSWER : 73162890
'''

from sets import Set

def remove_num_at_place(codes, num, place) : 
	new_codes = []
	for code in codes :
		if place >= len(code) : 
			continue
		if code[place] == num : 
			new_codes.append(code[:place] + code[place+1:])
		else :
			new_codes.append(code)
	return new_codes

def gen_num_map(codes) :
	num_map = {}
	for code in codes :
		for i in range(0,len(code)) :
			n = int(code[i])
			if n not in num_map :
				num_map[n] = Set()
			num_map[n].add(i)
	return num_map

def main():
	pass_code = []
	codes = []
	with open('data/p079_keylog.txt', 'r') as f:
		codes = f.readlines()
	codes = map(lambda s : s.split('\n')[0], codes)
	while True : 
		num_map = gen_num_map(codes)
		for (num, places) in num_map.iteritems() : 
			if 0 in places and len(places) == 1 :
				codes = remove_num_at_place(codes, str(num), 0)
				pass_code.append(num)
				break
		codes = filter(lambda code : len(code) > 0, codes)
		if len(codes) == 0 :
			break
	print "The code is %s" % "".join(str(a) for a in pass_code)


if __name__ == "__main__":
    main()