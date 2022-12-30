<!-- markdownlint-disable -->

<a href="../../python/RSA_numbers_factored.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `RSA_numbers_factored.py`
For type hinting:
```
IntList2       = NewType('IntList2',       List[Tuple[int, int]])
IntList4       = NewType('IntList4',       List[Tuple[int, int, int, int]])

RSA_factored_2 = NewType('RSA_factored_2', List[Tuple[int, int, int, int, Dict[int, int], Dict[int, int]]])
RSA_factored   = NewType('RSA_factored',   IntList4)
RSA_unfactored = NewType('RSA_unfactored', IntList2)

RSA_number     = NewType('RSA_number',     Union[RSA_factored_2, RSA_factored, RSA_unfactored])
``` 

RSA number n = RSA-l:
```
RSA_unfactored:  [l,n]
RSA_factored:    [l,n,p,q]           (n = p * q)
RSA_factored_2:  [l,n,p,q,pm1,qm1]   (n = p * q, Xm1 factorization dict of X-1)
``` 



(v1.10) 
- add uniq arg to RSA().square_sums() 
- add smp1m4 list of primes =1 (mod 4) less than 1000 
- add sqtst() 
- add lazydocs doc with Makefile fixing Example[s] bugs, docstrings up to and including SECTION03 
- add sq2d() 

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
- enable square_sum_prod() functions to deal with primefactors in list 
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
- initial version, with bits(), digits(), rsa list and main() testing 



Global variable descriptions: 
- small primes =1 (mod 4) less than 1000 
- list of RSA numbers 

**Global Variables**
---------------
- **smp1m4**
- **rsa**

---

<a href="../../python/RSA_numbers_factored.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION0`

```python
SECTION0()
```

int helper functions 


---

<a href="../../python/RSA_numbers_factored.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bits`

```python
bits(n: int) → int
```

returns bit-length of n 



**Example:**

  Of biggest RSA number.
```
     >>> bits(rsa[-1][1])
     2048
     >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `digits`

```python
digits(n: int) → int
```

returns number of decimal digits of n 



**Example:**

  Of biggest RSA number.
```
     >>> digits(rsa[-1][1])
     617
     >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION1`

```python
SECTION1()
```

Robert Chapman 2010 code from https://math.stackexchange.com/a/5883/1084297 with small changes: 
- asserts instead bad case returns 
- renamed root4() to root4m1() indicating which 4th root gets determined 
- made sq2() return tuple with positive numbers; before sq2(13) returned (-3,-2) 


---

<a href="../../python/RSA_numbers_factored.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `mods`

```python
mods(a: int, n: int) → int
```

returns "signed" a (mod n), in range -n//2..n//2 


---

<a href="../../python/RSA_numbers_factored.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `powmods`

```python
powmods(a: int, r: int, n: int) → int
```

return "signed" a**r (mod n), in range -n//2..n//2 


---

<a href="../../python/RSA_numbers_factored.py#L179"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `quos`

```python
quos(a: int, n: int) → int
```

returns equivalent of "a//n" for signed mod 


---

<a href="../../python/RSA_numbers_factored.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `grem`

```python
grem(w: Tuple[int, int], z: Tuple[int, int]) → Tuple[int, int]
```

returns remainder in Gaussian integers when dividing w by z 


---

<a href="../../python/RSA_numbers_factored.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `ggcd`

```python
ggcd(w: Tuple[int, int], z: Tuple[int, int]) → Tuple[int, int]
```

returns greatest common divisorfor gaussian integers 



**Example:**

  Demonstrates how ggcd() can be used to determine sum of squares.
```
     >>> powmods(13,2,17)

        -1
     >>> ggcd((17,0),(13,1))
     (4, -1)
     >>> 4**2+(-1)**2
     17
     >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L215"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `root4m1`

```python
root4m1(p: int) → int
```

returns sqrt(-1) (mod p) 


---

<a href="../../python/RSA_numbers_factored.py#L228"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sq2`

```python
sq2(p: int) → Tuple[int, int]
```



**Args:**
 
 - <b>`p`</b>:  asserts if not prime =1 (mod 4). 

**Returns:**
 
 - <b>`Tuple[int, int]`</b>:  the squares of ints sum up to p. 

**Example:**

 Determine unique sum of two squares for prime 233.
```
    >>> sq2(233)
    (13, 8)
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L248"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION2`

