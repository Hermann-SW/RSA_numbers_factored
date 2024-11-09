#!/usr/bin/python
""" pylinted and edited with black """
import os
import random
import time
import stdiomask
import sympy.ntheory as nt
from RSA_numbers_factored import RSA, digits, sq2, square_sums

s = stdiomask.getpass("factor: ")
random.seed(time.time_ns() * int(s))

L = 432

[p,q] = [random.getrandbits(L), random.getrandbits(L + 2)]

p=nt.nextprime(p)
while p%4==3:
    p=nt.nextprime(p+1)
q=nt.nextprime(q)
while q%4==3:
    q=nt.nextprime(q+1)
n=p*q

[x,y]=sq2(p);
[X,Y]=sq2(q);
print(x**2+y**2==p and X**2+Y**2==q)

[a,b]=(square_sums([x,y,X,Y]));[x,y]=a;[X,Y]=b;
print(x**2+y**2==n and X**2+Y**2==n) and len(set([a[1],a[2],b[1],b[2]]))==4

print(x)
print(y)
print(n)
print(digits(n)," decimal digits semiprime")
