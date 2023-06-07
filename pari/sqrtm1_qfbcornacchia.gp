assert(b, v, s) = { if(!(b), error(Str(v) Str(s))); }

R(n) = { (10^n - 1) \ 9; }

p = (10^10000 - 1) \ 3 - 10^6333;
p = 34 * R(36400) - 42000040044444004000024 * 10^2264 * R(36400) \ R(4550) - 1;
p = 65516468355 * 2 ^ 333333 + 1;

print(#digits(p), "-digit prime p");


print("lift(sqrt(Mod(-1, p)))");
sqrtm1 = lift(sqrt(Mod(-1, p)));
##
assert(Mod(sqrtm1^2, p) == Mod(p - 1, p), "sqrtm1", " not as needed");

[M,V]=halfgcd(sqrtm1,p);
##
[x,y] = [V[2], M[2,1]];
##
assert(x^2 + y^2 == p, "x,y", " not sum of squares");


print("qfbcornacchia(1, p)");
[x,y] = qfbcornacchia(1, p);
##
assert(x^2 + y^2 == p, "x,y", " not sum of squares");

sqrtm1 = lift(Mod(x/y, p));
##
assert(Mod(sqrtm1^2, p) == Mod(p - 1, p), "sqrtm1", " not as needed");


print("done");