```python
SECTION2()
```

Functions dealing with representations of int as sum of two squares 


---

<a href="../../python/RSA_numbers_factored.py#L254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sq2d`

```python
sq2d(p: int) → Tuple[int, int]
```



**Args:**
 
 - <b>`p`</b>:  asserts if not odd prime. 

**Returns:**
 
 - <b>`Tuple[int, int]`</b>:  the squares of ints difference is p. 

**Example:**

 Determine unique difference of two squares for prime 11 (= 6\*\*2 - 5\*\*2).
```
    >>> sq2d(11)
    (6, 5)
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L272"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sum_prod`

```python
square_sum_prod(n: Union[int, RSA_number]) → Union[IntList2, IntList4]
```



**Args:**
 
 - <b>`n`</b>:  int or RSA_number. 

**Returns:**
 
 - <b>`Union[IntList2, IntList4]`</b>:  squares of pairs of ints sum up to prime, prime[s] multiply to n. 

**Example:**

 For prime 233 and composite number RSA-59.
```
    >>> square_sum_prod(233)
    [13, 8]
    >>>
    >>> r = RSA.get(59)
    >>> s = square_sum_prod(r)
    >>> (s[0]**2 + s[1]**2) * (s[2]**2 + s[3]**2) == r[1]
    True
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L297"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sums_`

```python
square_sums_(s: List[int]) → List[int]
```



**Args:**
 
 - <b>`s`</b>:  List of int returned by square_sum_prod(). 

**Returns:**
 
 - <b>`List[int]`</b>:  squares of pairs of ints sum up to prime, prime[s] multiply to n. 

**Example:**

 For composite number RSA-59.
```
    >>> r = RSA.get(59)
    >>> s = square_sum_prod(r)
    >>> square_sums_(s)
    [[93861205413769670113229603198, 250662312444502854557140314865], [264836754409721537369435955610, 38768728061109707828243001823]]
    >>> for a,b in square_sums_(s):
    ...     a**2 + b**2 == r[1]
    ...
    True
    True
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L331"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sums`

```python
square_sums(
    l: List[int],
    revt: bool = False,
    revl: bool = False,
    uniq: bool = False
) → List[IntList2]
```



**Args:**
 
 - <b>`l`</b>:  List of int. 
 - <b>`revt`</b>:  sorting direction for tuples. 
 - <b>`revl`</b>:  sorting direction for list. 
 - <b>`uniq`</b>:  eliminate duplicates if True. 

**Returns:**
 
 - <b>`List[IntList2]`</b>:  square_sums_(s) sorted (tuples and list), optional duplicates removed. 

**Example:**

 For list corresponding to number 5\*5\*13 (5 = 2**2 + 1**2, 13 = 3**2 + 1**2).
```
    >>> s = [2, 1, 2, 1, 3, 2]
    >>> square_sums(s)
    [[1, 18], [6, 17], [10, 15], [10, 15]]
    >>> square_sums(s, revt=True, revl=True)
    [[18, 1], [17, 6], [15, 10], [15, 10]]
    >>> square_sums(s, uniq=True)
    [[1, 18], [6, 17], [10, 15]]
    >>> for a,b in square_sums(s, uniq=True):
    ...     assert a**2 + b**2 == 5*5*13
    ...
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L370"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sqtst`

```python
sqtst(l: List[int], k: int, dbg: int = 0) → None
```



**Note:**

> sqtst() verifies that 2**(k-1) == unique #sum_of_squares by many asserts for all k-element subsets of l 

**Args:**
 
 - <b>`l`</b>:  list of distinct primes =1 (mod 4) 
 - <b>`k`</b>:  size of subsets 
 - <b>`dbg`</b>:  0=without debug output, 1-3 with more and more 

**Example:**


```
    >>> smp1m4[slice(3)]
    [5, 13, 17]
    >>> sqtst(smp1m4[slice(3)], 2, dbg=3)
    (0, 1)
    [2, 1, 3, 2]
    [[1, 8], [4, 7]]
    (0, 2)
    [2, 1, 4, 1]
    [[2, 9], [6, 7]]
    (1, 2)
    [3, 2, 4, 1]
    [[5, 14], [10, 11]]
    >>> 
    >>> sqtst(smp1m4[slice(20)], 7)
    >>> 
``` 


