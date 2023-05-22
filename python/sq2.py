# pylint: disable=C0103, C3001
#                 invalid-name, unnecessary-lambda-assignment
"""determine sum of squares for 2467-digit prime"""
from time import time
from sys import stderr, argv

from RSA_numbers_factored import sq2

if argv[-1] == "gmpy2":
    from gmpy2 import mpz                  # pylint: disable=no-name-in-module
else:                 mpz = lambda x: x

start = time()
t = sq2(mpz(2 ** 2 ** 13 + 897))
print(str(time() - start) + "s", file=stderr)
print(t[0], t[1])
