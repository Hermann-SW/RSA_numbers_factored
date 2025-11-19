\\ https://pari.math.u-bordeaux.fr/archives/pari-users-2511/msg00014.html

\\ signed k (mod n) in range -floor(n/2)..ceil(n/2)
smod(k,n)=my(m=k%n);if(2*m>n,m-n,m);

\\ componentwise signed mod of gaussian integer
gismod(a,n)=smod(real(a),n)+I*smod(imag(a),n);

\\ gaussian integer w (mod z) 
gimod(w,z)={
  my(u=w*conj(z),n=norml2(z));
  w-z*((u-gismod(u,n))/n)
};
