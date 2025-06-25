"""Math and numpy modules."""

# A
import math as m
from math import gcd
from sys import stdin
from math import comb
from math import dist, cos, sin
import numpy as np



x = float(input())
a = m.log(m.pow(x, 3 / 16), 32)
b = m.pow(x, m.cos((m.pi * x) / (2 * m.e)))
c = m.pow(m.sin(x / m.pi), 2)
print(a + b - c)   


# B
for i in stdin:
    print(gcd(*map(int, i.split())))
    
# C
n, f = map(int, input().split())
print(comb(n, f) * f // n, comb(n, f))


# D
numbers = list(map(float, input().split()))
print(m.pow(m.prod(numbers), 1 / len(numbers)))

# E
deca_x, deca_y = map(float, input().split())
pola_r, pola_f = map(float, input().split())
pola_x = pola_r * cos(pola_f)
pola_y = pola_r * sin(pola_f)
print(dist((deca_x, deca_y), (pola_x, pola_y)))

# F


def multiplication_matrix(n):
    matrix = np.arange(1, n + 1)
    return matrix * matrix[:, None]


# G


def make_board(num):
    matrix = np.indices((num, num)).sum(axis=0) % 2
    return np.array(np.rot90(matrix), dtype='int8')


# H


def snake(m, n, direction='H'):
    matrix = np.zeros((n, m), dtype=np.int16)
    num = 1
    if direction == 'H':
        for i in range(n):
            if not i % 2:
                matrix[i] = np.arange(num, num + m)
            else:
                matrix[i] = np.arange(num + m - 1, num - 1, -1)
            num += m
    else:
        for j in range(m):
            if not j % 2:
                matrix[:, j] = np.arange(num, num + n)
            else:
                matrix[:, j] = np.arange(num + n - 1, num - 1, -1)
            num += n
    return matrix

# I


def rotate(matrix, angle):
    return np.rot90(matrix, (360 - angle) // 90)


# J


def stairs(vector):
    n = len(vector)
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        matrix[i] = np.roll(vector, i)
    return matrix