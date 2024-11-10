# pylinted and blacked
#
""" p=x²+y² (x > y) for all primes p=1 (mod 4) less than 1000 """
from matplotlib import pyplot as plt
from matplotlib import ticker

from RSA_numbers_factored import sq2, smp1m4

X = []
Y = []
for p in smp1m4:
    x, y = sq2(p)
    if x > y:
        X.append(x)
        Y.append(y)
    else:
        X.append(y)
        Y.append(x)

ax = plt.gca()

ax.set_title("p=x²+y² (x > y) for all primes p=1 (mod 4) less than 1000")

ax.set_aspect("equal")

ax.set_xlim([0, max(X) + 1])
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

ax.set_ylim([0, max(Y) + 1])
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

plt.scatter(X, Y)

plt.show()
