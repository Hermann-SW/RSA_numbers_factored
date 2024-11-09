readvec("../pari/RSA_numbers_factored.gp");

{
print1("factor: ");system("stty -echo");s=input();
system("stty echo");for(i=1,#digits(s),print1("*"));print();

setrand(if(eval(s)==1,1,getwalltime() * eval(s)));

L=432;

[p,q]=[random(2^L), random(2^(L+2))];
p=nextprime(p); while(p%4==3, p=nextprime(p+1));
q=nextprime(q); while(q%4==3, q=nextprime(q+1));
n=p*q;

[x,y]=to_squares_sum(lift(sqrt(Mod(-1,p))),p);
[X,Y]=to_squares_sum(lift(sqrt(Mod(-1,q))),q);
print(x^2+y^2==p && X^2+Y^2==q);

[a,b]=abs(square_sums([x,y,X,Y]));[x,y]=a;[X,Y]=b;
print(x^2+y^2==n && X^2+Y^2==n && #Set([a[1],a[2],b[1],b[2]])==4);

print(x);
print(y);
print(n);
print(#digits(n)," decimal digits semiprime");
quit;
}
