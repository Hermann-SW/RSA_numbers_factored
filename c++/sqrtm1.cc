// Precompute "sqrtm1 = sqrt(-1) (mod p)" for 100355-388342 digit primes:
//
// g++ sqrtm1.cc -lgmp -lgmpxx -O3 -o sqrt1
//
#include <assert.h>
#include <gmpxx.h>
#include <time.h>

#include <iostream>

int main(void) {
  mpz_class a, b, c;
  mpz_class r;

#if 0
  // 2996863034895 * 2 ** 1290000 ± 1    (10986s + 11465s on i7-11850H)
  mpz_ui_pow_ui(a.get_mpz_t(), 2, 1290000);
  b = "2996863034895";
#elif 0
  //  3756801695685 * 2 ** 666669 ± 1    (2732s on i7-11850H)
  mpz_ui_pow_ui(a.get_mpz_t(), 2, 666669);
  b = "3756801695685";
#elif 0
  // 65516468355 * 2 ** 333333 ± 1       (588s on i7-11850H)
  mpz_ui_pow_ui(a.get_mpz_t(), 2, 333333);
  b = "65516468355";
#elif 0
  // 1705 * 2 ** 906110 + 1              (5086s + 5239s + 5204s on i7-11850H)
  mpz_ui_pow_ui(a.get_mpz_t(), 2, 906110);
  b = "1705";
#else
  // 2145 * 2 ** 1099064 + 1             (7549s on i7-11850H)
  mpz_ui_pow_ui(a.get_mpz_t(), 2, 1099064);
  b = "2145";
#endif

  a = b * a + 1;
  c = a / 4;

  gmp_randclass r1(gmp_randinit_default);
  do {
    b = 2 + r1.get_z_range(a - 3);
    std::cerr << mpz_sizeinbase(b.get_mpz_t(), 2) << " bits\n";
    clock_t start = clock();
    mpz_powm(r.get_mpz_t(), b.get_mpz_t(), c.get_mpz_t(), a.get_mpz_t());
    std::cerr << static_cast<float>(clock() - start) / CLOCKS_PER_SEC << "s\n";
    std::cout << r << "\n";
  } while (r * r % a != a - 1);

  std::cerr << "done\n";
  return 0;
}
