#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 143:
Let ABC be a triangle with all interior angles being less than 120 degrees.
Let X be any point inside the triangle and let XA = p, XC = q, and XB = r.

Fermat challenged Torricelli to find the position of X such that p + q + r was
minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and AMC
are constructed on each side of triangle ABC, the circumscribed circles of
AOB, BNC, and AMC will intersect at a single point, T, inside the triangle.
Moreover he proved that T, called the Torricelli/Fermat point, minimises
p + q + r. Even more remarkable, it can be shown that when the sum is
minimised, AN = BM = CO = p + q + r and that AN, BM and CO also intersect at
T.

If the sum is minimised and a, b, c, p, q and r are all positive integers we
shall call triangle ABC a Torricelli triangle. For example, a = 399, b = 455,
c = 511 is an example of a Torricelli triangle, with p + q + r = 784.

Find the sum of all distinct values of p + q + r ≤ 120000 for Torricelli
triangles.

a^2 = q^2 + r^2 + qr
b^2 = r^2 + p^2 + rp
c^2 = q^2 + p^2 + qp

ANSWER :
'''
LSQ = 347
limit = 120000


def gcd(a, b):
    divisor = 1
    for n in range(2, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            divisor = n
    return divisor


def gen_pairs(limit):
    l = []
    for u in xrange(1, LSQ):
        for v in xrange(1, u):
            if gcd(u, v) != 1:
                continue
            a = 2 * u * v + v * v
            b = u * u - v * v
            if a + b > limit:
                break
            k = 1
            while k * (a + b) < limit:
                l.append((k * a, k * b))
                l.append((k * b, k * a))
                k += 1
    return l


def main():
    pairs = gen_pairs(120000)
    pairs.sort()
    index = map(lambda i: -1, xrange(0, limit))
    for i in xrange(0, len(pairs)):
        p = pairs[i]
        if index[p[0]] == -1:
            index[p[0]] = i

    sums = []

    for p in pairs:
        a = p[0]
        b = p[1]
        va = []
        vb = []

        ia = index[a]
        ib = index[b]

        while ia < len(pairs):
            n = pairs[ia]
            if n[0] != a:
                break
            va.append(n[1])
            ia += 1

        while ib < len(pairs):
            n = pairs[ib]
            if n[0] != b:
                break
            vb.append(n[1])
            ib += 1

        for c in va:
            if c in vb:
                if a + b + c < limit:
                    if a + b + c not in sums:
                        sums.append(a + b + c)
    print "The sum is %d" % sum(sums)

if __name__ == "__main__":
    main()
