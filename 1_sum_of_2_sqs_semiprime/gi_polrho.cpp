/*
f=gi_polrho
g++ -std=c++23 -Wall -Wextra -pedantic $f.cpp -o $f
cpplint --filter=-legal/copyright $f.cpp
cppcheck --enable=all --suppress=missingIncludeSystem $f.cpp --check-config
*/
#include <iostream>
#include <complex>
#include <cmath>
#include <string>
#include <cassert>

typedef std::complex<int> gaussian_integer;

int norml2(const gaussian_integer& c) {
    return c.real()*c.real() + c.imag()*c.imag();
}

std::string format_complex(const gaussian_integer& z) {
    int r = z.real();
    int i = z.imag();

    if (r == 0 && i == 0) return "0";
    if (i == 0) return std::to_string(r);
    if (r == 0) {
        if (i == 1) return "i";
        if (i == -1) return "-i";
        return std::to_string(i) + "i";
    }

    std::string res = std::to_string(r);
    if (i > 0) {
        res += "+";
        res += (i == 1) ? "i" : std::to_string(i) + "i";
    } else {
        res += "-";
        res += (i == -1) ? "i" : std::to_string(std::abs(i)) + "i";
    }
    return res;
}

gaussian_integer operator%(const gaussian_integer& num,
                           const gaussian_integer& den) {
  std::complex<double> num_d{num};
  std::complex<double> den_d{den};

  std::complex<double> result_d = num_d / den_d;

  gaussian_integer rounded_div{
    static_cast<int>(std::round(result_d.real())),
    static_cast<int>(std::round(result_d.imag()))
  };

  return num - rounded_div * den;
}

int main(int argc, char *argv[]) {
  assert(argc == 3);
  int ma = atoi(argv[1]);
  int mi = atoi(argv[2]);
  assert(ma > mi);
  gaussian_integer m{ma, mi}, I{0, 1};
  int n = norml2(m);

  std::cout << "digraph G {\n"
            << "layout=neato\noverlap = \"false\"\nsep = \"+0.1\"\n";
  for (int r=-ma; r <= ma; ++r) {
    for (int i=-ma; i <= ma; ++i) {
      gaussian_integer a{r, i};
      if (norml2(a) <= n/2) {
        gaussian_integer s = (a*a+1+I)%m;
        assert(norml2(s) <= n/2);
        std::cout << "\"" << format_complex(a) << "\"->"
                  << "\"" << format_complex(s) << "\"\n";
      }
    }
  }
  std::cout << "}\n";

  return 0;
}
