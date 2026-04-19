/*
   determine shortest path length along convex hull edges between two
   n=x^2+y^2+0^2 points on equator, 6 for 116561=229*509
   $ ./2graph 116561 > 116561.u 
   hermann@8840hs:~/RSA_numbers_factored/qhull$ ./equator.shortest_path 116561.u
   N=116561
   found1 31 340 0  2315
   found2 119 320 0  2839
   4224 vertices, 10776 edges
   distance(2839) = 6
   max distance = 49
   hermann@8840hs:~/RSA_numbers_factored/qhull$

   f=equator.shortest_path
   g++ -O3 -Wall -Wextra -pedantic $f.cpp -o $f
   cpplint --filter=-legal/copyright,-runtime/references $f.cpp 
   cppcheck --enable=all --suppress=missingIncludeSystem $f.cpp --check-config
*/
#include <time.h>
#include <iostream>
#include <utility>
#include <fstream>

#include <boost/graph/graph_traits.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/dijkstra_shortest_paths.hpp>
#include <boost/property_map/property_map.hpp>
#include <boost/graph/graph_utility.hpp>

using namespace boost; // NOLINT

int is_square(int n) {
    int s = round(sqrt(n));
    if (s*s == n) { return s; }
    return 0;
}

int main(int, char*argv[]) {
    typedef adjacency_list< listS, vecS, undirectedS, no_property,
        property< edge_weight_t, int > >
        graph_t;
    typedef graph_traits< graph_t >::vertex_descriptor vertex_descriptor;
    typedef std::pair< int, int > Edge;

    int n, m;
    std::string line;

    std::ifstream in(argv[1]);
    assert(in);

    std::getline(in, line);
    in >> line >> line >> n;

    int N = -1, s0, s1, s2, s3, v0 = -1, v1 = -1;

    for (int i=0; i < n; ++i) {
        int x, y, z;
        char c;
        in >> c >> x >> c >> y >> c >> z >> c;
        if (N == -1) {
            N = x*x + y*y + z*z;
            std::cout << "N=" << N << "\n";
            for (s0=1;; ++s0) {
                s1 = is_square(N-s0*s0);
                if (s1) break;
            }
            for (s2=s0+1;; ++s2) {
                s3 = is_square(N-s2*s2);
                if (s3) break;
            }
        }
        if (x == s0 && y == s1) {
            std::cout << "found1 " << x << " " << y << " " << z << "  "
                      << i << "\n";
            v0 = i;
        } else {
            if (x == s2 && y == s3) {
                std::cout << "found2 " << x << " " << y << " " << z << "  "
                          << i << "\n";
                v1 = i;
            }
        }
    }

    in >> m;

    Edge *edge_array = new Edge[m];
    int *weights = new int[m];

    for (int i=0; i < m; ++i) {
        int s, t, v;
        in >> s >> t >> v;
        edge_array[i] = Edge(s, t);
        weights[i] = 1;
    }


    graph_t g(edge_array, edge_array + m, weights, n);
    std::vector< vertex_descriptor > p(num_vertices(g));
    std::vector< int > d(num_vertices(g));
    vertex_descriptor s = vertex(v0, g);

    dijkstra_shortest_paths(g, s,
        predecessor_map(boost::make_iterator_property_map(
                            p.begin(), get(boost::vertex_index, g)))
            .distance_map(boost::make_iterator_property_map(
                d.begin(), get(boost::vertex_index, g))));

    std::cout << n << " vertices, " << m << " edges\n";
    std::cout << "distance(" << v1 << ") = " << d[v1] << "\n";

    std::cout << "max distance = "
              << *std::max_element(d.begin(), d.end()) << "\n";

    return EXIT_SUCCESS;
}
