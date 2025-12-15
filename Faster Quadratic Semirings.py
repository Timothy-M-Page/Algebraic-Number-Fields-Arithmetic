def mult(x: tuple[int, int], y: tuple[int, int], k: int) -> tuple[int, int]:
    return x[0]*y[0] + k*x[1]*y[1], x[0]*y[1] + x[1]*y[0]


def sigma(x: tuple[int, int], k: int) -> tuple[int, int]:
    """
    Computes σ(x) by looping over possible divisors (a,b)
    and solving algebraically for the co-divisor.
    """
    x0, x1 = x
    s0, s1 = 0, 0

    V = x[0] + k * x[1] + 1

    for a in range(V):
        for b in range(V):
            det = a*a - k*b*b
            if det == 0:
                continue

            c_num = a*x0 - k*b*x1
            d_num = -b*x0 + a*x1

            if c_num % det or d_num % det:
                continue

            c = c_num // det
            d = d_num // det

            if c >= 0 and d >= 0:
                s0 += a
                s1 += b

    return s0, s1


def nice_numbers(n: int, k: int) -> list[tuple[int, int]]:
    nice = []
    for a in range(n + 1):
        if a % 5 == 0:
            print(a)
        for b in range(n + 1):
            if a == 0 and b == 0:
                continue
            s0, s1 = sigma((a, b), k)
            for i in range(n):
                for j in range(n):
                    if mult((i, j), (a, b), k) == (s0, s1):
                        nice.append((a, b))
                        print(f"Integer : {a} + {b}√{k}.     "
                              f"Sigma : {sigma((a, b), k)[0]} + "
                              f"{sigma((a, b), k)[1]}√{k}.     "
                              f"Quotient : {i} + {j}√{k}.")
    return nice


def perfects_numbers(n: int, k: int) -> list[tuple[int, int]]:
    perfect_numbers = []

    for a in range(n + 1):
        if a % 5 == 0:
            print(a)
        for b in range(n + 1):
            s0, s1 = sigma((a, b), k)
            if s0 == 2*a and s1 == 2*b and not (s0 == 0 and s1 == 0):
                perfect_numbers.append((a, b))
                print(f"Perfect: {a} + {b}√{k}")

    return perfect_numbers


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


print(nice_numbers(100, 13))


