#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 98:
By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36^2. What is remarkable
is that, by using the same digital substitutions, the anagram, RACE,
also forms a square number: 9216 = 96^2. We shall call CARE (and RACE)
a square anagram word pair and specify further that leading zeroes are
not permitted, neither may a different letter have the same digital
value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text
file containing nearly two-thousand common English words, find all the
square anagram word pairs (a palindromic word is NOT considered to be
an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.

ANSWER : 18769
'''


def is_anagram(a, b):
    return sorted(a) == sorted(b)


def split(n):
    num = []
    while n > 0:
        num.append(n % 10)
        n /= 10
    return num[::-1]


def is_square(num):
    num = num[::-1]
    n = 0
    for i in range(0, len(num)):
        n += num[i] * 10 ** i
    return n == int(n ** 0.5) ** 2


def is_square_pair(a1, a2, num):
    num2 = []
    for c in a2:
        num2.append(num[a1.index(c)])
    return num2[0] != 0 and is_valid(a2, num2) and is_square(num2)


def is_valid(a, num):
    num_map = {}
    char_map = {}
    for i in range(0, len(num)):
        if num[i] not in num_map:
            num_map[num[i]] = []
        num_map[num[i]].append(i)
        if a[i] not in char_map:
            char_map[a[i]] = []
        char_map[a[i]].append(num[i])
        if len(char_map[a[i]]) > 0:
            if (len(filter(lambda n: n == char_map[a[i]][0],
                    char_map[a[i]])) > 1):
                return False
    for _, indicies in filter(lambda
                              (num, list): len(list) > 1, num_map.iteritems()):
        chars = [a[i] for i in indicies]
        if not len(chars) == len(filter(lambda c: c == chars[0], chars)):
            return False
    return True


def has_square_pair(anagram, num):
    for i in range(0, len(anagram)):
        a1 = anagram[i]
        if not is_valid(a1, num):
            continue
        for k in range(0, len(anagram)):
            if k != i:
                a2 = anagram[k]
                if is_square_pair(a1, a2, num):
                    return True
    return False


def largest_square(anagrams):
    if len(anagrams) > 0:
        n = len(anagrams[0][0])
        if n % 2 == 0:
            upper = 10 ** (n / 2) - 1
            lower = int(10 ** (((float(n) - 1.0) / 2.0))) + 1
        else:
            upper = int(10 ** (((float(n)) / 2.0)))
            lower = 10 ** ((n) / 2)
        for s in range(upper, lower, -1):
            num = split(s ** 2)
            for anagram in anagrams:
                if has_square_pair(anagram, num):
                    return s ** 2
    return 0


def main():
    with open("data/p98.txt") as f:
        words = f.readlines()[0].replace('\"', "").split(',')
    words = filter(lambda s: len(s) > 1, words)
    for n in range(max(map(len, words)), 2, -1):
        n_words = filter(lambda s: len(s) == n, words)
        anagrams = []
        while len(n_words) > 0:
            a = n_words[0]
            anagram = filter(lambda s: is_anagram(a, s), n_words)
            if len(anagram) > 1:
                anagrams.append(anagram)
            for s in anagram:
                n_words.remove(s)
        largest = largest_square(anagrams)
        if largest > 0:
            print "The largest square number is %d" % largest
            break


if __name__ == "__main__":
    main()
