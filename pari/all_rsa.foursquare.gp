readvec("RSA_numbers_factored.gp");

\\ from Bill's posting:
\\ https://pari.math.u-bordeaux.fr/archives/pari-users-2310/msg00012.html
threesquare(n)=abs(qfsolve(matdiagonal([1,1,1,-n]))[1..3]);
foursquarep(n)=
{
  for(i=1,sqrtint(n),
    my(P=n-i^2);
    if(P%8!=7 && ispseudoprime(P),return(concat(i,threesquare(P)))))
};

{
  foreach(rsa,r,[l,n]=r;
    my(F=foursquarep(n));
    print(l," ",F);
    assert(vecsum([x^2|x<-F])==n))
}
##

print("all asserts OK");
