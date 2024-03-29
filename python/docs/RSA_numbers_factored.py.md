<!-- markdownlint-disable -->

<a href="../../python/RSA_numbers_factored.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `RSA_numbers_factored.py`
For type hinting:
```
IntList2       = NewType('IntList2',       List[Tuple[int, int]])
IntList4       = NewType('IntList4',       List[Tuple[int, int, int, int]])

RSA_factored_2 = NewType('RSA_factored_2',     List[Tuple[int, int, int, int, Dict[int, int], Dict[int, int]]])
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

v1.11 
- add RSA.svg(), rewite RSA_svg demos 
- make validate() functions to enable/disable output 
- add RSA.sort_factors(), new demos 
- complete Python doc for sections 4+5, new section 6 
- functional parity for Python, JavaScript/nodejs and PARI/GP implementations 
- add RSA.unfactored(mod4=-1) 
- add to_sqrtm1() 
- add to_squares_sum() 
- add p-1/q-1 factorization dictionaries for RSA-230..RSA-250 (.py/.js/.gp) 
- make use of cypari2 if available, initially for using ".halfgcd(()" 
- improve doc 
- new RSA_svg.py demo 
- improve markdown 

v1.10 
- add uniq arg to RSA().square_sums() 
- add smp1m4 list of primes =1 (mod 4) less than 1000 
- add sqtst() 
- add lazydocs doc with Makefile fixing Example[s] bugs, docstrings up to and including SECTION03 
- add sq2d() 
- add MicroPython version 
- add square_sums_4() 
- avoid redundant return type in "Returns:", now lazydocs Makefile handles that 
- completed documentation, fix small typos, correct some hinting types, new examples 
- Todo: show lazydocs class member functions as "method" and not as "function" 
- New makefile doc|pylint|validate targets 
- "make pylint" clean (top line disable and pylint options) 
- make sure every function/method gets called at least once in validation 
- pylint warning related simplifications 
- "validate" target to compare with "validate.good", new "black" target 
- code formatting now with "black", results in need for --max-module-lines=2500 
- new "doc_diff" target 
- blacked Pydroid3 demo, then made pylint clean 
- updated both README.md, added table of contents 

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
- **pari**
- **smp1m4**
- **rsa**

---

<a href="../../python/RSA_numbers_factored.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION0`

```python
SECTION0()
```

int helper functions 


---

<a href="../../python/RSA_numbers_factored.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../../python/RSA_numbers_factored.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../../python/RSA_numbers_factored.py#L197"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION1`

```python
SECTION1()
```

Robert Chapman 2010 code from https://math.stackexchange.com/a/5883/1084297 with small changes: 
- asserts instead bad case returns 
- renamed root4() to root4m1() indicating which 4th root gets determined 
- made sq2() return tuple with positive numbers; before sq2(13) returned (-3,-2) 
- sq2(p) result can be obtained from sympy.solvers.diophantine.diophantine by diop_DN(-1, p)[0] 


---

<a href="../../python/RSA_numbers_factored.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `mods`

```python
mods(a: int, n: int) → int
```

returns "signed" a (mod n), in range -n//2..n//2 


---

<a href="../../python/RSA_numbers_factored.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `powmods`

```python
powmods(a: int, r: int, n: int) → int
```

returns "signed" a**r (mod n), in range -n//2..n//2 


---

<a href="../../python/RSA_numbers_factored.py#L230"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `quos`

```python
quos(a: int, n: int) → int
```

returns equivalent of "a//n" for signed mod 


---

<a href="../../python/RSA_numbers_factored.py#L236"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `grem`

```python
grem(w: Tuple[int, int], z: Tuple[int, int]) → Tuple[int, int]
```

returns remainder in Gaussian integers when dividing w by z 


---

<a href="../../python/RSA_numbers_factored.py#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `ggcd`

```python
ggcd(w: Tuple[int, int], z: Tuple[int, int]) → Tuple[int, int]
```

returns greatest common divisor for gaussian integers 



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

<a href="../../python/RSA_numbers_factored.py#L268"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `root4m1`

```python
root4m1(p: int) → int
```

returns sqrt(-1) (mod p) 


---

<a href="../../python/RSA_numbers_factored.py#L282"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sq2`

```python
sq2(p: int) → Tuple[int, int]
```



**Args:**
 
 - <b>`p`</b>:  asserts if p is no prime =1 (mod 4). 

**Returns:**
 
 -   pair of numbers, their squares summing up to p. 

