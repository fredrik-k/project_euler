#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 90:
Each of the six faces on a cube has a different digit (0 to 9) written on it; the same
is done to a second cube. By placing the two cubes side-by-side in different positions
we can form a variety of 2-digit numbers.

For example, the square number 64 could be formed:

In fact, by carefully choosing the digits on both cubes it is possible to display all
of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.

For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube
and {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an
arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square
numbers to be displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on each cube, not
the order.

{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last
example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming
2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the square numbers to
be displayed?

ANSWER :
'''

square_pairs = [(0,1), (0,4), (0, 6), (1,6), (2,5), (3,6), (4,6), (6,4), (8,1)]

def gen_dices() :
	dices = []
	for d1 in range(0,5) :
		for d2 in range(d1 + 1, 6) :
			for d3 in range(d2 + 1, 7) :
				for d4 in range(d3 + 1, 8) :
					for d5 in range(d4 + 1, 9) :
						for d6 in range(d5 + 1, 10) :
							d = [d1,d2,d3,d4,d5,d6]
							d = map(lambda n : 6 if n == 9 else n, d)
							dices.append(d)
	return dices

def valid_combination(d1, d2) :
	for (a,b) in square_pairs :
		if (a not in d1 or b not in d2) and (b not in d1 or a not in d2) :
			return False

	return True


def main():
	dices = gen_dices()
	count = 0
	for i in range(0,len(dices)) :
		for j in range(i + 1, len(dices)) :
			if valid_combination(dices[i], dices[j]) :
				count += 1
	print "The count is %d" % count

if __name__ == "__main__":
	main()


# Dice one must have : 0,
