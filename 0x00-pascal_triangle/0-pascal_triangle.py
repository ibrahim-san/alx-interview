#!/usr/bin/python3
"""
Pascal's Triangle
"""

from math import comb

def pascal_triangle(n):
    """
        returns a list of lists of
        integers representing
        the Pascal’s triangle of n
        Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        return [[1]] + [[comb(x, k) for k in range(0, x + 1)] for x in range(1, n)]