**Example:**

 Determine unique sum of two squares for prime 233.
```
    >>> sq2(233)
    (13, 8)
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L303"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION2`

```python
SECTION2()
```

Functions dealing with representations of int as sum of two squares 


---

<a href="../../python/RSA_numbers_factored.py#L310"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sq2d`

```python
sq2d(p: int) → Tuple[int, int]
```



**Args:**
 
 - <b>`p`</b>:  asserts if not odd prime. 

**Returns:**
 
 -   pair of numbers, with difference of their squares being p. 

**Example:**

 Determine unique difference of two squares for prime 11 (= 6\*\*2 - 5\*\*2).
```
    >>> sq2d(11)
    (6, 5)
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L329"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sum_prod`

```python
square_sum_prod(n: Union[int, RSA_number]) → Union[IntList2, IntList4]
```



**Args:**
 
 - <b>`n`</b>:  int or RSA_number. 

**Returns:**
 
 -   int list with squares of pairs of ints sum up to prime, prime[s] multiply to n. 

**Example:**

 For prime 233 and composite number RSA-59.
```
    >>> square_sum_prod(233)
    [13, 8]
    >>>
    >>> r = rsa[0]
    >>> s = square_sum_prod(r)
    >>> (s[0]**2 + s[1]**2) * (s[2]**2 + s[3]**2) == r[1]
    True
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L355"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sums_`

```python
square_sums_(s: List[int]) → Type[IntList2]
```



**Args:**
 
 - <b>`s`</b>:  List of int returned by square_sum_prod(n). 

**Returns:**
 
 -   List of int pairs, their squares summing up to n. 

**Example:**

 For composite number RSA-59.
```
    >>> r = rsa[0]
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

<a href="../../python/RSA_numbers_factored.py#L392"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `square_sums`

```python
square_sums(
    L: List[int],
    revt: bool = False,
    revl: bool = False,
    uniq: bool = False
) → Type[IntList2]
```



**Args:**
 
 - <b>`L`</b>:  List of int. 
 - <b>`revt`</b>:  sorting direction for tuples. 
 - <b>`revl`</b>:  sorting direction for list. 
 - <b>`uniq`</b>:  eliminate duplicates if True. 

**Returns:**
 
 -   square_sums_(l) sorted (tuples and list), optionally with duplicates removed. 

**Example:**

 For list corresponding to number  5\*5\*13 (5 = 2\*\*2 + 1\*\*2, 13 = 3\*\*2 + 2\*\*2).
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

<a href="../../python/RSA_numbers_factored.py#L513"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sqtst`

```python
sqtst(L: List[int], k: int, dbg: int = 0) → None
```



**Note:**

> sqtst() verifies that 2**(k-1) == unique #sum_of_squares by many asserts for all k-element subsets of l 

**Args:**
 
 - <b>`L`</b>:  list of distinct primes =1 (mod 4) 
 - <b>`k`</b>:  size of subsets 
 - <b>`dbg`</b>:  0=without debug output, 1-3 with more and more 

**Example:**


```
    >>> smp1m4[0:3]
    [5, 13, 17]
    >>> sqtst(smp1m4[0:3], 2, dbg=3)
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
    >>> sqtst(smp1m4[0:20], 7)
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L574"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_squares_sum`

```python
to_squares_sum(sqrtm1: int, p: int) → Type[IntList2]
```

much faster in case cypari2 is available 

**Args:**
 
 - <b>`sqrtm1`</b>:  sqrt(-1) (mod p). 
 - <b>`p`</b>:  prime p =1 (mod 4). 

**Returns:**
 
 -   sum of squares for p. 

**Example:**


```
    >>> to_squares_sum(11, 61)
    (6, -5)
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L592"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `to_sqrtm1`

```python
to_sqrtm1(xy: Type[IntList2], n: int) → int
```



**Args:**
 
 - <b>`xy`</b>:  xy[0]**2 + xy[1]**2 == n. 
 - <b>`n`</b>:  number =1 (mod 4). 

**Returns:**
 
 -   sqrt(-1) (mod n). 

**Example:**


```
    >>> to_sqrtm1((14,5),221)
    47
    >>> 47**2%221==221-1
    True
    >>>
``` 


---

<a href="../../python/RSA_numbers_factored.py#L611"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION3`

```python
SECTION3()
```

Functions working on "rsa" list 


---

<a href="../../python/RSA_numbers_factored.py#L618"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `idx`

