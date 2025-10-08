\\ similar to qhull rbox

\\ for square-free n>4
\\
r3(n)=if(n%8==7,0,if(n%8==3,24*qfbclassno(-n),12*qfbclassno(-4*n)));

n=eval(getenv("n"));

print("3\n",r3(n));

{
  for(a=-sqrtint(n),sqrtint(n),
    r=n-a^2;
    for(b=-sqrtint(r),sqrtint(r),
      c=r-b^2;
      if(issquare(c),
        print(a," ",b," ",sqrtint(c));
        if(c,print(a," ",b," ",-sqrtint(c)));
      );
    );
  );
}
