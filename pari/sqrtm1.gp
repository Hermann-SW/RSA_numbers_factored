\\ Determine sqrtm1 = sqrt(-1) (mod p)
\\
\\ $ n='(10^10000-1)\3 - 10^6333'  gp -q < sqrtm1.gp 2>err
\\ 2
\\   ***   last result computed in 3,042 ms.
\\ $ wc err
\\     1     1 10001 err
\\ $ 
assert(b, v, s) = { if(!(b), error(Str(v) Str(s))); }

if (getenv("n") == 0, print(\
  "Format: n=\"value\"  gp -q < sqrtm1.gp\n");\
quit);

n = eval(getenv("n"));
assert(n%4 == 1, "n != 1 (mod 4): ", n);

forprime(t=2,oo,if( kronecker(t, n)==-1, qnr=t; break()));
print(qnr);
p=lift(Mod(qnr, n)^(n\4));
##
write("/dev/stderr", p);
assert(p^2 % n == n-1, "p^2 % n != n-1: ", p);
