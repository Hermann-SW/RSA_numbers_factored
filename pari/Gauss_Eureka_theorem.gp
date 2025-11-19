\\ $ n=4^2*(8*5+7) gp -q < Gauss_Eureka_theorem.gp 
\\ n=752
\\ 8*n+3=norml2([15, 13, 75])
\\ n=Δ(7)+Δ(6)+Δ(37)=28+21+703
\\ $
\\
assert(b,s)=if(!(b), error(Str(s)));

delta(n)=n*(n+1)/2;

assert(getenv("n")!=0);
n=eval(getenv("n"));
print("n=",n);

sq3=abs(qfsolve(matdiagonal([1,1,1,-(8*n+3)]))[1..3])~;
assert(norml2(sq3)==8*n+3);
print("8*n+3=norml2(",sq3,")");

sq3\=2;
print1("n=Δ(",sq3[1],")+Δ(",sq3[2],")+Δ(",sq3[3],")",\
"=",delta(sq3[1]),"+",delta(sq3[2]),"+",delta(sq3[3]));
