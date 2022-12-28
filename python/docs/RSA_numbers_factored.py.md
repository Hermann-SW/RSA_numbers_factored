<!-- markdownlint-disable -->

<a href="../../python/RSA_numbers_factored.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `RSA_numbers_factored.py`

- add uniq arg to RSA().square_sums() 
- add smp1m4 array of primes =1 (mod 4) less than 1000 
- add sqtst() 

v1.9 
- remove not needed anymore RSA(). \_\_init\_\_() 
- add RSA().square_sums() 
- manual transpilation to RSA_numbers_factored.js 
- new home in RSA_numbers_factored repo python directory 
- gist now is pointer to new home only 
- add HTML demos making use of transpiled RSA_numbers_factored.js 

v1.8 
- include Robin Chapman code to determine prime p=1 (mod 4) sum of squares 
- make few changes, documented in that code section 
- make square_sum_prod base on sq2, eliminate subprocess.Popen() 
- remove RSA().square_sum_prod because not needed anymore 
- remove Popen and Pipe import  

v1.7 
- add "mod4" attribute to "has_factors()" and "RAS().factored()" 
    - default None selects all 
    - int value specifies remainder "mod 4" to be selected 
    - tuple specifies remainders "mod 4" for prime factores to be selected 
- remove "has_factors_1_1(_)", use "has_factors(_, mod4=(1,1))" instead 
- remove "RSA().factored_1_1()", use "RSA().factored(mod4=(1,1))" 
- add "RSA().square_diffs()" for returning two pairs 

v1.6 
- enable square_sum_prod() functions to deal with primefactors in array 
- add asserts enforcing "=1 (mod 4)" for square_sum_prod() functions 
- add has_factors_1_1() [returns whether both primefactors are "=1 (mod4)"] 
- add RSA().factored_1_1() based on that 

v1.5 
- add square_sums() for converting square_sum_prod output of composite number 
- add square_sums() assertions 

v1.4 
- add RSA.square_sum_prod(), using Popen() pipe for >1 calls  

v1.3 
- add square_sum_prod(), for use see: 
- https://github.com/Hermann-SW/square_sum_prod/blob/master/Popen.py 

v1.2 
- improve has_factors() and has_factors_2() 
- correct RSA().factored() to always return 4-tuples 

v1.1 
- removed not needed imports 
- added has_factors/has_factors_2 functions and used them everywwhere 
- resolved the RSA-190 assertion issue, using reduced_  works for all 
- added RSA convenience class 
- added some RSA class assertions for validation 
- RSA class factored() returns all RSA number tupels having factors 
- RSA class factored_2() returns all RSA number tupels p-1/q-1 factorizations 

v1.0 
- added primeprod_ functions 
- added factorization dictionaries for (p-1) and (q-1) of RSA-59 ... RSA-220 
- added Wikipedia RSA numbers that have not been factored sofar as well 
- added dict_ functions 
- added dictprod_ functions 
- added dict_totient and dictprod_totient assertions  [ mod phi(phi(n)) ] 
- added comments 

v0.2 
- added ind(rsa, x) function, returning index in rsa of RSA-x number 

v0.1 
- initial version, with bits(), digits(), rsa array and main() testing 

**Global Variables**
---------------
- **smp1m4**
- **rsa**

---

<a href="../../python/RSA_numbers_factored.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION0`

```python
SECTION0()
```

int helper functions  




---

<a href="../../python/RSA_numbers_factored.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bits`

```python
bits(n: int) → int
```

returns number of 1-bits in n 


---

<a href="../../python/RSA_numbers_factored.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `digits`

```python
digits(n: int) → int
```

returns number of decimal digits of n 


---

<a href="../../python/RSA_numbers_factored.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION1`

```python
SECTION1()
```

Robert Chapman 2010 code from https://math.stackexchange.com/a/5883/1084297 with small changes: 
- asserts instead bad case returns 
- renamed root4() to root4m1() indicating which 4th root gets determined 
- made sq2() return tuple with positive numbers; before sq2(13) = (-3,-2) 


---

<a href="../../python/RSA_numbers_factored.py#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `mods`

```python
mods(a: int, n: int) → int
```



**Args:**
 
 - <b>`a`</b>:  any int 
 - <b>`n`</b>:  modulus 

**Returns:**
 
 - <b>`int`</b>:  "signed mod" of a (mod n), in range -n//2..n//2 


---

<a href="../../python/RSA_numbers_factored.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `powmods`

```python
powmods(a: int, r: int, n: int) → int
```

return "signed" a**r (mod n), in range -n//2..n//2 


---

