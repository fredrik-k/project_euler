#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 142:
Find the smallest x + y + z with integers x > y > z > 0 such that
x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.

ANSWER : Fill in answer when solved

x + y = n^2              x = (a + b) / 2
x - y = m^2              y = (e + f) / 2
x + z = o^2              z = (c + d) / 2
x - z = p^2
y + z = q^2
y - z = r^2
'''

def is_square(n):
    return (n ** 0.5).is_integer()


def main():
    i = 4
    solved = False
    while not solved:
        a = i * i
        j = 3
        while j < i and not solved:
            c = j * j
            f = a - c
            if f < 0 or not is_square(f):
                j += 1
                continue
            k = 1 if j % 2 == 1 else 2
            while k < j and not solved:
                d = k * k
                e = a - d
                b = c - e
                if b <= 0 or e <= 0 or not is_square(b) or not is_square(e):
                    k += 2
                    continue
                x = (d + c) / 2
                y = (e + f) / 2
                z = (c - d) / 2
                solved = True
                print "The sum is %d" % (x + y + z)
                break
                k += 2
            j += 1
        i += 1




if __name__ == "__main__":
    main()