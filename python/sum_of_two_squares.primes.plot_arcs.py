# pylinted and blacked
#
""" p=x²+y² (x > y) for all primes p=1 (mod 4) less than int(argv[0]) """
from sys import argv
from math import sqrt
from matplotlib import pyplot as plt
from matplotlib import ticker
from sympy import primerange

from RSA_numbers_factored import sq2

X = []
Y = []
for p in primerange(5, int(argv[1])):
    if p % 4 == 1:
        x, y = sq2(p)
        X.append(max(x, y))
        Y.append(min(x, y))

D = 64
A = [X[0]]
B = [Y[0]]
for i in range(1, len(X)):
    r0 = sqrt(X[i - 1] ** 2 + Y[i - 1] ** 2)
    r1 = sqrt(X[i] ** 2 + Y[i] ** 2)
    for j in range(1, D):
        x = X[i - 1] + j * (X[i] - X[i - 1]) / D
        y = Y[i - 1] + j * (Y[i] - Y[i - 1]) / D
        r = sqrt(x**2 + y**2)
        x = x / r * (r0 + (r1 - r0) * j / D)
        y = y / r * (r0 + (r1 - r0) * j / D)
        A.append(x)
        B.append(y)
    A.append(X[i])
    B.append(Y[i])

ax = plt.gca()

ax.set_title(
    "p=x²+y² (x > y) for all primes p=1 (mod 4) less than "
    + argv[1]
    + " (variable radius arcs)"
)

ax.set_aspect("equal")

ax.set_xlim([0, max(X) + 1])
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

ax.set_ylim([0, max(Y) + 1])
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

plt.scatter(X, Y)
plt.plot(A, B)

plt.show()
