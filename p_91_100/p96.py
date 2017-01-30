#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 96:
Su Doku (Japanese meaning number place) is the name given to a popular
puzzle concept. Its origin is unclear, but credit must be attributed
to Leonhard Euler who invented a similar, and much more difficult,
puzzle idea called Latin Squares. The objective of Su Doku puzzles,
however, is to replace the blanks (or zeros) in a 9 by 9 grid in such
that each row, column, and 3 by 3 box contains each of the digits 1 to
9. Below is an example of a typical starting puzzle grid and its
solution grid.

0 0 3  0 2 0  6 0 0      4 8 3  9 2 1  6 5 7
9 0 0  3 0 5  0 0 1      9 6 7  3 4 5  8 2 1
0 0 1  8 0 6  4 0 0      2 5 1  8 7 6  4 9 3

0 0 8  1 0 2  9 0 0      5 4 8  1 3 2  9 7 6
7 0 0  0 0 0  0 0 8  ->  7 2 9  5 6 4  1 3 8
0 0 6  7 0 8  2 0 0      1 3 6  7 9 8  2 4 5

0 0 2  6 0 9  5 0 0      3 7 2  6 8 9  5 1 4
8 0 0  2 0 3  0 0 9      8 1 4  2 5 3  7 6 9
0 0 5  0 1 0  3 0 0      6 9 5  4 1 7  3 8 2

A well constructed Su Doku puzzle has a unique solution and can be
solved by logic, although it may be necessary to employ "guess and
test" methods in order to eliminate options (there is much contested
opinion over this). The complexity of the search determines the
difficulty of the puzzle; the example above is considered easy because
it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt, contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle
in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found
in the top left corner of each solution grid; for example, 483 is the
3-digit number found in the top left corner of the solution grid above

ANSWER : 24702
'''


def find_square(sudoku, i, j):
    rows = sudoku[(i / 3) * 3:(i / 3) * 3 + 3]
    sqr = map(lambda l: l[(j / 3) * 3:(j / 3) * 3 + 3], rows)
    nums = []
    nums.extend(sqr[0])
    nums.extend(sqr[1])
    nums.extend(sqr[2])
    return nums


def is_valid(sudoku, i, j):
    n = sudoku[i][j]
    if len(filter(lambda m: m == n, sudoku[i])) > 1:
        return False
    if len(filter(lambda l: l[j] == n, sudoku)) > 1:
        return False
    sqr = find_square(sudoku, i, j)
    if len(filter(lambda m: m == n, sqr)) > 1:
        return False
    return True


def solve(sudoku, i, j):
    j += 1
    if j == 9:
        i += 1
        if i == 9:
            return True
        j = 0
    if sudoku[i][j] != 0:
        return solve(sudoku, i, j)
    else:
        m = sudoku[i][j]
        for n in range(1, 10):
            sudoku[i][j] = n
            if is_valid(sudoku, i, j):
                if solve(sudoku, i, j):
                    return True
        sudoku[i][j] = m
        return False


def main():
    sudokus = []
    with open("data/p96.txt") as f:
        sudoku = []
        for s in f.readlines():
            s = s.strip("\n")
            if "Grid" in s and len(sudoku) == 9:
                sudokus.append(sudoku)
                sudoku = []
            elif "Grid" not in s:
                sudoku.append(map(int, s))
        sudokus.append(sudoku)
    for sudoku in sudokus:
        solve(sudoku, 0, -1)
    s = sum(map(lambda sudoku: int("%d%d%d" % tuple(sudoku[0][0:3])),
            sudokus))
    print "The sum is %d" % s


if __name__ == "__main__":
    main()
