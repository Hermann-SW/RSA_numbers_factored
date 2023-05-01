from RSA_numbers_factored import *

R = RSA()
r = R.factored_2()[-1]
l, n, p, q, pm1, qm1 = r
assert (p - 1) * (q - 1) == R.totient(r)
assert R.totient_2(r) == R.totient_2(l)
assert R.totient_2(r) == dictprod_totient(pm1, qm1)
assert pow(65537, R.reduced_totient_2(190), R.reduced_totient(190)) == 1

R.validate()
