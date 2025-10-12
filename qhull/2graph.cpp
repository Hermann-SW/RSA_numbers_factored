/*
g++ -O3 -Wall -Wextra -pedantic 2graph.cpp -o 2graph
cpplint --filter=-legal/copyright,-runtime/references 2graph.cpp 
cppcheck --enable=all --suppress=missingIncludeSystem 2graph.cpp --check-config
*/
#include <iostream>
#include <fstream>
#include <sstream>
#include <cassert>
#include <algorithm>
#include <vector>

typedef std::pair<int, int> pii;
#define ADD(v, a, b) v.push_back(a < b?pii(a, b):pii(b, a))
constexpr bool piile(const pii& l, const pii& r) {
  return l.first < r.first || (l.first == r.first && l.second < r.second);
}
void OUT(pii& p)  { std::cout << p.first << " " << p.second << " 0\n"; }

int main(int argc, char *argv[]) {
  assert(argc == 2);
  int d, n, f, m, N = atoi(argv[1]);
  double x, y, z;

  std::stringstream s;
  s << "n=" << N << " gp -q < nbox.gp | qconvex o > tmp";
  assert(0 == system(s.str().c_str()));

  std::ifstream is("tmp");
  is >> d >> n >> f >> m;

  std::cout << "LEDA.GRAPH\n";
  std::cout << "point3D\n";
  std::cout << "int\n";
  std::cout << n << "\n";

  for (int i = 0; i < n; ++i) {
    is >> x >> y >> z;
    std::cout << "(" << x << "," << y << "," << z << ")\n";
  }

  std::vector<pii> v;

  for (int i = 0; i < f; ++i) {
    int l, x, y, z;
    is >> l >> x;
    y = x;
    for (int k = 1; k < l; ++k) {
      is >> z;
      ADD(v, y, z);
      y = z;
    }
    ADD(v, y, x);
  }

  std::sort(v.begin(), v.end(), piile);
  auto last = std::unique(v.begin(), v.end());

  std::cout << m << "\n";
  std::for_each(v.begin(), last, OUT);

  return 0;
}