---

<a href="../../python/RSA_numbers_factored.py#L407"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION3`

```python
SECTION3()
```

Functions working on "rsa" list 


---

<a href="../../python/RSA_numbers_factored.py#L412"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `idx`

```python
idx(rsa: List[RSA_number], l: int) → int
```



**Args:**
 
 - <b>`rsa`</b>:  list of RSA numbers 
 - <b>`l`</b>:  bit-length or decimal-digit-length of RSA number 

**Returns:**
 
 - <b>`int`</b>:  index of RSA-l in rsa list, -1 if not found 


---

<a href="../../python/RSA_numbers_factored.py#L425"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `has_factors`

```python
has_factors(
    r: Type[RSA_number],
    mod4: Union[NoneType, int, Tuple[int, int]] = None
) → bool
```



**Args:**
 
 - <b>`r`</b>:  an RSA number 
 - <b>`mod4`</b>:  optional resriction or remainder mod 4 for number or its both prome factors 

**Returns:**
 
 - <b>`bool`</b>:  RSA number has factors, and adheres mod 4 restriction(s) 


---

<a href="../../python/RSA_numbers_factored.py#L439"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `has_factors_2`

```python
has_factors_2(r: Type[RSA_number]) → bool
```



**Args:**
 
 - <b>`r`</b>:  an RSA number 

**Returns:**
 
 - <b>`bool`</b>:  RSA number has factors p and q, and factorizations of p-1 and q-1 

**Example:**


```
    >>> r=RSA.get(100)
    >>> has_factors_2(r)
    True
    >>> l,n,p,q,pm1,qm1 = r
    >>> l
    100
    >>> 
    >>> q
    40094690950920881030683735292761468389214899724061
    >>> qm1
    {2: 2, 5: 1, 41: 1, 2119363: 1, 602799725049211: 1, 38273186726790856290328531: 1}
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L463"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION4`

```python
SECTION4()
```

primeprod_f functions, passing p and q instead n=p*q much faster than sympy.f 


---

<a href="../../python/RSA_numbers_factored.py#L467"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `primeprod_totient`

```python
primeprod_totient(p, q)
```






---

<a href="../../python/RSA_numbers_factored.py#L470"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `primeprod_reduced_totient`

```python
primeprod_reduced_totient(p, q)
```






---

<a href="../../python/RSA_numbers_factored.py#L474"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION5`

```python
SECTION5()
```

Functions on factorization dictionaries. 

[as returned by sympy.factorint() (in rsa[x][4] for p-1 and rsa[x][5] for q-1) ] 


---

<a href="../../python/RSA_numbers_factored.py#L481"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dict_int`

```python
dict_int(d)
```






---

<a href="../../python/RSA_numbers_factored.py#L488"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dict_totient`

```python
dict_totient(d)
```






---

<a href="../../python/RSA_numbers_factored.py#L498"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dictprod_totient`

```python
dictprod_totient(d1, d2)
```






---

<a href="../../python/RSA_numbers_factored.py#L501"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dictprod_reduced_totient`

```python
dictprod_reduced_totient(d1, d2)
```






---

<a href="../../python/RSA_numbers_factored.py#L507"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main(rsa)
```






---

## <kbd>class</kbd> `RSA`







---

<a href="../../python/RSA_numbers_factored.py#L684"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `factored`

```python
factored(mod4=None)
```





---

<a href="../../python/RSA_numbers_factored.py#L687"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `factored_2`

```python
factored_2()
```





---

<a href="../../python/RSA_numbers_factored.py#L673"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get`

```python
get(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L678"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_`

```python
get_(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L670"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `index`

```python
index(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L695"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `reduced_totient`

```python
reduced_totient(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L705"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `reduced_totient_2`

```python
reduced_totient_2(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L710"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `square_diffs`

```python
square_diffs(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L717"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `square_sums`

```python
square_sums(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L690"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `totient`

```python
totient(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L700"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `totient_2`

```python
totient_2(x)
```





---

<a href="../../python/RSA_numbers_factored.py#L722"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `validate`

```python
validate()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