```python
idx(rsa_: List[RSA_number], L: int) → int
```



**Args:**
 
 - <b>`rsa_`</b>:  list of RSA numbers 
 - <b>`L`</b>:  bit-length or decimal-digit-length of RSA number 

**Returns:**
 
 -   index of RSA-l in rsa list, -1 if not found 


---

<a href="../../python/RSA_numbers_factored.py#L632"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `has_factors`

```python
has_factors(
    r: Type[RSA_number],
    mod4: Union[NoneType, int, Tuple[int, int]] = None
) → bool
```



**Args:**
 
 - <b>`r`</b>:  an RSA number 
 - <b>`mod4`</b>:  optional restriction (remainder mod 4 for number or its both prime factors) 

**Returns:**
 
 -   RSA number has factors and adheres mod 4 restriction(s) 


---

<a href="../../python/RSA_numbers_factored.py#L649"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `has_factors_2`

```python
has_factors_2(
    r: Type[RSA_number],
    mod4: Union[NoneType, int, Tuple[int, int]] = None
) → bool
```



**Args:**
 
 - <b>`r`</b>:  an RSA number 
 - <b>`mod4`</b>:  optional restriction (remainder mod 4 for number or its both prime factors) 

**Returns:**
 
 -   RSA number has factors p and q, and factorization dictionaries of p-1 and q-1 

**Example:**

 For RSA-100
```
    >>> r=rsa[2]
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

<a href="../../python/RSA_numbers_factored.py#L682"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `without_factors`

```python
without_factors(r: Type[RSA_number], mod4: Optional[int] = None) → bool
```



**Args:**
 
 - <b>`r`</b>:  an RSA number 
 - <b>`mod4`</b>:  optional restriction (remainder mod 4 for number) 

**Returns:**
 
 -   RSA number has no factors and adheres mod 4 restriction(s) 


---

<a href="../../python/RSA_numbers_factored.py#L695"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION4`

```python
SECTION4()
```

primeprod_f functions, passing p and q instead n=p*q much faster than sympy.f 


---

<a href="../../python/RSA_numbers_factored.py#L701"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `primeprod_totient`

```python
primeprod_totient(p: int, q: int) → int
```



**Args:**
 
 - <b>`p,q`</b>:  odd primes. 

**Returns:**
 
 -   totient(n) with n=p*q. 


---

<a href="../../python/RSA_numbers_factored.py#L711"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `primeprod_reduced_totient`

```python
primeprod_reduced_totient(p: int, q: int) → int
```



**Args:**
 
 - <b>`p,q`</b>:  odd primes. 

**Returns:**
 
 -   reduced_totient(n) with n=p*q. 


---

<a href="../../python/RSA_numbers_factored.py#L721"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION5`

```python
SECTION5()
```

Functions on factorization dictionaries. 

[as returned by sympy.factorint() (in rsa[x][4] for p-1 and rsa[x][5] for q-1) ] 


---

<a href="../../python/RSA_numbers_factored.py#L730"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dict_int`

```python
dict_int(d: Dict[int, int]) → int
```



**Args:**
 
 - <b>`d`</b>:  factorization dictionary. 

**Returns:**
 
 -   n with d = sympy.factorint(n). 


---

<a href="../../python/RSA_numbers_factored.py#L744"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dict_totient`

```python
dict_totient(d: Dict[int, int]) → int
```



**Args:**
 
 - <b>`d`</b>:  factorization dictionary. 

**Returns:**
 
 -   totient(n) with d = sympy.factorint(n). 


---

<a href="../../python/RSA_numbers_factored.py#L760"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dictprod_totient`

```python
dictprod_totient(d1: Dict[int, int], d2: Dict[int, int]) → int
```



**Args:**
 
 - <b>`d1,d2`</b>:  factorization dictionaries. 

**Returns:**
 
 -   totient(n) with n=dict_int(d1)*dict_int(d2). 


---

