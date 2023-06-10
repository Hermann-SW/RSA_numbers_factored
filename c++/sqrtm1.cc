// Precompute "sqrtm1 = sqrt(-1) (mod p)" for 10000-388342 digit primes:
//
// g++ sqrtm1.cc -lgmp -lgmpxx -O3 -o sqrt1
//
#include <time.h>
#include <gmpxx.h>
#include <assert.h>

#include <iostream>

//  10000-digit  https://t5k.org/curios/page.php?number_id=9680
//  36401-digit  https://t5k.org/curios/page.php?number_id=3658
// 100355-digit  https://t5k.org/primes/page.php?id=89650
// 200700-digit  https://t5k.org/primes/page.php?id=103792
// 272770-digit  https://t5k.org/primes/lists/all.txt
// 330855-digit  https://t5k.org/primes/lists/all.txt
// 388342-digit  https://t5k.org/primes/page.php?id=122213
struct row { std::string f; unsigned b, e, a; } r[] = {
    { "65516468355", 2, 333333, 1 },    // 100355-digit
    { "3756801695685", 2, 666669, 1 },  // 200700-digit
    { "1705", 2, 906110, 1 },           // 272770-digit
    { "2145", 2, 1099064, 1 },          // 330855-digit
    { "2996863034895", 2, 1290000, 1 }  // 388342-digit
};

int main(int argc, char *argv[]) {
    mpz_class a, b, c, p;
    unsigned u = atoi(argv[1]);
    assert(u >= 0 && u < 7);

    switch (u) {
        case 0: {
            mpz_ui_pow_ui(a.get_mpz_t(), 10, 10000);
            a -= 1;
            a /= 3;
            mpz_ui_pow_ui(b.get_mpz_t(), 10, 6333);
            a -= b;
            break;
        }
        case 1: {
            mpz_ui_pow_ui(a.get_mpz_t(), 10, 36400);
            a -= 1;
            a /= 9;
            b = a;
            a *= 34;
            mpz_ui_pow_ui(c.get_mpz_t(), 10, 2264);
            c *= b;
            c *= mpz_class("42000040044444004000024");
            mpz_ui_pow_ui(b.get_mpz_t(), 10, 4550);
            b -= 1;
            b /= 9;
            c /= b;
            a -= c;
            a -= 1;
            break;
        }
        case 2:
        case 3:
        case 4:
        case 5:
        case 6: {
            u -= 2;
            mpz_ui_pow_ui(a.get_mpz_t(), r[u].b, r[u].e);
            a *= mpz_class(r[u].f);
            a += r[u].a;
            break;
        }
        default:  assert(0 || !"wrong selection (0-6)");
    }

    p = a;
    c = a / 4;

    // deterministic fast search for smallest quadratic non-residue
    b = 2;
    while (mpz_kronecker(b.get_mpz_t(), p.get_mpz_t()) != -1) {
        mpz_nextprime(b.get_mpz_t(), b.get_mpz_t());
    }
    std::cerr << "smallest quadratic non-residue prime: " << b << "\n";

    clock_t start = clock();
    mpz_powm(a.get_mpz_t(), b.get_mpz_t(), c.get_mpz_t(), p.get_mpz_t());
    std::cerr << static_cast<float>(clock() - start) / CLOCKS_PER_SEC << "s\n";
    std::cout << a << "\n";

    assert(a * a % p == p - 1);

    std::cerr << "done\n";
    return 0;
}
