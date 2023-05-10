#include <time.h>
#include <gmpxx.h>
#include <assert.h>

#include <iostream>
#include <utility>

// def SECTION1():
//   """
//   Robert Chapman 2010 code from https://math.stackexchange.com/a/5883/1084297
//   with small changes:
//   - asserts instead bad case returns
//   - renamed root4() to root4m1() indicating which 4th root gets determined
//   - made sq2() return tuple with positive numbers; before sq2(13) returned
//     (-3,-2)
//   - sq2(p) result can be obtained from sympy.solvers.diophantine.diophantine
//     by diop_DN(-1, p)[0]
//   """
//   return

typedef std::pair<mpz_class, mpz_class> mpz_class2;

mpz_class mods(mpz_class a, mpz_class n) {
    assert(n > 0);
    a = a % n;
    if (2 * a > n) {
        a -= n;
    }
    return a;
}

mpz_class powmods(mpz_class a, mpz_class r, mpz_class n) {
    mpz_class out = 1;
    while (r > 0) {
        if ((r % 2) == 1) {
            r -= 1;
            out = mods(out * a, n);
        }
        r /= 2;
        a = mods(a * a, n);
    }
    return out;
}

mpz_class quos(mpz_class a, mpz_class n) {
    assert(n > 0);
    return (a - mods(a, n))/n;
}

mpz_class2 grem(mpz_class2 w, mpz_class2 z) {
    // remainder in Gaussian integers when dividing w by z
    mpz_class w0 = w.first; mpz_class w1 = w.second;
    mpz_class z0 = z.first; mpz_class z1 = z.second;
    mpz_class u0, u1;
    mpz_class n = z0 * z0 + z1 * z1;
    assert(n != 0);
    u0 = quos(w0 * z0 + w1 * z1, n);
    u1 = quos(w1 * z0 - w0 * z1, n);
    return mpz_class2(w0 - z0 * u0 + z1 * u1, w1 - z0 * u1 - z1 * u0);
}

mpz_class2 ggcd(mpz_class2 w, mpz_class2 z) {
    while (z.first != 0 || z.second != 0) {
        mpz_class2 a = z; z = grem(w, z); w = a;
    }
    return w;
}

mpz_class root4m1(mpz_class p) {
    // 4th root of 1 modulo p
    mpz_class k = p/4;
    mpz_class j = 2;
    for (;;) {
        mpz_class a = powmods(j, k, p);
        mpz_class b = mods(a * a, p);
        if (b == -1) {
            return a;
        }
        assert(b == 1 && "p not prime");
        ++j;
    }
}

mpz_class2 sq2(mpz_class p) {
    assert(p > 1 && (p % 4) == 1);
    mpz_class a = root4m1(p);
    mpz_class2 xy = ggcd(mpz_class2(p, 0), mpz_class2(a, 1));
    return mpz_class2(abs(xy.first), abs(xy.second));
}
//
//##############################################################################

int main(void) {
  mpz_class a;
  mpz_class2 r;

  mpz_ui_pow_ui(a.get_mpz_t(), 2, 1<<13);
  a += 897;

  clock_t start = clock();
  r = sq2(a);
  std::cerr << static_cast<float>(clock() - start) / CLOCKS_PER_SEC << "s\n";
  std::cout << r.first << " " << r.second << "\n";

  return 0;
}
