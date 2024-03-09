from math import comb

def pascal_triangle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        return [[1]] + [[comb(x, k) for k in range(0, x + 1)] for x in range(1, n)]
