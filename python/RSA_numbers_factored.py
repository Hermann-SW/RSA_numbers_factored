# pylint: disable=C0103, I1101
#                 invalid-name, c-extension-no-member
"""
For type hinting:
```
IntList2       = NewType('IntList2',       List[Tuple[int, int]])
IntList4       = NewType('IntList4',       List[Tuple[int, int, int, int]])

RSA_factored_2 = NewType('RSA_factored_2', \
    List[Tuple[int, int, int, int, Dict[int, int], Dict[int, int]]])
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
- remove not needed anymore RSA(). \\_\\_init\\_\\_()
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
"""
from math import log2, log10
from itertools import combinations, chain
from typing import Tuple, List, Union, Dict, NewType, Type
from sympy.ntheory import isprime, jacobi_symbol
from sympy.ntheory import jacobi_symbol as kronecker
from sympy import lcm, gcd, I

try:
    import cypari2

    pari = cypari2.Pari()
    gen_to_python = cypari2.convert.gen_to_python
except ImportError:
    cypari2 = None

IntList2 = NewType("IntList2", List[Tuple[int, int]])
IntList4 = NewType("IntList4", List[Tuple[int, int, int, int]])

RSA_factored_2 = NewType(
    "RSA_factored_2", List[Tuple[int, int, int, int, Dict[int, int], Dict[int, int]]]
)
RSA_factored = NewType("RSA_factored", IntList4)
RSA_unfactored = NewType("RSA_unfactored", IntList2)

RSA_number = NewType("RSA_number", Union[RSA_factored_2, RSA_factored, RSA_unfactored])


def SECTION0():
    """
    int helper functions
    """
    return


def bits(n: int) -> int:
    """
    returns bit-length of n

    Example:
        Of biggest RSA number.
    ```
        >>> bits(rsa[-1][1])
        2048
        >>>
    ```
    """
    return int(log2(n) + 1)


def digits(n: int) -> int:
    """
    returns number of decimal digits of n

    Example:
        Of biggest RSA number.
    ```
        >>> digits(rsa[-1][1])
        617
        >>>
    ```
    """
    return int(log10(n) + 1)


def SECTION1():
    """
    Robert Chapman 2010 code from https://math.stackexchange.com/a/5883/1084297
    with small changes:
    - asserts instead bad case returns
    - renamed root4() to root4m1() indicating which 4th root gets determined
    - made sq2() return tuple with positive numbers; before sq2(13) returned (-3,-2)
    - sq2(p) result can be obtained from sympy.solvers.diophantine.diophantine by diop_DN(-1, p)[0]
    """
    return


def mods(a: int, n: int) -> int:
    """returns "signed" a (mod n), in range -n//2..n//2"""
    assert n > 0
    a = a % n
    if 2 * a > n:
        a -= n
    return a


def powmods(a: int, r: int, n: int) -> int:
    """returns "signed" a**r (mod n), in range -n//2..n//2"""
    out = 1
    while r > 0:
        if (r % 2) == 1:
            r -= 1
            out = mods(out * a, n)
        r //= 2
        a = mods(a * a, n)
    return out


def quos(a: int, n: int) -> int:
    """returns equivalent of "a//n" for signed mod"""
    assert n > 0
    return (a - mods(a, n)) // n


def grem(w: Tuple[int, int], z: Tuple[int, int]) -> Tuple[int, int]:
    """returns remainder in Gaussian integers when dividing w by z"""
    (w0, w1) = w
    (z0, z1) = z
    n = z0 * z0 + z1 * z1
    assert n > 0  # and "division by zero"
    u0 = quos(w0 * z0 + w1 * z1, n)
    u1 = quos(w1 * z0 - w0 * z1, n)
    return (w0 - z0 * u0 + z1 * u1, w1 - z0 * u1 - z1 * u0)


def ggcd(w: Tuple[int, int], z: Tuple[int, int]) -> Tuple[int, int]:
    """
    returns greatest common divisor for gaussian integers

    Example:
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
    """
    while z != (0, 0):
        w, z = z, grem(w, z)
    return w


def root4m1(p: int) -> int:
    """returns sqrt(-1) (mod p)"""
    assert p > 1 and (p % 4) == 1
    k = p // 4
    j = 2
    while True:
        a = powmods(j, k, p)
        b = mods(a * a, p)
        if b == -1:
            return a
        assert b == 1  # and "p not prime"
        j += 1


def sq2(p: int) -> Tuple[int, int]:
    """
    Args:
        p: asserts if p is no prime =1 (mod 4).
    Returns:
        _: pair of numbers, their squares summing up to p.
    Example:
        Determine unique sum of two squares for prime 233.
    ```
        >>> sq2(233)
        (13, 8)
        >>>
    ```
    """
    assert p > 1 and p % 4 == 1

    a = root4m1(p)
    x, y = ggcd((p, 0), (a, 1))
    return abs(x), abs(y)


def SECTION2():
    """
    Functions dealing with representations of int as sum of two squares
    """
    return


def sq2d(p: int) -> Tuple[int, int]:
    """
    Args:
        p: asserts if not odd prime.
    Returns:
        _: pair of numbers, with difference of their squares being p.
    Example:
        Determine unique difference of two squares for prime 11 (= 6\\*\\*2 - 5\\*\\*2).
    ```
        >>> sq2d(11)
        (6, 5)
        >>>
    ```
    """
    assert p > 1 and isprime(p)

    return 1 + p // 2, p // 2


def square_sum_prod(n: Union[int, RSA_number]) -> Union[IntList2, IntList4]:
    """
    Args:
        n: int or RSA_number.
    Returns:
        _: int list with squares of pairs of ints sum up to prime, prime[s] multiply to n.
    Example:
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
    """
    if isinstance(n, list):
        L = square_sum_prod(n[2])
        return L + square_sum_prod(n[3])

    return list(sq2(n))


def square_sums_(s: List[int]) -> Type[IntList2]:
    """
    Args:
        s: List of int returned by square_sum_prod(n).
    Returns:
        _: List of int pairs, their squares summing up to n.
    Example:
        For composite number RSA-59.
    ```
        >>> r = rsa[0]
        >>> s = square_sum_prod(r)
        >>> square_sums_(s)
        [[93861205413769670113229603198, 250662312444502854557140314865], \
[264836754409721537369435955610, 38768728061109707828243001823]]
        >>> for a,b in square_sums_(s):
        ...     a**2 + b**2 == r[1]
        ...
        True
        True
        >>>
    ```
    """
    if len(s) == 2:
        return [s]

    b = s.pop()
    a = s.pop()
    r = []
    for p in square_sums_(s):
        # Brahmagupta–Fibonacci identity
        r.append([abs(a * p[0] - b * p[1]), a * p[1] + b * p[0]])
        r.append([a * p[0] + b * p[1], abs(b * p[0] - a * p[1])])
    s.append(a)
    s.append(b)
    return r


