"""
Define a semi-ring (R, + ,x) where R is all combinations of a + b * √k
for a non square k, with a and b natural numbers. That is, the semi-ring
associated to the quadratic field Q(√k).

Such semi-rings allow a well-defined sum of divisors function, any element
has a finite number of divisors using the definition : a|b iff there exists c
such that b = ac, for elements a,b and c in R.

We wish to investigate perfect numbers in such semi-rings, defined as usual
with sigma(n) = sum_(d|n) d.


Note that there should be a semiring and associated arithmetic behaviour for
every algebraic number field. We can begin with quadratic fields as they
are nice and simple but once we understand more algebraic number theory we can
look at all sorts of fields and other arithmetic functions, the number of divisors
and Euler's totient function should be easy to generalise.
"""