<a href="../../python/RSA_numbers_factored.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `quos`

```python
quos(a: int, n: int) → int
```

returns "a//n" 


---

<a href="../../python/RSA_numbers_factored.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `grem`

```python
grem(w: tuple, z: tuple) → tuple
```

remainder in Gaussian integers when dividing w by z 


---

<a href="../../python/RSA_numbers_factored.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `ggcd`

```python
ggcd(w: tuple, z: tuple) → tuple
```

gcd() for gaussian integers 


---

<a href="../../python/RSA_numbers_factored.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `root4m1`

```python
root4m1(p: int) → int
```



**Args:**
 
 - <b>`p`</b>:  module 

**Returns:**
 
 - <b>`int`</b>:  sqrt(-1) (mod p) 


---

<a href="../../python/RSA_numbers_factored.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sq2`

```python
sq2(p: int) → Tuple[int, int]
```



**Args:**
 
 - <b>`p`</b>:  prime p=1 (mod 4), asserts if not 

**Returns:**
 
 - <b>`Tuple[int, int]`</b>:  the squares of two ints sum up to p 

**Examples:**
 This is how it is used. ``` print(sq2(233))```
    (13, 8)
    >>>



---

<a href="../../python/RSA_numbers_factored.py#L186"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION2`

```python
SECTION2()
```

Functions dealing with representations of int as sum of two squares  




---

<a href="../../python/RSA_numbers_factored.py#L191"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sum_prod`

```python
square_sum_prod(n)
```






---

<a href="../../python/RSA_numbers_factored.py#L198"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sums_`

```python
square_sums_(s)
```






---

<a href="../../python/RSA_numbers_factored.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sums`

```python
square_sums(l, revt=False, revl=False, uniq=False)
```






---

<a href="../../python/RSA_numbers_factored.py#L227"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sqtst`

```python
sqtst(l, k, dbg=0)
```






---

<a href="../../python/RSA_numbers_factored.py#L238"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION3`

```python
SECTION3()
```

Functions working on "rsa" array  




---

<a href="../../python/RSA_numbers_factored.py#L243"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `idx`

```python
idx(rsa, l)
```






---

<a href="../../python/RSA_numbers_factored.py#L249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `has_factors`

```python
has_factors(r, mod4=None)
```






---

<a href="../../python/RSA_numbers_factored.py#L256"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `has_factors_2`

```python
has_factors_2(r)
```






---

<a href="../../python/RSA_numbers_factored.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION4`

```python
SECTION4()
```

primeprod_f functions, passing p and q instead n=p*q much faster than sympy.f  




---

<a href="../../python/RSA_numbers_factored.py#L263"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `primeprod_totient`

```python
primeprod_totient(p, q)
```






---

<a href="../../python/RSA_numbers_factored.py#L266"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `primeprod_reduced_totient`

```python
primeprod_reduced_totient(p, q)
```






---

<a href="../../python/RSA_numbers_factored.py#L270"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION5`

```python
SECTION5()
```

Functions on factorization dictionaries. 

[as returned by sympy.factorint() (in rsa[x][4] for p-1 and rsa[x][5] for q-1) ]  




---

<a href="../../python/RSA_numbers_factored.py#L277"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dict_int`

```python
dict_int(d)
```






---

<a href="../../python/RSA_numbers_factored.py#L284"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dict_totient`

```python
dict_totient(d)
```






---

<a href="../../python/RSA_numbers_factored.py#L294"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dictprod_totient`

```python
dictprod_totient(d1, d2)
```






---

<a href="../../python/RSA_numbers_factored.py#L297"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dictprod_reduced_totient`

```python
dictprod_reduced_totient(d1, d2)
```






---

<a href="../../python/RSA_numbers_factored.py#L303"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main(rsa)
```






---

## <kbd>class</kbd> `RSA`







---

<a href="../../python/RSA_numbers_factored.py#L480"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `factored`

```python
factored(mod4=None)
```





---

<a href="../../python/RSA_numbers_factored.py#L483"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `factored_2`

```python
factored_2()
```





---

<a href="../../python/RSA_numbers_factored.py#L469"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get`

```python
get(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L474"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_`

```python
get_(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L466"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `index`

```python
index(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L491"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `reduced_totient`

```python
reduced_totient(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L501"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `reduced_totient_2`

```python
reduced_totient_2(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L506"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `square_diffs`

```python
square_diffs(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L513"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `square_sums`

```python
square_sums(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L486"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `totient`

```python
totient(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L496"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `totient_2`

```python
totient_2(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L518"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `validate`

```python
validate()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