def square_sums(
    L: List[int], revt: bool = False, revl: bool = False, uniq: bool = False
) -> Type[IntList2]:
    """
    Args:
        L: List of int.
        revt: sorting direction for tuples.
        revl: sorting direction for list.
        uniq: eliminate duplicates if True.
    Returns:
        _: square_sums_(l) sorted (tuples and list), optionally with duplicates removed.
    Example:
        For list corresponding to number
          5\\*5\\*13 (5 = 2\\*\\*2 + 1\\*\\*2, 13 = 3\\*\\*2 + 2\\*\\*2).
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
    """
    r = square_sums_(L)
    for t in r:
        t.sort(reverse=revt)
    r.sort(key=(lambda t: t[0]), reverse=revl)
    if uniq:
        return [L for i, L in enumerate(r) if i == 0 or r[i - 1][0] != L[0]]
    return r


smp1m4 = [
    5,
    13,
    17,
    29,
    37,
    41,
    53,
    61,
    73,
    89,
    97,
    101,
    109,
    113,
    137,
    149,
    157,
    173,
    181,
    193,
    197,
    229,
    233,
    241,
    257,
    269,
    277,
    281,
    293,
    313,
    317,
    337,
    349,
    353,
    373,
    389,
    397,
    401,
    409,
    421,
    433,
    449,
    457,
    461,
    509,
    521,
    541,
    557,
    569,
    577,
    593,
    601,
    613,
    617,
    641,
    653,
    661,
    673,
    677,
    701,
    709,
    733,
    757,
    761,
    769,
    773,
    797,
    809,
    821,
    829,
    853,
    857,
    877,
    881,
    929,
    937,
    941,
    953,
    977,
    997,
]


def sqtst(L: List[int], k: int, dbg: int = 0) -> None:
    """
    Note:
        sqtst() verifies that 2**(k-1) == unique #sum_of_squares by many
        asserts for all k-element subsets of l
    Args:
        L: list of distinct primes =1 (mod 4)
        k: size of subsets
        dbg: 0=without debug output, 1-3 with more and more
    Example:
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
    """
    assert len(L) >= k
    for s in combinations(range(len(L)), k):
        LS = list(chain(*[sq2(L[x]) for x in s]))
        S = square_sums(LS, uniq=True)
        if dbg >= 1:
            if dbg >= 3:
                print(s)
            if dbg >= 2:
                print(LS)
            print(S)
        assert 2 ** (k - 1) == len(S)


if cypari2 is None:

    def to_squares_sum(sqrtm1: int, p: int) -> Type[IntList2]:
        """
        Args:
            sqrtm1: sqrt(-1) (mod p).
            p: prime p =1 (mod 4).
        Returns:
            _: sum of squares for p.
        Example:
        ```
            >>> to_squares_sum(11, 61)
            (6, -5)
            >>>
        ```
        """
        return gcd(p, sqrtm1 + I).as_real_imag()

else:

    def to_squares_sum(sqrtm1: int, p: int) -> Type[IntList2]:
        """much faster in case cypari2 is available
        Args:
            sqrtm1: sqrt(-1) (mod p).
            p: prime p =1 (mod 4).
        Returns:
            _: sum of squares for p.
        Example:
        ```
            >>> to_squares_sum(11, 61)
            (6, -5)
            >>>
        ```
        """
        [M, V] = pari.halfgcd(sqrtm1, p)
        return gen_to_python(V[1]), gen_to_python(M[1, 0])


def to_sqrtm1(xy: Type[IntList2], n: int) -> int:
    """
    Args:
        xy: xy[0]**2 + xy[1]**2 == n.
        n: number =1 (mod 4).
    Returns:
        _: sqrt(-1) (mod n).
    Example:
    ```
        >>> to_sqrtm1((14,5),221)
        47
        >>> 47**2%221==221-1
        True
        >>>
    ```
    """
    return xy[0] * pow(xy[1], -1, n) % n


def SECTION3():
    """
    Functions working on "rsa" list
    """
    return


def idx(rsa_: List[RSA_number], L: int) -> int:
    """
    Args:
        rsa_: list of RSA numbers
        L: bit-length or decimal-digit-length of RSA number
    Returns:
        _: index of RSA-l in rsa list, -1 if not found
    """
    for i, r in enumerate(rsa_):
        if r[0] == L:
            return i
    return -1


def has_factors(
    r: Type[RSA_number], mod4: Union[None, int, Tuple[int, int]] = None
) -> bool:
    """
    Args:
        r: an RSA number
        mod4: optional restriction (remainder mod 4 for number or its both prime factors)
    Returns:
        _: RSA number has factors and adheres mod 4 restriction(s)
    """
    return len(r) >= 4 and (
        mod4 is None
        or (isinstance(mod4, int) and r[1] % 4 == mod4)
        or (isinstance(mod4, tuple) and r[2] % 4 == mod4[0] and r[3] % 4 == mod4[1])
    )


def has_factors_2(
    r: Type[RSA_number], mod4: Union[None, int, Tuple[int, int]] = None
) -> bool:
    """
    Args:
        r: an RSA number
        mod4: optional restriction (remainder mod 4 for number or its both prime factors)
    Returns:
        _: RSA number has factors p and q, and factorization dictionaries of p-1 and q-1
    Example:
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
    """
    return len(r) >= 6 and (
        mod4 is None
        or (isinstance(mod4, int) and r[1] % 4 == mod4)
        or (isinstance(mod4, tuple) and r[2] % 4 == mod4[0] and r[3] % 4 == mod4[1])
    )


def without_factors(r: Type[RSA_number], mod4: Union[None, int] = None) -> bool:
    """
    Args:
        r: an RSA number
        mod4: optional restriction (remainder mod 4 for number)
    Returns:
        _: RSA number has no factors and adheres mod 4 restriction(s)
    """
    return len(r) == 2 and (
        mod4 is None or (isinstance(mod4, int) and r[1] % 4 == mod4)
    )


def SECTION4():
    """
    primeprod_f functions, passing p and q instead n=p*q much faster than sympy.f
    """


def primeprod_totient(p: int, q: int) -> int:
    """
    Args:
        p,q: odd primes.
    Returns:
        _: totient(n) with n=p*q.
    """
    return (p - 1) * (q - 1)


def primeprod_reduced_totient(p: int, q: int) -> int:
    """
    Args:
        p,q: odd primes.
    Returns:
        _: reduced_totient(n) with n=p*q.
    """
    return int(lcm(p - 1, q - 1))


def SECTION5():
    """
    Functions on factorization dictionaries.

    [as returned by sympy.factorint() (in rsa[x][4] for p-1 and rsa[x][5] for q-1) ]
    """
    return


def dict_int(d: Dict[int, int]) -> int:
    """
    Args:
        d: factorization dictionary.
    Returns:
        _: n with d = sympy.factorint(n).
    """
    p = 1
    for k in d.keys():
        p *= k ** d[k]

    return p


def dict_totient(d: Dict[int, int]) -> int:
    """
    Args:
        d: factorization dictionary.
    Returns:
        _: totient(n) with d = sympy.factorint(n).
    """
    p = 1
    for k in d.keys():
        p *= (k - 1) * (k ** (d[k] - 1))

    return p


