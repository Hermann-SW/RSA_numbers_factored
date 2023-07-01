## RSA_numbers

Can be found here:  
https://en.wikipedia.org/wiki/RSA_numbers#RSA-100

RSA-100 .. RSA-250 have been factored, with prime factors listed.  
RSA-250 .. RSA-617/RSA-2048 are unfactored sofar.

## msieve

I had forked msieve repo to be able to do exactly identical (sequential) factorizations of RSA numbers on different platforms:  
https://github.com/Hermann-SW/msieve#readme

This was achieved by:  
- add method to pass random generator seed
- modify code that was dependent on CPU cache size

Factoring of RSA-59 .. RSA-110 was done on different systems, listed in the repo.  
Here only runtimes [h] for AMD Ryzen 5 7600X CPU:  

| RSA | runtime [h] |
|----:|--------:|
|  59 | 0:00:01 |
|  79 | 0:01:10 |
| 100 | 1:32:59 |
| 110 |13:43:43 | 


## cado-nfs

"Parts of the Number Field Sieve computation are massively distributed" was the main argument to try cado-nfs  
https://github.com/cado-nfs/cado-nfs  
with my new [PC with 7600X CPU](https://github.com/Hermann-SW/7600x#details-of-pc).

After RSA-100 was factored in less than 8min(!!) with 12 threads on six-core 7600X CPU (down from 1.5h with msieve), I started factoring RSA-129. That completed in 3:11:10h, leaving me puzzled. I started writing this page and factored missing numbers below RSA-129 as well.

| RSA | runtime [h] |
|----:|------------:|
|  59 |    (0:00:27)|
|  79 |     0:01:09 |
| 100 |     0:07:42 |
| 110 |     0:14:50 |
| 120 |     0:57:19 |
| 129 |     3:11:10 |

Factorization end screenshot for RSA-129:  
![RSA-129.3_11_10h.png](RSA-129.3_11_10h.png)

Factorization end screenshot for RSA-100:  
![RSA-100.462s.png](RSA-100.462s.png)
