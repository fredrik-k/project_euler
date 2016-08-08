#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 84: 
In the game, Monopoly, the standard board is set up in the following way:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	 									C1
T2	 									U1
H1	 									C2
CH3	 									C3
R4	 									R2
G3	 									D1
CC3	 									CC2
G2	 									D2
G1	 									D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP

A player starts on the GO square and adds the scores on two 6-sided dice to 
determine the number of squares they advance in a clockwise direction. Without 
any further rules we would expect to visit each square with equal probability: 
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance)
 changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player 
to go directly to jail, if a player rolls three consecutive doubles, they do not
advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands 
on CC or CH they take a card from the top of the respective pile and, after following 
the instructions, it is returned to the bottom of the pile. There are sixteen cards 
in each pile, but for the purpose of this problem we are only concerned with cards 
that order a movement; any instruction not concerned with movement will be ignored 
and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
	Advance to GO
	Go to JAIL
Chance (10/16 cards):
	Advance to GO
	Go to JAIL
	Go to C1
	Go to E3
	Go to H2
	Go to R1
	Go to next R (railway company)
	Go to next R
	Go to next U (utility company)
	Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. For this reason 
it should be clear that, with the exception of G2J for which the probability of 
finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 
request a movement to another square, and it is the final square that the player 
finishes at on each roll that we are interested in. We shall make no distinction 
between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule 
about requiring a double to "get out of jail", assuming that they pay to get out on 
their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can 
concatenate these two-digit numbers to produce strings that correspond with sets of 
squares.

Statistically it can be shown that the three most popular squares, in order, are 
JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So 
these three most popular squares can be listed with the six-digit modal 
string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit 
modal string.

ANSWER : 101524
'''

import random

def dice_roll(sides) :
	return random.randint(1,sides)

def roll_four_sided_dices() : 
	d1 = dice_roll(4)
	d2 = dice_roll(4)
	return (d1+d2, d1 == d2)

def main():
	visit_map = {i:0 for i in range(0,40)}
	cc_cards = [0, 10]
	cc_cards.extend([-1 for i in range(0,14)])
	random.shuffle(cc_cards)
	ch_cards = [0, 10, 11, 24, 39, 5, -2, -2, -3, -4]
	ch_cards.extend([-1 for i in range(0,6)])
	random.shuffle(ch_cards)
	current = 0
	double_count = 0
	for i in range(0,1000000) :
		next_roll, is_double = roll_four_sided_dices()
		current += next_roll
		current %= 39
		if is_double :
			double_count += 1
		else :
			double_count = 0
		if double_count == 3 :
			double_count = 0
			current = 10
		if current == 30 : 
			current = 10
		if current in [2, 17, 33] :
			cc_card = cc_cards.pop(0)
			cc_cards.append(cc_card)
			if cc_card != -1 : 
				current = cc_card
		if current in [7,22, 36] :
			ch_card = ch_cards.pop(0)
			ch_cards.append(ch_card)
			if ch_card > -1 : 
				current = ch_card
			if ch_card < -1 : 
				if ch_card == -2 :
					if current < 5 : 
						current = 5
					elif current < 15 : 
						current = 15
					elif current < 25 :
						current = 25
					elif current < 35 :
						current = 35
					else :
						current = 5 
				if ch_card == -3 :
					if current < 12 : 
						current = 12 
					elif current < 28 :
						current = 28 
					else : 
						current = 12 
				if ch_card == -4 : 
					current -= 3 
		visit_map[current] += 1
	top_visits =  map(lambda (key, value) : key, sorted(visit_map.iteritems(), 
			key = lambda (key, value): -value)[:3])
	print "The six digit string is %s" % "".join(str(n) for n in top_visits)

if __name__ == "__main__":
	main()
