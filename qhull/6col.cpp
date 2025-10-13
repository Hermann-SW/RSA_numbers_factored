/*
g++ -O3 -Wall -Wextra -pedantic 6col.cpp -o 6col
cpplint --filter=-legal/copyright,-runtime/references 6col.cpp 
cppcheck --enable=all --suppress=missingIncludeSystem 6col.cpp --check-config
*/
#include <math.h>

#include <iostream>
#include <fstream>
#include <sstream>
#include <cassert>
#include <algorithm>
#include <vector>

#include "planar_graph_playground/c++/util.hpp"
#include "planar_graph_playground/c++/undirected_graph.hpp"

typedef std::vector<int> piii;
#define ADD(v, a, b, i) \
  { piii X = {a, b, i}; piii Y = {b, a, i}; v.push_back(a < b?X:Y); }
bool piiile(piii& l, piii& r) {
  return l[0] < r[0] || (l[0] == r[0] && l[1] < r[1]);
}
void OUT(piii& p)  { std::cout << p[0] << " " << p[1] << " " << p[2] << "\n"; }

int d2i(double d) { return static_cast<int>(round(d)); }

int main(int argc, char *argv[]) {
  assert(argc == 3);
  assert(atoi(argv[1]) % 4 == 1);
  assert(atoi(argv[2]) % 4 == 1);
  assert(atoi(argv[1]) < atoi(argv[2]));
  int d, n, f, m, N = atoi(argv[1]) * atoi(argv[2]);
  double x, y, z;

  std::string rgb[]={"0 0 1", "0 1 0", "1 0 0", "0 1 1", "1 0.5 0", "0 0.5 1"};

  std::stringstream s;
  s << "n=" << N << " gp -q < nbox.gp | qconvex o > tmp";
  assert(0 == system(s.str().c_str()));

  std::ifstream is("tmp");
  is >> d >> n >> f >> m;

  std::vector<std::vector<int>> C;
  for (int i = 0; i < n; ++i) {
    is >> x >> y >> z;
    std::vector<int> p = {d2i(x), d2i(y), d2i(z)};
    C.push_back(p);
  }

  std::vector<piii> v;
  std::vector<piii> vs;

  for (int i = 0; i < f; ++i) {
    int l, x, y, z;
    std::vector<int> F;
    is >> l >> x;
    y = x;
    F.push_back(x);
    for (int k = 1; k < l; ++k) {
      is >> z;
      ADD(v, y, z, i);
      F.push_back(z);
      y = z;
    }
    ADD(v, y, x, i);
    vs.push_back(F);
  }

  std::sort(v.begin(), v.end(), piiile);

  graph D;

  for (int k = 0; k < f; ++k)  new_vertex(D);

  for (unsigned i = 0; i < v.size(); i+=2) {
    assert(v[i][0] == v[i+1][0]);
    assert(v[i][1] == v[i+1][1]);
    assert(v[i][2] != v[i+1][2]);
    new_edge(D, v[i][2], v[i+1][2]);
  }

  std::vector<int> col = six_coloring(D);

  std::cout << n_faces_planar(D) << " vertices, " << n_edges(D) << " edges, " \
            << n_vertices(D) << " faces (" \
            << *std::max_element(col.begin(), col.end()) + 1 << " colors)\n";

  std::ofstream os("tmp.off");

  os <<
    "{appearance {-edge -evert linewidth 2} LIST #  | qconvex G TO tmp\n";

  std::vector<int> cF(f);

  for (int v = 0; v < f; ++v) {
    os << "{ OFF " << vs[v].size() << " 1 1 #\n";
    for (unsigned i = 0; i < vs[v].size(); ++i) {
      int w = vs[v][i];
      os << C[w][0] << " " << C[w][1] << " " << C[w][2] << "\n";
    }
    os << vs[v].size();
    for (unsigned i = 0; i < vs[v].size(); ++i)  os << " " << i;
    os << " " << rgb[col[v]] << " 1.0 }\n";

    cF[vs[v].size()]++;
  }

  os << "}\n";
  os.close();

  std::cout << "\nface lengths\n";
  for (int l = 0; l < f; ++l) {
    if (cF[l] > 0)  std::cout << cF[l] << "×" << l << "\n";
  }

  assert(0 == system("geomview -wpos 900,900@960,20 tmp.off"));

  return 0;
}