"""
Nice Numbers up to 200 in N(2)
Integer : 0 + 6√2.       Sigma : 12 + 12√2.      Quotient : 2 + 1√2.
Integer : 0 + 28√2.      Sigma : 56 + 56√2.      Quotient : 2 + 1√2.
Integer : 1 + 0√2.       Sigma : 1 + 0√2.        Quotient : 1 + 0√2.
Integer : 1 + 1√2.       Sigma : 2 + 1√2.        Quotient : 0 + 1√2.
Integer : 2 + 1√2.       Sigma : 4 + 3√2.        Quotient : 1 + 1√2.
Integer : 10 + 7√2.      Sigma : 28 + 20√2.      Quotient : 0 + 2√2.
Integer : 10 + 8√2.      Sigma : 42 + 28√2.      Quotient : 1 + 2√2.
Integer : 11 + 8√2.      Sigma : 22 + 16√2.      Quotient : 2 + 0√2.   ***
Integer : 12 + 6√2.      Sigma : 48 + 36√2.      Quotient : 2 + 2√2.
Integer : 16 + 11√2.     Sigma : 54 + 38√2.      Quotient : 2 + 1√2.
Integer : 20 + 14√2.     Sigma : 84 + 60√2.      Quotient : 0 + 3√2.
Integer : 22 + 16√2.     Sigma : 98 + 70√2.      Quotient : 3 + 1√2.
Integer : 24 + 18√2.     Sigma : 132 + 96√2.     Quotient : 4 + 1√2.
Integer : 60 + 42√2.     Sigma : 336 + 240√2.    Quotient : 0 + 4√2.
Integer : 96 + 66√2.     Sigma : 648 + 456√2.    Quotient : 4 + 2√2.
Integer : 152 + 108√2.   Sigma : 952 + 672√2.    Quotient : 2 + 3√2.

Nice Numbers up to 200 in N(3)
Integer : 1 + 0√3.     Sigma : 1 + 0√3.      Quotient : 1 + 0√3.
Integer : 3 + 2√3.     Sigma : 6 + 4√3.      Quotient : 2 + 0√3.   ***
Integer : 5 + 3√3.     Sigma : 9 + 5√3.      Quotient : 0 + 1√3.
Integer : 9 + 5√3.     Sigma : 24 + 14√3.    Quotient : 1 + 1√3.
Integer : 28 + 0√3.    Sigma : 56 + 0√3.     Quotient : 2 + 0√3.
Integer : 28 + 28√3.   Sigma : 112 + 56√3.   Quotient : 1 + 1√3.
Integer : 54 + 30√3.   Sigma : 288 + 168√3.  Quotient : 2 + 2√3.
Integer : 140 + 84√3.  Sigma : 504 + 280√3.  Quotient : 0 + 2√3.
Integer : 165 + 95√3.  Sigma : 570 + 330√3.  Quotient : 0 + 2√3.

Nice Numbers up to 200 in N(5)
Integer : 1 + 0√5.     Sigma : 1 + 0√5.      Quotient : 1 + 0√5.
Integer : 6 + 0√5.     Sigma : 12 + 0√5.     Quotient : 2 + 0√5.
Integer : 28 + 0√5.    Sigma : 56 + 0√5.     Quotient : 2 + 0√5.

Nice Numbers up to 100 in N(6)
Integer : 1 + 0√6.     Sigma : 1 + 0√6.      Quotient : 1 + 0√6.
Integer : 28 + 0√6.    Sigma : 56 + 0√6.     Quotient : 2 + 0√6.
Integer : 56 + 28√6.   Sigma : 168 + 56√6.   Quotient : 0 + 1√6.
Integer : 66 + 27√6.   Sigma : 162 + 66√6.   Quotient : 0 + 1√6.

Nice Numbers up to 100 in N(7)
Integer : 1 + 0√7.     Sigma : 1 + 0√7.     Quotient : 1 + 0√7.
Integer : 6 + 0√7.     Sigma : 12 + 0√7.    Quotient : 2 + 0√7.
Integer : 8 + 2√7.     Sigma : 16 + 4√7.    Quotient : 2 + 0√7.   ***

Nice Numbers up to 100 in N(8)
Integer : 1 + 0√8.     Sigma : 1 + 0√8.      Quotient : 1 + 0√8.
Integer : 6 + 0√8.     Sigma : 12 + 0√8.     Quotient : 2 + 0√8.
Integer : 28 + 0√8.    Sigma : 56 + 0√8.     Quotient : 2 + 0√8.
Integer : 32 + 11√8.   Sigma : 64 + 22√8.    Quotient : 2 + 0√8.   ***
Integer : 84 + 30√8.   Sigma : 240 + 84√8.   Quotient : 0 + 1√8.

Nice Numbers up to 100 in N(10)
Integer : 1 + 0√10.     Sigma : 1 + 0√10.     Quotient : 1 + 0√10.
Integer : 6 + 0√10.     Sigma : 12 + 0√10.    Quotient : 2 + 0√10.
Integer : 28 + 0√10.    Sigma : 56 + 0√10.    Quotient : 2 + 0√10.

Nice Numbers up to 100 in N(11)
Integer : 1 + 0√11.     Sigma : 1 + 0√11.     Quotient : 1 + 0√11.
Integer : 6 + 0√11.     Sigma : 12 + 0√11.    Quotient : 2 + 0√11.
Integer : 14 + 4√11.    Sigma : 28 + 8√11.    Quotient : 2 + 0√11.   ***
Integer : 28 + 0√11.    Sigma : 56 + 0√11.    Quotient : 2 + 0√11.

Nice Numbers up to 100 in N(13)
Integer : 1 + 0√13.     Sigma : 1 + 0√13.      Quotient : 1 + 0√13.
Integer : 6 + 0√13.     Sigma : 12 + 0√13.     Quotient : 2 + 0√13.
Integer : 28 + 0√13.    Sigma : 56 + 0√13.     Quotient : 2 + 0√13.
Integer : 52 + 16√13.   Sigma : 156 + 48√13.   Quotient : 3 + 0√13.   ***

"""

