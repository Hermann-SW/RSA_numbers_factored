// NOLINT(legal/copyright)
// g++ pi.cc -lgmp -lgmpxx -O3 -Wall -pedantic -Wextra -o pi
// (cpplinted and cppchecked)
//
#include <time.h>
#include <math.h>
#include <gmpxx.h>
#include <assert.h>

#include <iostream>
#include <cstdint>

int main(int argc, char *argv[]) {
    mpz_class mx, a = 2;
    if (argc < 2) {
        std::cerr << "Format: ./pi exp\n";
        exit(1);
    }
    uint64_t c = 0, u = atoi(argv[1]);
    mpz_ui_pow_ui(mx.get_mpz_t(), 10, u);

    do {
        mpz_nextprime(a.get_mpz_t(), a.get_mpz_t());
        ++c;
    }
    while (a <= mx);  // NOLINT
    std::cerr << "pi(" << mx << ")=" << c << "\n";

    return 0;
}
