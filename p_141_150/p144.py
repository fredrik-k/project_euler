#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
PROBLEM 144:
In laser physics, a "white cell" is a mirror system that acts as a delay line
for the laser beam. The beam enters the cell, bounces around on the mirrors,
and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation
4x^2 + y2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing
the light to enter and exit through the hole.


The light beam in this problem starts at the point (0.0,10.1) just outside the
white cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual
law of reflection "angle of incidence equals angle of reflection." That is,
both the incident and reflected beams make the same angle with the normal line
at the point of incidence.

In the figure on the left, the red line shows the first two points of contact
between the laser beam and the wall of the white cell; the blue line shows the
line tangent to the ellipse at the point of incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is
 m = −4x/y

The normal line is perpendicular to this tangent line at the point of
incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before
exiting?

ANSWER : 354
'''


def perp_slope(x, y):
    m = y / (4 * x)
    return m


def find_ref_ray(x1, y1, x2, y2):
    l1 = (x1 ** 2.0 + y1 ** 2.0) ** 0.5
    l2 = (x2 ** 2.0 + y2 ** 2.0) ** 0.5
    z = (x1 * x2 + y1 * y2) / (l1 * l2)
    xr = x1 / l1 - 2 * x2 / l2 * z
    yr = y1 / l1 - 2 * y2 / l2 * z
    return (xr, yr)


def find_intersection(x0, y0, xr, yr):
    a = 5.0
    b = 10.0
    c = y0 - yr / xr * x0
    m = yr / xr
    root = (a**2.0 * m ** 2.0 + b**2.0 - c**2.0) ** 0.5
    den = a**2.0 * m**2.0 + b**2.0
    xn = (-a**2.0 * m * c - a * b * root) / den
    yn = (b**2.0 * c - a * b * m * root) / den
    if abs(x0 - xn) < 0.0001 and abs(y0 - yn) < 0.0001:
        xn = (-a**2.0 * m * c + a * b * root) / den
        yn = (b**2.0 * c + a * b * m * root) / den
    return (xn, yn)


def main():
    x_0 = 0.0
    y_0 = 10.1
    x_1 = 1.4
    y_1 = -9.6
    c = 1
    while abs(x_1) > 0.01 or y_1 < 0:
        c += 1
        dx = x_1 - x_0
        dy = y_1 - y_0
        m = perp_slope(x_1, y_1)
        (xr, yr) = find_ref_ray(dx, dy, 1.0, m)
        (xn, yn) = find_intersection(x_1, y_1, xr, yr)
        x_0 = x_1
        y_0 = y_1
        x_1 = xn
        y_1 = yn

    print "The number of reflections are %d" % c


if __name__ == "__main__":
    main()
