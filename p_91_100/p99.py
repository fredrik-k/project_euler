#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 99:
Comparing two numbers written in index form like 2^11 and 37 is not
difficult, as any calculator would confirm that
2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382518061 > 519432525806 would be much
more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K
text file containing one thousand lines with a base/exponent pair on
each line, determine which line number has the greatest numerical
value.

NOTE: The first two lines in the file represent the numbers in the
example given above.

ANSWER : 709
'''

import math


def main():
    with open("data/p99.txt") as f:
        nums = map(lambda s: s.replace('\n', ''), f.readlines())
        nums = map(lambda n: tuple(map(int, n.split(','))), nums)
        nums = map(lambda (n, x): x * math.log(n), nums)
    print "The index is %d" % (nums.index(max(nums)) + 1)


if __name__ == "__main__":
    main()