# functions on pair of factorization dictionaries
#
def dictprod_totient(d1: Dict[int, int], d2: Dict[int, int]) -> int:
    """
    Args:
        d1,d2: factorization dictionaries.
    Returns:
        _: totient(n) with n=dict_int(d1)*dict_int(d2).
    """
    return dict_totient(d1) * dict_totient(d2)


def dictprod_reduced_totient(d1: Dict[int, int], d2: Dict[int, int]) -> int:
    """
    Args:
        d1,d2: factorization dictionaries.
    Returns:
        _: reduced_totient(n) with n=dict_int(d1)*dict_int(d2).
    """
    return int(lcm(dict_totient(d1), dict_totient(d2)))


def SECTION6():
    """
    Validation functions, rsa list
    """
    return


def validate_squares() -> None:
    """avoid R0915 pylint too-many-statements warning for validate()"""
    s = [2, 1, 3, 2, 4, 1]  # 1105 = 5 * 13 * 17 = (2² + 1²) * (3² + 2²) * (4² + 1²)

    p = 1
    for j in range(0, len(s), 2):
        p *= s[j] ** 2 + s[j + 1] ** 2

    L = square_sums_(s)
    for t in L:
        assert t[0] ** 2 + t[1] ** 2 == p

    L = square_sums(s)  # [[4, 33], [9, 32], [12, 31], [23, 24]]
    for t in L:
        assert t[0] ** 2 + t[1] ** 2 == p
        assert t[0] < t[1]
    for j in range(len(L) - 1):
        assert L[j][0] < L[j + 1][0]

    L = square_sums(s, revl=True, revt=True)
    for t in L:
        assert t[0] ** 2 + t[1] ** 2 == p
        assert t[0] > t[1]
    for j in range(len(L) - 1):
        assert L[j][0] > L[j + 1][0]

    sqtst(smp1m4[10:20], 8)

    s = square_sum_prod(rsa[0])
    assert (s[0] ** 2 + s[1] ** 2) * (s[2] ** 2 + s[3] ** 2) == rsa[0][1]

    assert sq2d(257)[0] ** 2 - sq2d(257)[1] ** 2 == 257

    assert sq2(100049)[0] ** 2 + sq2(100049)[1] ** 2 == 100049


def validate(rsa_, doprint: bool = False) -> None:
    """
    Assert many identities to assure data consistency and generate demo output for non RSA-class
    functionality. Gets executed by [RSA().validate()](#function-validate-1).
    Args:
        rsa_: list of rsa entries.
    """
    if doprint:
        print(
            "\nwith p-1 and q-1 factorizations (n=p*q):",
            len(["" for r in rsa_ if len(r) == 6]),
        )
    br = 6
    assert len(["" for r in rsa_ if len(r) == 6]) == 25
    for i, r in enumerate(rsa_):
        if has_factors_2(r):
            (L, n, p, q, pm1, qm1) = r
        elif has_factors(r):
            (L, n, p, q) = r
        else:
            (L, n) = r

        assert L == digits(n) or L == bits(n)

        if i > 0:
            assert n > rsa_[i - 1][1]

        if has_factors(r):
            assert n == p * q
            assert isprime(p)
            assert isprime(q)
            assert pow(997, primeprod_totient(p, q), n) == 1
            assert pow(997, primeprod_reduced_totient(p, q), n) == 1

        if has_factors_2(r):
            for k in pm1.keys():
                assert isprime(k)

            for k in qm1.keys():
                assert isprime(k)

            assert dict_int(pm1) == p - 1
            assert dict_int(qm1) == q - 1

            assert pow(997, dict_totient(pm1), p - 1) == 1
            assert pow(997, dict_totient(qm1), q - 1) == 1

            assert (
                pow(
                    65537,
                    dictprod_reduced_totient(pm1, qm1),
                    primeprod_reduced_totient(p, q),
                )
                == 1
            )

            # this does only work for RSA number != RSA-190
            if L != 190:
                assert (
                    pow(65537, dictprod_totient(pm1, qm1), primeprod_totient(p, q)) == 1
                )

        if not has_factors_2(r) and has_factors_2(rsa_[i - 1]):
            if doprint:
                print(
                    "\n\nwithout (p-1) and (q-1) factorizations, but p and q:",
                    len(["" for r in rsa_ if len(r) == 4]),
                )
            br = 3
            assert len(["" for r in rsa_ if len(r) == 4]) == 0

        if not has_factors(r) and has_factors(rsa_[i - 1]):
            if doprint:
                print(
                    "\nhave not been factored sofar:",
                    len(["" for r in rsa_ if len(r) == 2]),
                )
            br = 3
            assert len(["" for r in rsa_ if len(r) == 2]) == 31

        if doprint:
            print(
                f"{L:3d}",
                ("bits  " if L == bits(n) else "digits")
                + (
                    ","
                    if i < len(rsa_) - 1
                    else "(=" + str(digits(rsa_[-1][1])) + " digits)\n"
                ),
                end="\n" if i % 7 == br or i == len(rsa_) - 1 else "",
            )

    validate_squares()


