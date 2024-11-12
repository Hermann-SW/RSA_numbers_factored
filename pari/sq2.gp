readvec("RSA_numbers_factored.gp");
f(v)={if(v[1]%2==0,v,[v[2],v[1]])};
{
  n=eval(getenv("n"));
  h=sqrtint(n);
  M=matrix(h,h);
  forprime(p=5,n,if(p%4==1,
    [x,y]=f(sq2(p));
    M[h+1-y,x]=1;
  ));
  print("P1\n#\n",h," ",h);
  foreach(M~,r,foreach(r,c,print1(c));print())
}