<a href="../../python/RSA_numbers_factored.py#L770"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dictprod_reduced_totient`

```python
dictprod_reduced_totient(d1: Dict[int, int], d2: Dict[int, int]) → int
```



**Args:**
 
 - <b>`d1,d2`</b>:  factorization dictionaries. 

**Returns:**
 
 -   reduced_totient(n) with n=dict_int(d1)*dict_int(d2). 


---

<a href="../../python/RSA_numbers_factored.py#L780"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `SECTION6`

```python
SECTION6()
```

Validation functions, rsa list 


---

<a href="../../python/RSA_numbers_factored.py#L787"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `validate_squares`

```python
validate_squares() → None
```

avoid R0915 pylint too-many-statements warning for validate() 


---

<a href="../../python/RSA_numbers_factored.py#L823"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `validate`

```python
validate(rsa_, doprint: bool = False) → None
```

Assert many identities to assure data consistency and generate demo output for non RSA-class functionality. Gets executed by [RSA().validate()](#function-validate-1). 

**Args:**
 
 - <b>`rsa_`</b>:  list of rsa entries. 


---

## <kbd>class</kbd> `RSA`
RSA convenience class. 

<a href="../../python/RSA_numbers_factored.py#L1577"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__()
```

avoid W0201 pylint warning 




---

<a href="../../python/RSA_numbers_factored.py#L1627"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `factored`

```python
factored(mod4: Union[NoneType, int, Tuple[int, int]] = None) → Type[IntList4]
```



**Args:**
 
 - <b>`mod4`</b>:  optional restriction (remainder mod 4 for number or its both prime factors). 

**Returns:**
 
 -   list of RSA_number being factored and satisfying mod4 restriction 

**Example:**


```
    >>> len(rsa)
    56
    >>> len(RSA.factored())
    25
    >>> len(RSA.factored(mod4=3))
    13
    >>> len(RSA.factored(mod4=1))
    12
    >>> len(RSA.factored(mod4=(1,1)))
    5
    >>> len(RSA.factored(mod4=(3,3)))
    7
    >>>
``` 

---

<a href="../../python/RSA_numbers_factored.py#L1654"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `factored_2`

```python
factored_2(
    mod4: Union[NoneType, int, Tuple[int, int]] = None
) → List[RSA_number]
```



**Args:**
 
 - <b>`mod4`</b>:  optional restriction (remainder mod 4 for number or its both prime factors). 

**Returns:**
 
 -   list of RSA_number with factorization dictionaries. 

---

<a href="../../python/RSA_numbers_factored.py#L1604"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get`

```python
get(x: int) → Type[RSA_number]
```



**Args:**
 
 - <b>`x`</b>:  RSA number length. 

**Returns:**
 
 -   RSA-x from rsa list, asserts if not found. 

---

<a href="../../python/RSA_numbers_factored.py#L1615"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_`

```python
get_(x: Union[int, RSA_number]) → Type[RSA_number]
```



**Args:**
 
 - <b>`x`</b>:  RSA number length or RSA_number. 

**Returns:**
 
 -   identity or RSA-x from rsa list. 

---

<a href="../../python/RSA_numbers_factored.py#L1595"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `index`

```python
index(x: int) → int
```



**Args:**
 
 - <b>`x`</b>:  bit-length or decimal-digit-length of RSA number. 

**Returns:**
 
 -   index of RSA-x in rsa list, -1 if not found. 

---

<a href="../../python/RSA_numbers_factored.py#L1700"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `reduced_totient`

```python
reduced_totient(x: Union[int, RSA_number]) → int
```



**Args:**
 
 - <b>`x`</b>:  RSA number length or RSA_number. 

**Returns:**
 
 -   reduced_totient(x). 

---

<a href="../../python/RSA_numbers_factored.py#L1724"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `reduced_totient_2`

```python
reduced_totient_2(x: Union[int, RSA_number]) → int
```



**Args:**
 
 - <b>`x`</b>:  RSA number length or RSA_number. 

**Returns:**
 
 -   apply reduced_totient function to reduced_totient(x). 

---

<a href="../../python/RSA_numbers_factored.py#L1860"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `sort_factors`

```python
sort_factors() → None
```

make p the bigger of factors by switching if needed 

---

<a href="../../python/RSA_numbers_factored.py#L1736"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `square_diffs`

```python
square_diffs(x: Union[int, RSA_number]) → Type[IntList2]
```



**Args:**
 
 - <b>`x`</b>:  RSA number length or RSA_number. 

**Returns:**
 
 -   two differences of squares resulting in x. 

**Example:**


```
    >>> t = RSA.get(250)
    >>> n = t[1]
    >>> [a,b],[c,d] = RSA.square_diffs(t)
    >>> (a**2 - b**2) == n and (c**2 - d**2) == n
    True
    >>>
``` 

---

<a href="../../python/RSA_numbers_factored.py#L1760"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `square_sums`

```python
square_sums(x: Union[int, RSA_number]) → Type[IntList2]
```



**Args:**
 
 - <b>`x`</b>:  RSA number length or RSA_number. 

