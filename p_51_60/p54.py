#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 54: 
In the card game poker, a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of 
the highest value wins; for example, a pair of eights beats a pair of 
fives (see example 1 below). But if two ranks tie, for example, both 
players have a pair of queens, then highest cards in each hand are 
compared (see example 4 below); if the highest cards tie then the next 
highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the 
first five are Player 1's cards and the last five are Player 2's cards. You 
can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear 
winner.

How many hands does Player 1 win?

ANSWER : 376
'''
import csv
from sets import Set
from collections import Counter

def is_flush(hand) :
	return len(Set(map(lambda card : card[1], hand))) == 1 

def is_straight(hand) : 
	rank = rank_hand(hand)[::-1]
	if rank[0] == best_card['A'] and rank[1] == best_card['5'] : 
		rank[0] = 5
	diff_set = Set(map(lambda (c1,c2) : c1 - c2, zip(rank, rank[1:])))
	return len(diff_set) == 1 and list(diff_set)[0] == 1

def is_straight_flush(hand) :
	return is_straight(hand) and is_flush(hand) 

best_card = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
			'8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}

def rank_hand(hand) : 
	return sorted(map(lambda card: best_card[card[0]], hand))

def is_royal_flush(hand) : 
	return is_straight_flush(hand) and rank_hand(hand)[0] == best_card['A']

def pair_count(rank) : 
	return map(lambda (card, count) : count, Counter(rank).iteritems())

def is_four_of_a_kind(rank) : 
	return 4 in pair_count(rank) 

def is_full_house(rank) :
	count = pair_count(rank)
	return 3 in count and 2 in count

def is_three_of_a_kind(rank) :
	count = pair_count(rank)
	return 3 in count and 2 not in count

def is_two_pairs(rank) :
	count = pair_count(rank)
	return 3 not in count and 2 in count and len(count) == 3

def is_pair(rank) :
	count = pair_count(rank)
	return 3 not in count and 2 in count
 
def score_hand(hand) : 
	rank = rank_hand(hand)[::-1]
	if is_royal_flush(hand) : 
		return (1, rank)
	if is_straight_flush(hand) : 
		return (2, rank)
	if is_four_of_a_kind(rank) :
		return (3, rank)
	if is_full_house(rank) : 
		return (4, rank) 
	if is_flush(hand) :
		return (5, rank) 
	if is_straight(hand) :
		return (6, rank)
	if is_three_of_a_kind(rank) :
		return (7, rank)
	if is_two_pairs(rank) :
		return (8, rank)
	if is_pair(rank) :
		return (9, rank)
	return (10, rank)

def compare_card(c1,c2) :
	for i in range(0,5) :
		if c1[i] != c2[i] : 
			return c1[i] > c2[i]

def compare_pair(c1,c2) : 
	cnt1 = sorted(Counter(c1).iteritems(), key = lambda (card, count) : - count)
	cnt2 = sorted(Counter(c2).iteritems(), key = lambda (card, count) : - count)
	cnt1 = sorted(filter(lambda (card, count) : count == cnt1[0][1], cnt1), key = lambda (card, count) : - card)
	cnt2 = sorted(filter(lambda (card, count) : count == cnt2[0][1], cnt2), key = lambda (card, count) : - card)
	if cnt1[0][0] == cnt2[0][0] :
		return compare_card(c1,c2)
	else :
		return cnt1[0][0] > cnt2[0][0]


def main():
	win_count = 0
	games = []
	with open('data/p054_poker.txt', 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			games.append(row[0].split(' '))
	for game in games : 
		p1 = score_hand(game[:5])
		p2 = score_hand(game[5:])
		if p1[0] != p2[0] : 
			if p1[0] < p2[0] :
				win_count += 1
		elif p1[0] in [1,2,5,6,10] :
			if compare_card(p1[1], p2[1]) :
				win_count += 1
		else :
			if compare_pair(p1[1], p2[1]) :
				win_count += 1
	print "The number of wins are %d" % win_count
		
if __name__ == "__main__" :
	main()


