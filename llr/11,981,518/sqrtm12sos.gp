assert(b, v, s) = { if(!(b), error(Str(v) Str(s))); }

\\ as of 2/15/2024:
\\ https://t5k.org/primes/lists/all.txt
\\ -----  ------------------------------- -------- ----- ---- --------------
\\  rank  description                     digits   who   year comment
\\ -----  ------------------------------- -------- ----- ---- --------------
\\     1  2^82589933-1                    24862048 G16   2018 Mersenne 51??
\\     2  2^77232917-1                    23249425 G15   2018 Mersenne 50??
\\     3  2^74207281-1                    22338618 G14   2016 Mersenne 49??
\\     4  2^57885161-1                    17425170 G13   2013 Mersenne 48
\\     5  2^43112609-1                    12978189 G10   2008 Mersenne 47
\\     6  2^42643801-1                    12837064 G12   2009 Mersenne 46
\\     7e Phi(3,-516693^1048576)          11981518 L4561 2023 Generalized unique
\\     8  Phi(3,-465859^1048576)          11887192 L4561 2023 Generalized unique
\\
p = polcyclo(3,-516693^1048576);

print(#digits(p), "-digit prime p (", #digits(p, 2), " bits)");

\\ sqrtm1 determined in 8.5 days on AMD 7950X CPU with patched LLR tool:
\\ https://github.com/Hermann-SW/RSA_numbers_factored/llr/11,981,518

sqrtm1 = readvec("sqrtm1.gp")[1];
assert(Mod(sqrtm1^2, p) == Mod(p - 1, p), "sqrtm1", " not as needed");

print("[M,V] = halfgcd(sqrtm1, p)");
[M,V] = halfgcd(sqrtm1, p);
##
print("[x,y] = [V[2], M[2,1]]");
[x,y] = [V[2], M[2,1]];
##
assert(x^2 + y^2 == p, "x,y", " not sum of squares");


print("done, all asserts OK");
