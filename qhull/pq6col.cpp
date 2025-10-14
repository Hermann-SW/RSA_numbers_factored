/*
   show 6 face colors convex hull; integer x,y,z points with n=p*q=x^2+y^2+z^2
   $ ./pq6col 5 13

   f=pq6col
   g++ -O3 -Wall -Wextra -pedantic $f.cpp -o $f
   cpplint --filter=-legal/copyright,-runtime/references $f.cpp 
   cppcheck --enable=all --suppress=missingIncludeSystem $f.cpp --check-config
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

typedef std::vector<int> v3i;
bool v3ile(v3i& l, v3i& r) {
  return l[0] < r[0] || (l[0] == r[0] && l[1] < r[1]);
}
int d2i(double d) { return static_cast<int>(round(d)); }

bool is_odd_prime(int n) {
  if (n % 2 == 0)  return false;
  for (int d=3; d*d <= n; d+=2) {
    if (n % d == 0)  return false;
  }
  return true;
}

int main(int argc, char *argv[]) {
  assert(argc == 3);
  assert(atoi(argv[1]) % 4 == 1);
  assert(atoi(argv[2]) % 4 == 1);
  assert(atoi(argv[1]) < atoi(argv[2]));
  assert(is_odd_prime(atoi(argv[1])));
  assert(is_odd_prime(atoi(argv[2])));
  assert(0 == system("gp -h > /dev/null"));
  assert(0 == system("qconvex > /dev/null"));
  assert(0 == (0xfe & system("geomview -foo 2>/dev/null")));

  int d, n, f, m, N = atoi(argv[1]) * atoi(argv[2]);
  double x, y, z;

  //                  blue     green    red      cyan     orange     azure
  std::string rgb[]={"0 0 1", "0 1 0", "1 0 0", "0 1 1", "1 0.5 0", "0 0.5 1"};


  // create file with qconvex for graph creation
  std::stringstream s;
  s << "n=" << N << " gp -q < nbox.gp | qconvex o > tmp";
  assert(0 == system(s.str().c_str()));


  // read file created with qconvex
  std::ifstream is("tmp");
  is >> d >> n >> f >> m;

  std::vector<std::vector<int>> XYZ;
  for (int i = 0; i < n; ++i) {
    is >> x >> y >> z;
    XYZ.push_back({d2i(x), d2i(y), d2i(z)});
  }

  std::vector<v3i> v;
  std::vector<v3i> vs;
  std::vector<int> cF(f);

  for (int i = 0; i < f; ++i) {
    int l, x, y, z;
    std::vector<int> F;
    is >> l >> x;
    y = x;
    F.push_back(x);
    for (int k = 1; k < l; ++k) {
      is >> z;
      v.push_back({std::min(y, z), std::max(y, z), i});
      F.push_back(z);
      y = z;
    }
    v.push_back({std::min(y, x), std::max(y, x), i});
    vs.push_back(F);
    cF[F.size()]++;
  }

  // O(n*log(n)), but avoids need for planar embeddimg algorithm
  std::sort(v.begin(), v.end(), v3ile);


  // create dual graph of polyhedron
  graph D;

  for (int k = 0; k < f; ++k)  new_vertex(D);

  for (unsigned i = 0; i < v.size(); i+=2) {
    assert(v[i][0] == v[i+1][0]);
    assert(v[i][1] == v[i+1][1]);
    assert(v[i][2] != v[i+1][2]);
    new_edge(D, v[i][2], v[i+1][2]);
  }

  // vertex six-coloring of D is face coloring of polyhedron
  std::vector<int> col = six_coloring(D);


  // statistics
  std::cout << "n=" << N << ": " << n_faces_planar(D) << " vertices, " \
            << n_edges(D) << " edges, " << n_vertices(D) << " faces (" \
            << *std::max_element(col.begin(), col.end()) + 1 << " colors)\n" \
            << "\nface lengths\n";
  for (int l = 0; l < f; ++l) {
    if (cF[l] > 0)  std::cout << cF[l] << "×" << l << "\n";
  }


  // create OFF file for geomview to display, with at most 6 face colors
  std::ofstream os("tmp.off");

  os <<        // -edge does not display edges, not needed by face 6-coloring
    "{appearance {-edge -evert linewidth 2} LIST #  | qconvex G TO tmp\n";

  for (int v = 0; v < f; ++v) {
    os << "{ OFF " << vs[v].size() << " 1 1 #\n";
    for (unsigned i = 0; i < vs[v].size(); ++i) {
      int w = vs[v][i];
      os << XYZ[w][0] << " " << XYZ[w][1] << " " << XYZ[w][2] << "\n";
    }
    os << vs[v].size();
    for (unsigned i = 0; i < vs[v].size(); ++i)  os << " " << i;
    os << " " << rgb[col[v]] << " 1.0 }\n";
  }

  os << "}\n";
  os.close();


  // display polyhedron with geomview
  assert(0 == system("geomview -wpos 900,900@960,20 tmp.off"));


  return 0;
}