**Returns:**
 
 -   two different sums of squares resulting in x. 

**Example:**


```
    >>> t = RSA.get(129)
    >>> n = t[1]
    >>> [a,b],[c,d] = RSA.square_sums(t)
    >>> (a**2 + b**2) == n and (c**2 + d**2) == n
    True
    >>> len({a,b,c,d})
    4
    >>>
``` 

---

<a href="../../python/RSA_numbers_factored.py#L1784"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `square_sums_4`

```python
square_sums_4(x: Union[int, RSA_number]) → Tuple[int, int, int, int]
```



**Args:**
 
 - <b>`x`</b>:  RSA_number length or RSA_number 

**Returns:**
 
 -   square sums of tuple elements sum up to RSA number 

**Example:**


```
    >>> p,q = 13,29
    >>> n = p*q
    >>> sq4 = RSA.square_sums_4([0,0,p,q])
    >>> sq4
    (15, 4, 6, 10)
    >>> sum([x**2 for x in sq4]) == n
    True
    >>> sum([x**2 for x in RSA.square_sums_4(129)]) == RSA.get(129)[1]
    True
    >>> RSA.square_sums_4(59)
    (179348979911745603741332779404, 85487774497975933628103176206, 105946792191696573364448656521, 144715520252806281192691658344)
    >>>
``` 

---

<a href="../../python/RSA_numbers_factored.py#L1823"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `svg`

```python
svg(n: Union[int, RSA_number], scale: int) → str
```

Generate prime factors svg. 

---

<a href="../../python/RSA_numbers_factored.py#L1815"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `to_sqrtm1`

```python
to_sqrtm1(xy: Type[IntList2], p: int) → int
```

shortcut 

---

<a href="../../python/RSA_numbers_factored.py#L1819"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `to_squares_sum`

```python
to_squares_sum(sqrtm1: int, p: int) → Type[IntList2]
```

shortcut 

---

<a href="../../python/RSA_numbers_factored.py#L1688"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `totient`

```python
totient(x: Union[int, RSA_number]) → int
```



**Args:**
 
 - <b>`x`</b>:  RSA number length or RSA_number. 

**Returns:**
 
 -   totient(x). 

---

<a href="../../python/RSA_numbers_factored.py#L1712"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `totient_2`

```python
totient_2(x: Union[int, RSA_number]) → int
```



**Args:**
 
 - <b>`x`</b>:  RSA number length or RSA_number. 

**Returns:**
 
 -   apply totient function to totient(x). 

---

<a href="../../python/RSA_numbers_factored.py#L1665"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `unfactored`

```python
unfactored(mod4: Optional[int] = None) → Type[IntList2]
```



**Args:**
 
 - <b>`mod4`</b>:  optional restriction (remainder mod 4 for number). 

**Returns:**
 
 -   list of RSA_number being unfactored and satisfying mod4 restriction 

**Example:**


```
    >>> len(rsa)
    56
    >>> len(RSA.factored())
    25
    >>> len(RSA.unfactored())
    31
    >>> len(RSA.unfactored(1))
    17
    >>> len(RSA.unfactored(3))
    14
    >>>
``` 

---

<a href="../../python/RSA_numbers_factored.py#L1871"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `validate`

```python
validate(doprint: bool = False) → None
```

Assert many identities to assure data consistency and optionally generate demo output  (executed if \_\_name\_\_ == "\_\_main\_\_"). 

**Example:**


```
     $ python RSA_numbers_factored.py

     with p-1 and q-1 factorizations (n=p*q): 25
      59 digits, 79 digits,100 digits,110 digits,120 digits,129 digits,130 digits,
     140 digits,150 digits,155 digits,160 digits,170 digits,576 bits  ,180 digits,
     190 digits,640 bits  ,200 digits,210 digits,704 bits  ,220 digits,230 digits,
     232 digits,768 bits  ,240 digits,250 digits,

     without (p-1) and (q-1) factorizations, but p and q: 0

     have not been factored sofar: 31
     260 digits,270 digits,896 bits  ,280 digits,290 digits,300 digits,309 digits,
     1024 bits  ,310 digits,320 digits,330 digits,340 digits,350 digits,360 digits,
     370 digits,380 digits,390 digits,400 digits,410 digits,420 digits,430 digits,
     440 digits,450 digits,460 digits,1536 bits  ,470 digits,480 digits,490 digits,
     500 digits,617 digits,2048 bits  (=617 digits)

     $
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
