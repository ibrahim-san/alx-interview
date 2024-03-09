#!/usr/bin/python3
"""
Pascal's Triangle
"""

from math import comb

def pascal_triangle(n):
    """
    This function returns a pascal triangle of height n in the form of a list of integer lists
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        return [[1]] + [[comb(x, k) for k in range(0, x + 1)] for x in range(1, n)]
