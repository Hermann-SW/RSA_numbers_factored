#!/usr/bin/env node

const fs = require('fs');

function powmod(a, e, m){
  if (e == 0n)  return 1n;
  if (e == 1n)  return a % m;
  var p = powmod(a, e >> 1n, m);
  p = (e % 2n == 1n) ? p*p*a : p*p;
  return p % m;
}

p=516693n**1048576n
p=p**2n-p+1n

fs.readFile('sqrtm1.gp', 'utf8', (err, data) => {
  console.log(powmod(BigInt(data),2n,p)===p-1n)
});

fs.readFile('sos.gp', 'utf8', (err, data) => {
  [x,y]=data.split(",")
  x=BigInt(x.replace('[',''))
  y=BigInt(y.replace(']',''))
  console.log(x*x+y*y===p)
});
