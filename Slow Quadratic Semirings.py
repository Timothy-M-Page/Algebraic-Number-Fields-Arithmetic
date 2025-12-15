"""
Define a semi-ring (R, + ,x) where R is all combinations of a + b * root(k)
for a non square k, with a and b natural numbers. That is, the semi-ring
associated to the quadratic field Q(root(k)).

Such semi-rings allow a well-defined sum of divisors function, any element
has a finite number of divisors using the definition : a|b iff there exists c
such that b = ac, for elements a,b and c in R.

We wish to investigate perfect numbers in such semi-rings, defined as usual
with sigma(n) = sum_(d|n) d.
"""

import math


def value(x: list[int], k: int) -> int:
    # Used as an upper bound for a range given the input is a list.
    return math.ceil(x[0] + k*x[1])


def multiply(x: list[int], y: list[int], k: int) -> list[int]:
    return [x[0]*y[0] + k*x[1]*y[1], x[0]*y[1] + x[1]*y[0]]


def divide(x: list[int], y: list[int], k: int) -> list[int]:
    V = value(x, k) + 1
    for i in range(V):
        for j in range(V):
            if multiply(y, [i, j], k) == x:
                return [i, j]
    else:
        return [0, 0]


def divs(x: list[int], k: int) -> list[list[int]]:
    divisors = []
    V = value(x, k)+1
    for i in range(V):
        for j in range(V):
            a = divide(x, [i, j], k)[0]
            b = divide(x, [i, j], k)[1]
            if [a, b] != [0, 0]:
                divisors.append([a, b])
    return divisors


def sigma(x: list[int], k: int) -> list[int]:
    summation = [0, 0]
    V = value(x, k)+1
    for i in range(V):
        for j in range(V):
            a = divide(x, [i, j], k)[0]
            b = divide(x, [i, j], k)[1]
            summation[0] += a
            summation[1] += b
    return summation


def perfects(n: int, k: int) -> list[list[int]]:
    perfect_numbers = []
    for i in range(n+1):
        # print(i)
        for j in range(n+1):
            if divide(sigma([i, j], k), [i, j], k) != [0, 0]:
                perfect_numbers.append([i, j])
                print([i, j])
    return perfect_numbers


def analysis(x: list[int], k: int) -> None:
    print(f"Integer {x[0]} + {x[1]}√{k}")
    print(f"Divisors : {divisors(x, k)}")
    print(f"Sum of divisors : {sigma(x, k)}")
    print(f"Quotient : {divide(sigma(x, k), x, k)}")
    return None


def divisors(x: tuple[int, int], k: int):
    x0, x1 = x
    divs = []

    V = x[0] + k * x[1] + 1

    for a in range(V):
        for b in range(V):
            det = a*a - k*b*b
            if det == 0:
                continue

            c_num = a*x0 - k*b*x1
            d_num = -b*x0 + a*x1

            if c_num % det != 0 or d_num % det != 0:
                continue

            c = c_num // det
            d = d_num // det

            if c >= 0 and d >= 0:
                divs.append((a, b, c, d))

    return divs


