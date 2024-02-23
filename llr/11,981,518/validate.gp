p=polcyclo(3,-516693^1048576);

s=readvec("sqrtm1.gp")[1];
s^2%p==p-1
##

[x,y]=readvec("sos.gp")[1];
x^2+y^2==p
##
