#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 107:
The following undirected network consists of seven vertices and twelve
edges with a total weight of 243.


The same network can be represented by the matrix below.

        A   B   C   D   E   F   G
        A   -   16  12  21  -   -   -
        B   16  -   -   17  20  -   -
        C   12  -   -   28  -   31  -
        D   21  17  28  -   18  19  23
        E   -   20  -   18  -   -   11
        F   -   -   31  19  -   -   27
        G   -   -   -   23  11  27  -

However, it is possible to optimise the network by removing some edges
and still ensure that all points on the network remain connected. The
network which achieves the maximum saving is shown below. It has a
weight of 93, representing a saving of 243 − 93 = 150 from the
original network.


Using network.txt (right click and 'Save Link/Target As...'), a 6K
text file containing a network with forty vertices, and given in
matrix form, find the maximum saving which can be achieved by removing
redundant edges whilst ensuring that the network remains connected.

ANSWER : 259679
'''


def index_of_min(l):
    index = 0
    m = -1
    for i in range(0, len(l)):
        n = l[i]
        if n == -1:
            continue
        if m == -1:
            n = m
            index = i
        if n < m:
            n = m
            index = i
    return index


def find_possible_edges(visited_map, graph):
    possible = []
    for i in range(0, len(visited_map)):
        if visited_map[i]:
            edges = graph[i]
            for j in range(0, len(edges)):
                n = edges[j]
                if n != -1 and not visited_map[j]:
                    possible.append((n, i, j))
    return possible


def main():
    with open("data/p107.txt") as f:
        graph = f.readlines()
    graph = map(lambda s: s.strip("\n"), graph)
    graph = map(lambda s: s.replace('-', '-1'), graph)
    graph = map(lambda s: map(int, s.split(',')), graph)

    visited_map = [False] * len(graph)
    visited_map[1] = [True]

    s = 0

    while False in visited_map:
        possible = find_possible_edges(visited_map, graph)
        (n, f, t) = sorted(possible, key=lambda (n, i, j): n)[0]
        s += n
        visited_map[t] = True

    total_sum = 0
    for i in range(0, len(graph)):
        for j in range(0, i):
            n = graph[i][j]
            if n != -1:
                total_sum += n
    print "The maximum savings are %d" % (total_sum - s)


if __name__ == "__main__":
    main()
