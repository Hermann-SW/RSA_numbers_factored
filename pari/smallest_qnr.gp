if (getenv("n") == 0, print(\
  "Format: n=\"value\"  gp -q < smallest_qnr.gp\n"\
  "10000/36401/100355/200700/272770/330855/388342-digit number examples:\n"\
  "n=\"(10 ^ 10000 - 1) \\ 3 - 10 ^ 6333\"\n"\
  "n=\"34*((10^36400-1)\\9)-42000040044444004000024*10^2264*((10^36400-1)\\9)\\\((10^4550-1)\\9)-1\"\n"\
  "n=\"65516468355 * 2 ^ 333333 + 1\"\n"\
  "n=\"3756801695685 * 2 ^ 666669 + 1\"\n"\
  "n=\"1705 * 2 ^ 906110 + 1\"\n"\
  "n=\"2145 * 2 ^ 1099064 + 1\"\n"\
  "n=\"2996863034895 * 2 ^ 1290000 + 1\"");\
quit);

n = eval(getenv("n"));
print("n is ", #digits(n),"-digit number");

smallest_qnr(m) = { forprime(t=2, oo, if(kronecker(t, m)==-1, return(t))); }

nr = smallest_qnr(n);
##
print("smallest quadratic non-residue of n: ", nr);
