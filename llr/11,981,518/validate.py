#!/usr/bin/env python

from gmpy2 import mpz

p=mpz(516693)**1048576
p=p**2-p+1

with open("sqrtm1.gp") as in_file:
    lines = in_file.read().splitlines()
s=mpz(lines[0])

print(pow(s,2,p)==p-1)

with open("sos.gp") as in_file:
    lines = in_file.read().splitlines()
[x,y]=lines[0].split(",")
x=mpz(x[1:])
y=mpz(y[:-1])

print(x**2+y**2==p)
