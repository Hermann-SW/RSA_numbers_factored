\\ similar to qhull rbox

\\ from https://pari.math.u-bordeaux.fr/archives/pari-users-2510/msg00012.html
\\
classno(n)=quadclassunit(n).no;

\\ for square-free n>4
\\
r3(n)=if(n%8==7,0,if(n%8==3,24*classno(-n),12*classno(-4*n)));

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