# rsa list entries of form (n=p*q):
#   x, RSA-x = n [, p, q [, (p-1), (q-1) as factorization dictionaries]]
#
rsa = [
    [
        59,
        71641520761751435455133616475667090434063332228247871795429,
        200429218120815554269743635437,
        357440504101388365610785389017,
        {2: 2, 3: 2, 946790500267: 1, 5880369817360553: 1},
        {2: 3, 41: 1, 149: 1, 1356913: 1, 2739881: 1, 1967251783951: 1},
    ],
    [
        79,
        7293469445285646172092483905177589838606665884410340391954917800303813280275279,
        848184382919488993608481009313734808977,
        8598919753958678882400042972133646037727,
        {2: 4, 3: 1, 181: 1, 725252770335461: 1, 134611158882680922107: 1},
        {
            2: 1,
            3: 1,
            13: 1,
            283: 1,
            158923: 1,
            139139007277: 1,
            17616807254846020469: 1,
        },
    ],
    [
        100,
        1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139,
        37975227936943673922808872755445627854565536638199,
        40094690950920881030683735292761468389214899724061,
        {
            2: 1,
            3167: 1,
            3613: 1,
            587546788471: 1,
            3263521422991: 1,
            865417043661324529: 1,
        },
        {
            2: 2,
            5: 1,
            41: 1,
            2119363: 1,
            602799725049211: 1,
            38273186726790856290328531: 1,
        },
    ],
    [
        110,
        35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667,
        6122421090493547576937037317561418841225758554253106999,
        5846418214406154678836553182979162384198610505601062333,
        {
            2: 1,
            11: 1,
            41: 1,
            127: 1,
            53445720712446074139157404521548080741185454495287: 1,
        },
        {
            2: 2,
            13: 1,
            379: 1,
            293729: 1,
            3577378891: 1,
            282316043074791150281193589330501811: 1,
        },
    ],
    [
        120,
        227010481295437363334259960947493668895875336466084780038173258247009162675779735389791151574049166747880487470296548479,
        327414555693498015751146303749141488063642403240171463406883,
        693342667110830181197325401899700641361965863127336680673013,
        {
            2: 1,
            19: 1,
            23: 1,
            173: 1,
            191: 1,
            20207133825867205597523477: 1,
            561051027433723110582599363: 1,
        },
        {
            2: 2,
            673: 1,
            9500104961: 1,
            11317677666073: 1,
            2395450201344737432933763488281637: 1,
        },
    ],
    [
        129,
        114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541,
        3490529510847650949147849619903898133417764638493387843990820577,
        32769132993266709549961988190834461413177642967992942539798288533,
        {2: 5, 3: 2, 12119894134887676906763366735777424074367238328102041124968127: 1},
        {
            2: 2,
            41: 1,
            199811786544309204572938952383136959836449042487761844754867613: 1,
        },
    ],
    [
        130,
        1807082088687404805951656164405905566278102516769401349170127021450056662540244048387341127590812303371781887966563182013214880557,
        39685999459597454290161126162883786067576449112810064832555157243,
        45534498646735972188403686897274408864356301263205069600999044599,
        {
            2: 1,
            17: 1,
            70790437: 1,
            122695989299375939: 1,
            134385819829647641627927415253175893091: 1,
        },
        {
            2: 1,
            11: 1,
            29: 1,
            1823: 1,
            5659: 1,
            9349: 1,
            91917993786815014822957: 1,
            8050592072224516717989781921: 1,
        },
    ],
    [
        140,
        21290246318258757547497882016271517497806703963277216278233383215381949984056495911366573853021918316783107387995317230889569230873441936471,
        3398717423028438554530123627613875835633986495969597423490929302771479,
        6264200187401285096151654948264442219302037178623509019111660653946049,
        {
            2: 1,
            7: 1,
            7649: 1,
            435653: 1,
            396004811: 1,
            183967535370446691250943879126698812223588425357931: 1,
        },
        {
            2: 6,
            61: 1,
            135613: 1,
            3159671789: 1,
            3744661133861411144034292857028083085348933344798791: 1,
        },
    ],
    [
        150,
        155089812478348440509606754370011861770654545830995430655466945774312632703463465954363335027577729025391453996787414027003501631772186840890795964683,
        348009867102283695483970451047593424831012817350385456889559637548278410717,
        445647744903640741533241125787086176005442536297766153493419724532460296199,
        {
            2: 2,
            7: 1,
            24514564358712967361: 1,
            1562667948044178859823: 1,
            324446162657135923876474272694399: 1,
        },
        {
            2: 1,
            11: 1,
            11807588869: 1,
            30053283389: 1,
            57084195242235980757292641664096499756257280147893049: 1,
        },
    ],
    [
        155,
        10941738641570527421809707322040357612003732945449205990913842131476349984288934784717997257891267332497625752899781833797076537244027146743531593354333897,
        102639592829741105772054196573991675900716567808038066803341933521790711307779,
        106603488380168454820927220360012878679207958575989291522270608237193062808643,
        {
            2: 1,
            607: 1,
            305999: 1,
            276297036357806107796483997979900139708537040550885894355659143575473: 1,
        },
        {
            2: 1,
            241: 1,
            430028152261281581326171: 1,
            514312985943800777534375166399250129284222855975011: 1,
        },
    ],
    [
        160,
        2152741102718889701896015201312825429257773588845675980170497676778133145218859135673011059773491059602497907111585214302079314665202840140619946994927570407753,
        45427892858481394071686190649738831656137145778469793250959984709250004157335359,
        47388090603832016196633832303788951973268922921040957944741354648812028493909367,
        {
            2: 1,
            37: 1,
            41: 1,
            43: 1,
            61: 1,
            541: 1,
            13951723: 1,
            104046987091804241291: 1,
            7268655850686072522262146377121494569334513: 1,
        },
        {
            2: 1,
            9973: 1,
            165833: 1,
            369456908150299181: 1,
            3414553020359960488907: 1,
            11356507337369007109137638293561: 1,
        },
    ],
    [
        170,
        26062623684139844921529879266674432197085925380486406416164785191859999628542069361450283931914514618683512198164805919882053057222974116478065095809832377336510711545759,
        3586420730428501486799804587268520423291459681059978161140231860633948450858040593963,
        7267029064107019078863797763923946264136137803856996670313708936002281582249587494493,
        {
            2: 1,
            11: 2,
            14819920373671493747106630525902976955749833392809827112149718432371687813462977661: 1,
        },
        {
            2: 2,
            11: 1,
            17: 1,
            13398542879421488583699281633021272027489: 1,
            725099705609835336143088040991339807926261: 1,
        },
    ],
    [
        576,
        188198812920607963838697239461650439807163563379417382700763356422988859715234665485319060606504743045317388011303396716199692321205734031879550656996221305168759307650257059,
        398075086424064937397125500550386491199064362342526708406385189575946388957261768583317,
        472772146107435302536223071973048224632914695302097116459852171130520711256363590397527,
        {
            2: 2,
            3: 1,
            53: 1,
            7129: 1,
            10987: 1,
            55057: 1,
            6706111: 1,
            1554503367019: 1,
            295964577748188802772167: 1,
            47041965497216811220810358707: 1,
        },
        {
            2: 1,
            29: 1,
            479: 1,
            1427: 1,
            50459: 1,
            64875151642726381031695262181898031: 1,
            3642901060841810176072710975277263462871: 1,
        },
    ],
    [
        180,
        191147927718986609689229466631454649812986246276667354864188503638807260703436799058776201365135161278134258296128109200046702912984568752800330221777752773957404540495707851421041,
        400780082329750877952581339104100572526829317815807176564882178998497572771950624613470377,
        476939688738611836995535477357070857939902076027788232031989775824606225595773435668861833,
        {
            2: 3,
            74051: 1,
            571409: 1,
            1183963023213768222526863985153367780550281409253671455047486308276274179178583: 1,
        },
        {
            2: 3,
            277: 1,
            751: 1,
            47779: 1,
            88291435965578199481003: 1,
            67935712535668043985232693389634831578450559709946498371: 1,
        },
    ],
    [
        190,
        1907556405060696491061450432646028861081179759533184460647975622318915025587184175754054976155121593293492260464152630093238509246603207417124726121580858185985938946945490481721756401423481,
        31711952576901527094851712897404759298051473160294503277847619278327936427981256542415724309619,
        60152600204445616415876416855266761832435433594718110725997638280836157040460481625355619404899,
        {
            2: 1,
            13: 1,
            17: 1,
            117942829778890159: 1,
            608315903368337597399922156790185265420315923114346604246372907578490454531: 1,
        },
        {
            2: 1,
            13: 1,
            23: 2,
            29: 1,
            61: 1,
            61979: 1,
            1029139: 1,
            11076049: 1,
            122763887: 1,
            179557466519: 1,
            65675852814931: 1,
            2417209330310800553076788105930421719: 1,
        },
    ],
    [
        640,
        3107418240490043721350750035888567930037346022842727545720161948823206440518081504556346829671723286782437916272838033415471073108501919548529007337724822783525742386454014691736602477652346609,
        1634733645809253848443133883865090859841783670033092312181110852389333100104508151212118167511579,
        1900871281664822113126851573935413975471896789968515493666638539088027103802104498957191261465571,
        {
            2: 1,
            3: 1,
            18353: 1,
            6165734768339: 1,
            2407708176268419609396902878150001458465496860753486300568907485254279557902789: 1,
        },
        {
            2: 1,
            5: 1,
            4679777803781: 1,
            1147248313909137269625397453326444547: 1,
            35405444252479708968191506911058325334824672051: 1,
        },
    ],
    [
        200,
        27997833911221327870829467638722601621070446786955428537560009929326128400107609345671052955360856061822351910951365788637105954482006576775098580557613579098734950144178863178946295187237869221823983,
        3532461934402770121272604978198464368671197400197625023649303468776121253679423200058547956528088349,
        7925869954478333033347085841480059687737975857364219960734330341455767872818152135381409304740185467,
        {
            2: 2,
            23: 1,
            5659: 1,
            1863116572519082873: 1,
            3641748419425073268358467953440928333785886539123234990349574362260484991067: 1,
        },
        {
            2: 1,
            7: 2,
            53: 1,
            56431: 1,
            27041280343130385842778890540635231890964902337459944866729610065694493849918896101627429719: 1,
        },
    ],
    [
        210,
        245246644900278211976517663573088018467026787678332759743414451715061600830038587216952208399332071549103626827191679864079776723243005600592035631246561218465817904100131859299619933817012149335034875870551067,
        435958568325940791799951965387214406385470910265220196318705482144524085345275999740244625255428455944579,
        562545761726884103756277007304447481743876944007510545104946851094548396577479473472146228550799322939273,
        {
            2: 1,
            139: 1,
            435257: 1,
            519733289736523: 1,
            6932248500061305295021028550723941660959717063772746586104992075809382113041649041: 1,
        },
        {
            2: 3,
            163: 1,
            35107: 1,
            135131: 1,
            4812098496903739364963036362220429: 1,
            18897182075554701446530869863369005371346689915598405295351: 1,
        },
    ],
    [
        704,
        74037563479561712828046796097429573142593188889231289084936232638972765034028266276891996419625117843995894330502127585370118968098286733173273108930900552505116877063299072396380786710086096962537934650563796359,
        9091213529597818878440658302600437485892608310328358720428512168960411528640933367824950788367956756806141,
        8143859259110045265727809126284429335877899002167627883200914172429324360133004116702003240828777970252499,
        {
            2: 2,
            5: 1,
            17: 1,
            7759: 1,
            248701: 1,
            3311937667: 1,
            1669783862489: 1,
            1880450644642000493838449: 1,
            1332463449301370557601927007350718066344655275587: 1,
        },
        {
            2: 1,
            19: 1,
            149: 1,
            233: 1,
            426163: 1,
            34302641: 1,
            415283201: 1,
            1016849808034953458625818870540101111962118382063042645574809052805036673401061: 1,
        },
    ],
    [
        220,
        2260138526203405784941654048610197513508038915719776718321197768109445641817966676608593121306582577250631562886676970448070001811149711863002112487928199487482066070131066586646083327982803560379205391980139946496955261,
        68636564122675662743823714992884378001308422399791648446212449933215410614414642667938213644208420192054999687,
        32929074394863498120493015492129352919164551965362339524626860511692903493094652463337824866390738191765712603,
        {
            2: 1,
            13: 1,
            43: 1,
            28193842369532636782383767843087334604038997195313: 1,
            2177506520644400595610840424310201965314922932012095082429: 1,
        },
        {
            2: 1,
            169219: 1,
            52057548312320557: 1,
            543519485463084901: 1,
            10794188103674435582857519: 1,
            318574926912398362522990586376853019071825313: 1,
        },
    ],
    [
        230,
        17969491597941066732916128449573246156367561808012600070888918835531726460341490933493372247868650755230855864199929221814436684722874052065257937495694348389263171152522525654410980819170611742509702440718010364831638288518852689,
        4528450358010492026612439739120166758911246047493700040073956759261590397250033699357694507193523000343088601688589,
        3968132623150957588532394439049887341769533966621957829426966084093049516953598120833228447171744337427374763106901,
        {
            2: 2,
            7: 1,
            89: 1,
            1443721818299: 1,
            3361189948307: 1,
            4663983417158218304523477646391085358367: 1,
            80291209425238160178702519466590094229112518419: 1,
        },
        {
            2: 2,
            5: 2,
            64279: 1,
            17639078797309: 1,
            50683730684497957: 1,
            690514165195709800287433291837488016671814279191657241584683922421815714039547: 1,
        },
    ],
    [
        232,
        1009881397871923546909564894309468582818233821955573955141120516205831021338528545374366109757154363664913380084917065169921701524733294389270280234380960909804976440540711201965410747553824948672771374075011577182305398340606162079,
        29669093332083606603617799242426306347429462625218523944018571574194370194723262390744910112571804274494074452751891,
        34038161751975634380066094984915214205471217607347231727351634132760507061748526506443144325148088881115083863017669,
        {
            2: 1,
            5: 1,
            165479: 1,
            9558969107: 1,
            19746412471: 1,
            121852699704246278672182283286643773248913917: 1,
            779519473309251176957543614683532598812571459: 1,
        },
        {
            2: 2,
            41: 1,
            443: 1,
            192884403020146233859: 1,
            38252589736891930996676352841652107162937: 1,
            63498076483167021259794181873325947749878784693473: 1,
        },
    ],
    [
        768,
        1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413,
        33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489,
        36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917,
        {
            2: 8,
            11: 2,
            13: 1,
            7193: 1,
            160378082551: 1,
            7721565388263419219: 1,
            111103163449484882484711393053: 1,
            84004952723285306031729150607619115287285483651: 1,
        },
        {
            2: 2,
            359: 1,
            25589166898885508654766458077735343058690221562913013678743755072295083333225124814326892161139840020955987977931: 1,
        },
    ],
    [
        240,
        124620366781718784065835044608106590434820374651678805754818788883289666801188210855036039570272508747509864768438458621054865537970253930571891217684318286362846948405301614416430468066875699415246993185704183030512549594371372159029236099,
        509435952285839914555051023580843714132648382024111473186660296521821206469746700620316443478873837606252372049619334517,
        244624208838318150567813139024002896653802092578931401452041221336558477095178155258218897735030590669041302045908071447,
        {
            2: 2,
            13: 1,
            23: 1,
            1321: 1,
            132763: 1,
            278061697469: 1,
            1315547325027673: 1,
            56002191126873727127840221168033: 1,
            118556636965066556618358708032119781642592804124537: 1,
        },
        {
            2: 1,
            11: 1,
            1777: 1,
            5578663: 1,
            72948121: 1,
            15848143457: 1,
            13873690665893: 1,
            24733198296085446306734731206154829: 1,
            2827446579993070379467886273012523477719327: 1,
        },
    ],
    [
        250,
        2140324650240744961264423072839333563008614715144755017797754920881418023447140136643345519095804679610992851872470914587687396261921557363047454770520805119056493106687691590019759405693457452230589325976697471681738069364894699871578494975937497937,
        64135289477071580278790190170577389084825014742943447208116859632024532344630238623598752668347708737661925585694639798853367,
        33372027594978156556226010605355114227940760344767554666784520987023841729210037080257448673296881877565718986258036932062711,
        {
            2: 1,
            6213239: 1,
            101910617047160921359: 1,
            4597395223158209096147: 1,
            11015842872223957032465527015746975907581857223611379316467045416408679146689: 1,
        },
        {
            2: 1,
            5: 1,
            13: 1,
            440117350342384303: 1,
            8015381692860102796237: 1,
            72769022935390028131583224155323574786067394416649454368282707661426220155269516297: 1,
        },
    ],
    [
        260,
        22112825529529666435281085255026230927612089502470015394413748319128822941402001986512729726569746599085900330031400051170742204560859276357953757185954298838958709229238491006703034124620545784566413664540684214361293017694020846391065875914794251435144458199,
    ],
    [
        270,
        233108530344407544527637656910680524145619812480305449042948611968495918245135782867888369318577116418213919268572658314913060672626911354027609793166341626693946596196427744273886601876896313468704059066746903123910748277606548649151920812699309766587514735456594993207,
    ],
    [
        896,
        412023436986659543855531365332575948179811699844327982845455626433876445565248426198098870423161841879261420247188869492560931776375033421130982397485150944909106910269861031862704114880866970564902903653658867433731720813104105190864254793282601391257624033946373269391,
    ],
    [
        280,
        1790707753365795418841729699379193276395981524363782327873718589639655966058578374254964039644910359346857311359948708984278578450069871685344678652553655035251602806563637363071753327728754995053415389279785107516999221971781597724733184279534477239566789173532366357270583106789,
    ],
    [
        290,
        30502351862940031577691995198949664002982179597487683486715266186733160876943419156362946151249328917515864630224371171221716993844781534383325603218163254920110064990807393285889718524383600251199650576597076902947432221039432760575157628357292075495937664206199565578681309135044121854119,
    ],
    [
        300,
        276931556780344213902868906164723309223760836398395325400503672280937582471494739461900602187562551243171865731050750745462388288171212746300721613469564396741836389979086904304472476001839015983033451909174663464663867829125664459895575157178816900228792711267471958357574416714366499722090015674047,
    ],
    [
        309,
        133294399882575758380143779458803658621711224322668460285458826191727627667054255404674269333491950155273493343140718228407463573528003686665212740575911870128339157499072351179666739658503429931021985160714113146720277365006623692721807916355914275519065334791400296725853788916042959771420436564784273910949,
    ],
    [
        1024,
        135066410865995223349603216278805969938881475605667027524485143851526510604859533833940287150571909441798207282164471551373680419703964191743046496589274256239341020864383202110372958725762358509643110564073501508187510676594629205563685529475213500852879416377328533906109750544334999811150056977236890927563,
    ],
    [
        310,
        1848210397825850670380148517702559371400899745254512521925707445580334710601412527675708297932857843901388104766898429433126419139462696524583464983724651631481888473364151368736236317783587518465017087145416734026424615690611620116380982484120857688483676576094865930188367141388795454378671343386258291687641,
    ],
    [
        320,
        21368106964100717960120874145003772958637679383727933523150686203631965523578837094085435000951700943373838321997220564166302488321590128061531285010636857163897899811712284013921068534616772684717323224436400485097837112174432182703436548357540610175031371364893034379963672249152120447044722997996160892591129924218437,
    ],
    [
        330,
        121870863310605869313817398014332524915771068622605522040866660001748138323813524568024259035558807228052611110790898823037176326388561409009333778630890634828167900405006112727432172179976427017137792606951424995281839383708354636468483926114931976844939654102090966520978986231260960498370992377930421701862444655244698696759267,
    ],
    [
        340,
        2690987062294695111996484658008361875931308730357496490239672429933215694995275858877122326330883664971511275673199794677960841323240693443353204889858591766765807522315638843948076220761775866259739752361275228111366001104150630004691128152106812042872285697735145105026966830649540003659922618399694276990464815739966698956947129133275233,
    ],
    [
        350,
        26507199951735394734498120973736811015297864642115831624674545482293445855043495841191504413349124560193160478146528433707807716865391982823061751419151606849655575049676468644737917071142487312863146816801954812702917123189212728868259282632393834443989482096498000219878377420094983472636679089765013603382322972552204068806061829535529820731640151,
    ],
    [
        360,
        218682020234317263146640637228579265464915856482838406521712186637422774544877649638896808173342116436377521579949695169845394824866781413047516721975240052350576247238785129338002757406892629970748212734663781952170745916609168935837235996278783280225742175701130252626518426356562342682345652253987471761591019113926725623095606566457918240614767013806590649,
    ],
    [
        370,
        1888287707234383972842703127997127272470910519387718062380985523004987076701721281993726195254903980001896112258671262466144228850274568145436317048469073794495250347974943216943521462713202965796237266310948224934556725414915442700993152879235272779266578292207161032746297546080025793864030543617862620878802244305286292772467355603044265985905970622730682658082529621,
    ],
    [
        380,
        30135004431202116003565860241012769924921679977958392035283632366105785657918270750937407901898070219843622821090980641477056850056514799336625349678549218794180711634478735831265177285887805862071748980072533360656419736316535822377792634235019526468475796787118257207337327341698664061454252865816657556977260763553328252421574633011335112031733393397168350585519524478541747311,
    ],
    [
        390,
        268040194118238845450103707934665606536694174908285267872982242439770917825046230024728489676042825623316763136454136724676849961188128997344512282129891630084759485063423604911639099585186833094019957687550377834977803400653628695534490436743728187025341405841406315236881249848600505622302828534189804007954474358650330462487514752974123986970880843210371763922883127855444022091083492089,
    ],
    [
        400,
        2014096878945207511726700485783442547915321782072704356103039129009966793396141985086509455102260403208695558793091390340438867513766123418942845301603261911930567685648626153212566300102683464717478365971313989431406854640516317519403149294308737302321684840956395183222117468443578509847947119995373645360710979599471328761075043464682551112058642299370598078702810603300890715874500584758146849481,
    ],
    [
        410,
        19653601479938761414239452741787457079262692944398807468279711209925174217701079138139324539033381077755540830342989643633394137538983355218902490897764441296847433275460853182355059915490590169155909870689251647778520385568812706350693720915645943335281565012939241331867051414851378568457417661501594376063244163040088180887087028771717321932252992567756075264441680858665410918431223215368025334985424358839,
    ],
    [
        420,
        209136630247651073165255642316333073700965362660524505479852295994129273025818983735700761887526097496489535254849254663948005091692193449062731454136342427186266197097846022969248579454916155633686388106962365337549155747268356466658384680996435419155013602317010591744105651749369012554532024258150373034059528878269258139126839427564311148202923131937053527161657901326732705143817744164107601735413785886836578207979,
    ],
    [
        430,
        3534635645620271361541209209607897224734887106182307093292005188843884213420695035531516325888970426873310130582000012467805106432116010499008974138677724241907444538851271730464985654882214412422106879451855659755824580313513382070785777831859308900851761495284515874808406228585310317964648830289141496328996622685469256041007506727884038380871660866837794704723632316890465023570092246473915442026549955865931709542468648109541,
    ],
    [
        440,
        26014282119556025900707884873713205505398108045952352894235085896633912708374310252674800592426746319007978890065337573160541942868114065643853327229484502994233222617112392660635752325773689366745234119224790516838789368452481803077294973049597108473379738051456732631199164835297036074054327529666307812234597766390750441445314408171802070904072739275930410299359006059619305590701939627725296116299946059898442103959412221518213407370491,
    ],
    [
        450,
        198463423714283662349723072186113142778946286925886208987853800987159869256900787915916842423672625297046526736867114939854460034942655873583931553781158032447061155145160770580926824366573211993981662614635734812647448360573856313224749171552699727811551490561895325344395743588150359341484236709604618276434347948498243152515106628556992696242074513657383842554978233909962839183287667419172988072221996532403300258906083211160744508191024837057033,
    ],
    [
        460,
        1786856020404004433262103789212844585886400086993882955081051578507634807524146407881981216968139444577147633460848868774625431829282860339614956262303635645546753552581286559710032014178315212224644686666427660441466419337888368932452217321354860484353296131403821175862890998598653858373835628654351880480636223164308238684873105235011577671552114945370886842810830301698313339004163655154668570049008475016448080768256389182668489641536264864604484300734909,
    ],
    [
        1536,
        1847699703211741474306835620200164403018549338663410171471785774910651696711161249859337684305435744585616061544571794052229717732524660960646946071249623720442022269756756687378427562389508764678440933285157496578843415088475528298186726451339863364931908084671990431874381283363502795470282653297802934916155811881049844908319545009848393775227257052578591944993870073695755688436933812779613089230392569695253261620823676490316036551371447913932347169566988069,
    ],
    [
        470,
        17051473784681185209081599238887028025183255852149159683588918369809675398036897711442383602526314519192366612270595815510311970886116763177669964411814095748660238871306469830461919135901638237924444074122866545522954536883748558744552128950445218096208188788876324395049362376806579941053305386217595984047709603954312447692725276887594590658792939924609261264788572032212334726855302571883565912645432522077138010357669555555071044090857089539320564963576770285413369,
    ],
    [
        480,
        302657075295090869739730250315591803589112283576939858395529632634305976144571441696598170401251852159138533455982172343712313383247732107268535247763784105186549246199888070331088462855743520880671299302895546822695492968577380706795842802200829411198422297326020823369315258921162990168697393348736236081296604185145690639952829781767901497605213955485328141965346769742597479306858645849268328985687423881853632604706175564461719396117318298679820785491875674946700413680932103,
    ],
    [
        490,
        1860239127076846517198369354026076875269515930592839150201028353837031025971373852216474332794920643399906822553185507255460678213880084116286603739332465781718042017172224499540303152935478714013629615010650024865526886634157459758925793594165651020789220067311416926076949777767604906107061937873540601594274731617619377537419071307115490065850326946551649682856865437718319058695376406980449326388934924579147508558589808491904883853150769224537555274811376719096144119390052199027715691,
    ],
    [
        500,
        18971941337486266563305347433172025272371835919534283031845811230624504588707687605943212347625766427494554764419515427586743205659317254669946604982419730160103812521528540068803151640161162396312837062979326593940508107758169447860417214110246410380402787011098086642148000255604546876251377453934182215494821277335671735153472656328448001134940926442438440198910908603252678814785060113207728717281994244511323201949222955423789860663107489107472242561739680319169243814676235712934292299974411361,
    ],
    [
        617,
        22701801293785014193580405120204586741061235962766583907094021879215171483119139894870133091111044901683400949483846818299518041763507948922590774925466088171879259465921026597046700449819899096862039460017743094473811056991294128542891880855362707407670722593737772666973440977361243336397308051763091506836310795312607239520365290032105848839507981452307299417185715796297454995023505316040919859193718023307414880446217922800831766040938656344571034778553457121080530736394535923932651866030515041060966437313323672831539323500067937107541955437362433248361242525945868802353916766181532375855504886901432221349733,
    ],
    [
        2048,
        25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357,
    ],
]


