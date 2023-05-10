"""determine sum of squares for 2466-digit prime"""
from time import time
from sys import stderr, argv
if len(argv) > 1 and argv[1] == "gmpy2":
    from gmpy2 import mpz
else:
    def mpz(x):
        return x

from RSA_numbers_factored import sq2

start = time()
t = sq2(mpz(2 ** 2 ** 13 + 897))
print(str(time() - start) + "s", file=stderr)
print(t[0], t[1])
