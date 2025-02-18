#include <time.h>
#include <gmpxx.h>
#include <assert.h>

#include <iostream>
#include <utility>

const int kMaxLen = 25000000 + 10;  // 100million bit hex encoded number

char buf[kMaxLen];

void readbuf(const char *name) {
  FILE *src = fopen(name, "r");
  assert(src);
  fseek(src, 0, SEEK_END);
  size_t s = ftell(src);
  assert(s <= kMaxLen);
  rewind(src);
  assert(1 == fread(buf, s, 1, src));
  fclose(src);
}

int main(void) {
  char *t, *u, *v;
  mpz_class a, b = 2, p;
  size_t s;
  FILE *src;

  mpz_ui_pow_ui(a.get_mpz_t(), 516693, 1048576);
  p = a*a -a + 1;

  std::cout << mpz_sizeinbase(p.get_mpz_t(), 10) << " decimal digits prime p\n";


  readbuf("sqrtm1.gp");

  clock_t start = clock();
  mpz_set_str(a.get_mpz_t(), buf, 0);
  std::cerr << static_cast<float>(clock() - start) / CLOCKS_PER_SEC
            << "s for mpz_set_str() of ";

  std::cout << mpz_sizeinbase(a.get_mpz_t(), 16)
            << " hexadecimal digits sqrt(-1) (mod p)\n";

  start = clock();
  mpz_powm(b.get_mpz_t(), a.get_mpz_t(), b.get_mpz_t(), p.get_mpz_t());
  std::cerr << static_cast<float>(clock() - start) / CLOCKS_PER_SEC
            << "s for powm(_, sqrtm1, 2, p)\n";

  std::cout << (b == p-1) << " (sqrtm1*sqrtm1 % p == p-1)\n";


  readbuf("sos.gp");

  start = clock();
  t = strchr(buf, '[')+1;
  u = strchr(t, ',');
  *u++ = '\0';
  v = strchr(u, ']');
  *v = '\0';

  mpz_set_str(a.get_mpz_t(), t, 0);
  mpz_set_str(b.get_mpz_t(), u, 0);
  std::cerr << static_cast<float>(clock() - start) / CLOCKS_PER_SEC
            << "s for mpz_set_str() of x and y\n";

  std::cout << (a*a + b*b == p) << " (x*x + y*y == p)\n";


  return 0;
}