class RSA:
    """RSA convenience class."""

    def __init__(self):
        """avoid W0201 pylint warning"""
        self.i = 0

    def __iter__(self):
        """for iteration over RSA"""
        self.i = 0
        return self

    def __next__(self):
        """for iteration over RSA"""
        if self.i < len(rsa):
            r = rsa[self.i]
            self.i += 1
            return r

        raise StopIteration

    def index(self, x: int) -> int:
        """
        Args:
            x: bit-length or decimal-digit-length of RSA number.
        Returns:
            _: index of RSA-x in rsa list, -1 if not found.
        """
        return idx(rsa, x)

    def get(self, x: int) -> Type[RSA_number]:
        """
        Args:
            x: RSA number length.
        Returns:
            _: RSA-x from rsa list, asserts if not found.
        """
        i = self.index(x)
        assert i != -1
        return rsa[i]

    def get_(self, x: Union[int, RSA_number]) -> Type[RSA_number]:
        """
        Args:
            x: RSA number length or RSA_number.
        Returns:
            _: identity or RSA-x from rsa list.
        """
        if isinstance(x, list):
            return x

        return self.get(x)

    def factored(
        self, mod4: Union[None, int, Tuple[int, int]] = None
    ) -> Type[IntList4]:
        """
        Args:
            mod4: optional restriction (remainder mod 4 for number or its both prime factors).
        Returns:
            _: list of RSA_number being factored and satisfying mod4 restriction
        Example:
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
        """
        return [r[0:4] for r in rsa if has_factors(r, mod4)]

    def factored_2(
        self, mod4: Union[None, int, Tuple[int, int]] = None
    ) -> List[RSA_number]:
        """
        Args:
            mod4: optional restriction (remainder mod 4 for number or its both prime factors).
        Returns:
            _: list of RSA_number with factorization dictionaries.
        """
        return [r for r in rsa if has_factors_2(r, mod4)]

    def unfactored(self, mod4: Union[None, int] = None) -> Type[IntList2]:
        """
        Args:
            mod4: optional restriction (remainder mod 4 for number).
        Returns:
            _: list of RSA_number being unfactored and satisfying mod4 restriction
        Example:
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
        """
        return [r for r in rsa if without_factors(r, mod4)]

    def totient(self, x: Union[int, RSA_number]) -> int:
        """
        Args:
            x: RSA number length or RSA_number.
        Returns:
            _: totient(x).
        """
        r = self.get_(x)
        assert has_factors(r)
        p, q = r[2:4]
        return primeprod_totient(p, q)

    def reduced_totient(self, x: Union[int, RSA_number]) -> int:
        """
        Args:
            x: RSA number length or RSA_number.
        Returns:
            _: reduced_totient(x).
        """
        r = self.get_(x)
        assert has_factors(r)
        p, q = r[2:4]
        return primeprod_reduced_totient(p, q)

    def totient_2(self, x: Union[int, RSA_number]) -> int:
        """
        Args:
            x: RSA number length or RSA_number.
        Returns:
            _: apply totient function to totient(x).
        """
        r = self.get_(x)
        assert has_factors_2(r)
        pm1, qm1 = r[4:6]
        return dictprod_totient(pm1, qm1)

    def reduced_totient_2(self, x: Union[int, RSA_number]) -> int:
        """
        Args:
            x: RSA number length or RSA_number.
        Returns:
            _: apply reduced_totient function to reduced_totient(x).
        """
        r = self.get_(x)
        assert has_factors_2(r)
        pm1, qm1 = r[4:6]
        return dictprod_reduced_totient(pm1, qm1)

    def square_diffs(self, x: Union[int, RSA_number]) -> Type[IntList2]:
        """
        Args:
            x: RSA number length or RSA_number.
        Returns:
            _: two differences of squares resulting in x.
        Example:
        ```
            >>> t = RSA.get(250)
            >>> n = t[1]
            >>> [a,b],[c,d] = RSA.square_diffs(t)
            >>> (a**2 - b**2) == n and (c**2 - d**2) == n
            True
            >>>
        ```
        """
        r = self.get_(x)
        assert has_factors(r)
        n, p, q = r[1:4]
        return [
            [(p + q) // 2, abs(p - q) // 2],
            [(n + 1) // 2, (n - 1) // 2],
        ]

    def square_sums(self, x: Union[int, RSA_number]) -> Type[IntList2]:
        """
        Args:
            x: RSA number length or RSA_number.
        Returns:
            _: two different sums of squares resulting in x.
        Example:
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
        """
        r = self.get_(x)
        assert has_factors(r)
        p, q = r[2:4]
        assert p % 4 == 1 and q % 4 == 1
        return square_sums(square_sum_prod(r))

    def square_sums_4(self, x: Union[int, RSA_number]) -> Tuple[int, int, int, int]:
        """
        Args:
            x: RSA_number length or RSA_number
        Returns:
            _: square sums of tuple elements sum up to RSA number
        Example:
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
            (179348979911745603741332779404, 85487774497975933628103176206, \
105946792191696573364448656521, 144715520252806281192691658344)
            >>>
        ```
        """
        r = self.get_(x)
        assert has_factors(r)
        p, q = r[2:4]
        assert p % 4 == 1 and q % 4 == 1
        P = sq2(p)
        Q = sq2(q)
        return P[0] * Q[0], P[1] * Q[1], P[0] * Q[1], P[1] * Q[0]

    def to_sqrtm1(self, xy: Type[IntList2], p: int) -> int:
        """shortcut"""
        return to_sqrtm1(xy, p)

    def to_squares_sum(self, sqrtm1: int, p: int) -> Type[IntList2]:
        """shortcut"""
        return to_squares_sum(sqrtm1, p)

    def svg(self, n: Union[int, RSA_number], scale: int) -> str:
        """
        Generate prime factors svg.
        """
        r = self.get_(n)
        if len(r) < 4:
            return ""
        p, q = r[2:4]
        X = bits(q) - 1
        Y = bits(p) - 1
        s = (
            '<svg width="'
            + str(scale * bits(q))
            + '" height="'
            + str(scale * bits(p))
            + '" viewBox="'
            + "0 0 "
            + str(bits(q))
            + " "
            + str(bits(q))
            + '" xmlns="http://www.w3.org/2000/svg">'
        )
        for y in range(bits(p) - 1, -1, -1):
            for x in range(bits(q) - 1, -1, -1):
                col = "blue" if (p & (1 << y) != 0 and q & (1 << x) != 0) else "cyan"
                s += (
                    '<rect x="'
                    + str(X - x)
                    + '" y="'
                    + str(Y - y)
                    + '" width="1" height="1" fill="'
                    + col
                    + '" stroke-width="0"/>'
                )
        s += "</svg>"
        return s

    def sort_factors(self) -> None:
        """make p the bigger of factors by switching if needed"""
        for i in range(len(rsa)):
            if len(rsa[i]) > 2 and rsa[i][2] < rsa[i][3]:
                [p,q] = rsa[i][2:4]
                rsa[i][2:4] = [q,p]
                if len(rsa[i]) > 4:
                    [pm1,qm1] = rsa[i][4:6]
                    rsa[i][4:6] = [qm1,pm1]


    def validate(self, doprint: bool = False) -> None:
        """
        Assert many identities to assure data consistency and optionally generate demo output
              (executed if \\_\\_name\\_\\_ == "\\_\\_main\\_\\_").
        Example:
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
        """
        assert(self.factored((1,1))[-1] == self.factored_2((1,1))[-1][0:4])
        assert(self.factored(3)[-1] == self.factored_2(3)[-1][0:4])

        r = self.factored_2()[-1]
        l, _n, p, q, pm1, qm1 = r
        assert (p - 1) * (q - 1) == self.totient(r)
        assert self.totient_2(r) == self.totient_2(l)
        assert self.totient_2(r) == dictprod_totient(pm1, qm1)
        assert pow(65537, self.reduced_totient_2(190), self.reduced_totient(190)) == 1
        assert len(self.factored()) == 25
        assert len(self.factored_2()) == 25

        r = self.get(2048)
        assert r[0] == 2048 and bits(r[1]) == 2048
        assert r == self.get_(r)
        assert r == self.get_(2048)

        assert self.index(617) == len(rsa) - 2

        r = self.get(250)
        [a, b], [c, d] = self.square_diffs(r)
        assert r[0] == 250 and a**2 - b**2 == r[1] and c ** 2 - d**2 == r[1]

        r = self.get(129)
        [a, b], [c, d] = self.square_sums(r)
        assert r[0] == 129 and a**2 + b**2 == r[1] and c ** 2 + d**2 == r[1]
        a, b, c, d = self.square_sums_4(r)
        assert a**2 + b**2 + c**2 + d**2 == r[1]

        xy = sq2(997)
        sqrtm1 = self.to_sqrtm1(xy, 997)
        assert pow(sqrtm1, 2, 997) == 997 - 1
        assert self.to_squares_sum(sqrtm1, 997) == xy

        validate(rsa, doprint)


if __name__ == "__main__":
    RSA().validate("doprint")
