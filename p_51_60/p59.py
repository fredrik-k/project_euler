#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 59: 
Each character on a computer is assigned a unique code and the preferred 
standard is ASCII (American Standard Code for Information Interchange). 
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to 
ASCII, then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key 
on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, 
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text 
message, and the key is made up of random bytes. The user would keep the 
encrypted message and the encryption key in different locations, and without 
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified 
method is to use a password as a key. If the password is shorter than the 
message, which is likely, the key is repeated cyclically throughout the 
message. The balance for this method is using a sufficiently long password 
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower 
case characters. Using cipher.txt (right click and 'Save Link/Target As...'), 
a file containing the encrypted ASCII codes, and the knowledge that the plain 
text must contain common English words, decrypt the message and find the sum 
of the ASCII values in the original text.

ANSWER :
'''
import itertools

def grouper(n, iterable, fillvalue=None):
	args = [iter(iterable)] * n
	return itertools.izip_longest(*args, fillvalue=fillvalue)

def xor_strings(s,t):
	"""xor two strings together"""
	return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))

def check_chr(c) : 
	if c == 32 or c == 34: 
		return True
	if c < 65 : 
		return False
	if c > 122 :
		return False
	if c > 90 and c < 97 :
		return False
	return True

def main():
	file = open('data/p059_cipher.txt', 'r')
	cipher = map(int, file.read().split(','))
	groups = list(grouper(3, cipher))
	spaces = []
	for i in range(0,3) :
		m = {}
		for group in groups :
			if group[i] not in m : 
				m[group[i]] = 0
			m[group[i]] += 1
		spaces.append(sorted(list(m.iteritems()), key = lambda (entry,count) : -count)[0][0])
	keys = []
	for s in spaces : 
		i = 97
		while i <= ord('z') :
			if chr(s ^ i) == ' ' :
				keys.append(i)
				break
			i += 1
	decypted = []
	for group in groups :
		group = filter(lambda item : item != None, group)
		decypted.extend(map(lambda (char,key) : char ^ key, zip(group,keys)))
	
	print "The sum of the ASCII values are %d" % sum(decypted)

if __name__ == "__main__":
    main()