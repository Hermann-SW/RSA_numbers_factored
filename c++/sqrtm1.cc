// Precompute "sqrtm1 = sqrt(-1) (mod p)" for 10000-9383761 digit primes:
//
// g++ sqrtm1.cc -lgmp -lgmpxx -O3 -Wall -pedantic -Wextra -o sqrtm1
// (cpplinted and cppchecked)
//
#include <time.h>
#include <math.h>
#include <gmpxx.h>
#include <assert.h>

#include <iostream>

//  0:  10000-digit  https://t5k.org/curios/page.php?number_id=9680
//  1:  36401-digit  https://t5k.org/curios/page.php?number_id=3658
//  2: 100355-digit  https://t5k.org/primes/page.php?id=89650
//  3: 200700-digit  https://t5k.org/primes/page.php?id=103792
//  4: 272770-digit  https://t5k.org/primes/lists/all.txt
//  5: 330855-digit  https://t5k.org/primes/lists/all.txt
//  6: 388342-digit  https://t5k.org/primes/page.php?id=122213
//  7:         2165  10^999999+308267*10^292000+1     1000000 CH10  2021
//                   https://t5k.org/primes/lists/all.txt
//  8:           10  10223*2^31172165+1               9383761 SB12  2016
//  9:         4794  456551^98304-456551^49152+1      556351 L4142 2017
// >9: 2^n+9 isprime https://oeis.org/A057196
struct row { std::string f; unsigned b, e, a; } r[] = {
    { "65516468355", 2, 333333, 1 },    // 100355-digit
    { "3756801695685", 2, 666669, 1 },  // 200700-digit
    { "1705", 2, 906110, 1 },           // 272770-digit
    { "2145", 2, 1099064, 1 },          // 330855-digit
    { "2996863034895", 2, 1290000, 1 }  // 388342-digit
};

float roundf_(float f, int p) {
    float q = powf(10., p);
    return roundf(q * f) / q;
}

int main(int argc, char *argv[]) {
    const int sday = 24*60*60;
    mpz_class a, b, c, p;
    char *buf;
    if (argc < 2) {
        std::cerr << "Format: ./sqrtm1 i [div]  with 0<=i<=8 or i>8, div>=1\n";
        exit(1);
    }
    int d = 1, bits, u = atoi(argv[1]);
    float dt;
    assert(u >= 0);
    buf = new char[32000000];
    assert(buf);

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
        case 7: {
            mpz_ui_pow_ui(a.get_mpz_t(), 10, 999999);
            mpz_ui_pow_ui(b.get_mpz_t(), 10, 292000);
            b *= mpz_class("308267");
            a += b;
            a += 1;
            break;
        }
        case 8: {
            mpz_ui_pow_ui(a.get_mpz_t(), 2, 31172165);
            a *= mpz_class("10223");
            a += 1;
            break;
        }
        case 9: {
            mpz_ui_pow_ui(b.get_mpz_t(), 456551, 49152);
            a = b*b - b + 1;
            break;
        }
        default: {
            assert(u > 9 || !"wrong selection (0-9, >9)");
            mpz_ui_pow_ui(a.get_mpz_t(), 2, u);
            a += 9;
            break;
        }
    }

    p = a;
    c = a / 4;

    std::cerr
        << strlen(mpz_get_str(buf, 10, p.get_mpz_t())) << "-digit prime p ("
        << (bits = strlen(mpz_get_str(buf, 2, p.get_mpz_t()))) << " bits)\n";

    if (argc > 2)  {
        b = 2;
        c = d = 1 + (strlen(buf) - 1) / atoi(argv[2]);
        mpz_powm(c.get_mpz_t(), b.get_mpz_t(), c.get_mpz_t(), p.get_mpz_t());
    }

    // deterministic fast search for smallest quadratic non-residue
    b = 2;
    while (mpz_kronecker(b.get_mpz_t(), p.get_mpz_t()) != -1) {
        mpz_nextprime(b.get_mpz_t(), b.get_mpz_t());
    }
    std::cerr << "smallest quadratic non-residue prime: " << b << "\n";

    clock_t start = clock();
    mpz_powm(a.get_mpz_t(), b.get_mpz_t(), c.get_mpz_t(), p.get_mpz_t());
    dt = static_cast<float>(clock() - start) / CLOCKS_PER_SEC;

    if (argc > 2) {
        std::cerr << dt << "s (" << roundf_(dt/d*bits/sday, 2) << " days)\n";
    } else {
        std::cerr << dt << "s\n";

        std::cout << a << "\n";

        assert(a * a % p == p - 1);
    }

    std::cerr << "done\n";
    delete buf;

    return 0;
}
