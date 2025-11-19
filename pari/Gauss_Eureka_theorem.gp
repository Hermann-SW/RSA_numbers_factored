\\ $ n=4^3*11+7 gp -q < Gauss_Eureka_theorem.gp
\\ Δ(20)+Δ(29)+Δ(11)
\\ =210+435+66
\\ =711
\\ $
\\
assert(b,s)=if(!(b), error(Str(s)));

delta(n)=n*(n+1)/2;

assert(getenv("n")!=0);
n=eval(getenv("n"));

sq3=abs(qfsolve(matdiagonal([1,1,1,-(8*n+3)]))[1..3]);
assert(norml2(sq3)==8*n+3);
sq3\=2;

print("Δ(",sq3[1],")+Δ(",sq3[2],")+Δ(",sq3[3],")");
print("=",delta(sq3[1]),"+",delta(sq3[2]),"+",delta(sq3[3]));
print("=",delta(sq3[1])+delta(sq3[2])+delta(sq3[3]));
