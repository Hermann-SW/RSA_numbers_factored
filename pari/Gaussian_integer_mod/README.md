modulus for Gaussian integers, short demo:
```
$ gp -q gimod.gp 
? sq2=19+4*I;
? a=19+19*I;
? a=gimod(a^2,sq2)
-8 + 6*I
? a=gimod(a^2,sq2)
8 - I
? gcd(norml2(a),norml2(sq2))
13
? norml2(sq2)
377
? factorint(norml2(sq2))

[13 1]

[29 1]

? 
```
