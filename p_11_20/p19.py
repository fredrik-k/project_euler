#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 19: 
You are given the following information, but you may prefer to 
do some research for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November.
- All the rest have thirty-one,
- Saving February alone, Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not 
  on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the 
twentieth century (1 Jan 1901 to 31 Dec 2000)?

ANSWER : 171
'''

monthDaysMapp = {
	1 : 31,
	2 : 28,
	3 : 31, 
	4 : 30,
	5 : 31,
	6 : 30,
	7 : 31,
	8 : 31, 
	9 : 30,
	10 : 31,
	11 : 30, 
	12 : 31,
}


def main():
	count = 0
	day = 1
	for year in range(1, 101) : 
		for month in range(1, 13) :
			if day is 6 : 
				count += 1
			day += monthDaysMapp[month]
			if month is 20 and year % 4 is 0 :
				day += 1
			day = day % 7
	print "There has been", count, "sundays on the first of a month in the twentieth century"


if __name__ == "__main__":
    main()