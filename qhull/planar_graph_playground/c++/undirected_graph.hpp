#ifndef _HOME_PI_PLANAR_GRAPH_PLAYGROUND_CPP_UNDIRECTED_GRAPH_HPP_
#define _HOME_PI_PLANAR_GRAPH_PLAYGROUND_CPP_UNDIRECTED_GRAPH_HPP_
// Copyright: https://mit-license.org/
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <cassert>

typedef int vertex;
typedef int edge;

typedef std::vector<edge> Vertex;
typedef std::vector<std::array<int, 2>> Edge;

#define _f(g) if (g) g

struct planar_face_traversal_visitor {
    std::function<void()> begin_traversal = 0;
    std::function<void()> end_traversal = 0;
    std::function<void()> begin_face = 0;
    std::function<void()> end_face = 0;
    std::function<void(vertex)> next_vertex = 0;
    std::function<void(edge)> next_edge = 0;
    std::function<void(vertex, edge)> next_vertex_edge = 0;
};

struct compact5_traversal_visitor {
    std::function<void()> begin_traversal = 0;
    std::function<void()> end_traversal = 0;
    std::function<void(vertex)> begin_vertex = 0;
    std::function<void(vertex)> end_vertex = 0;
    std::function<void(edge)> next_edge = 0;
    std::function<void(vertex, edge)> next_vertex_edge = 0;
};

class graph {
 public:
    std::vector<Vertex> V;
    std::vector<Edge> E;

explicit graph(int n = 0, int m = 0) : V(std::vector<Vertex>(n, Vertex(0))),
                                       E(std::vector<Edge>(m, Edge(0))) {
    }
};

graph empty_graph() {
    return graph();
}

int degree(const graph& G, vertex v) {
    return G.V[v].size();
}

int n_vertices(const graph& G) {
    return G.V.size();
}

int n_edges(const graph& G) {
    return G.E.size();
}

int n_faces(const graph& G, int chi) {
    return chi + n_edges(G) - n_vertices(G);
}

int n_faces_planar(const graph& G) {
    return n_faces(G, 2);
}

template <typename F>
void forall_vertices(const graph& G, const F& f) {
    for (vertex v = 0; v < n_vertices(G); v += 1) {
        f(v);
    }
}

int max_degree(const graph& G) {
    int mdeg = -1;

    forall_vertices(G, [&G, &mdeg](vertex v) {
        if (degree(G, v) > mdeg) {
            mdeg = degree(G, v);
        }
    });

    return mdeg;
}

template <typename F>
void forall_edges(const graph& G, const F& f) {
    for (edge e = 0; e < n_edges(G); e += 1) {
        f(e);
    }
}

edge any_edge(const graph& G) {
    return (G.E.size() > 0) ? 0 : -1;
}

edge first_incident_edge(const graph& G, vertex v) {
    return degree(G, v) == 0 ? -1 : G.V[v][0];
}

template <typename F>
void forall_incident_edges(const graph& G, vertex v, const F& f) {
    std::for_each(G.V[v].cbegin(), G.V[v].cend(), f);
}

template <typename F>
void forall_incident2_edges(const graph& G, std::vector<vertex>& a,
                            const F& f) {
    std::for_each(a.cbegin(), a.cend(), [&G, &f](vertex v) {
        std::for_each(G.V[v].cbegin(), G.V[v].cend(), [v, &f](edge e) {
            f(v, e);
        });
    });
}

vertex source(const graph& G, edge e) {
    return G.E[e][0][0];
}

vertex target(const graph& G, edge e) {
    return G.E[e][1][0];
}

vertex opposite(const graph& G, vertex v, edge e) {
    return (v == source(G, e)) ? target(G, e) : source(G, e);
}

int ind(const graph& G, vertex v, edge e) {
    return (v == source(G, e)) ? 0 : 1;
}

edge next_incident_edge(const graph& G, vertex v, edge e) {
    return G.V[v][(G.E[e][ind(G, v, e)][1] + 1) % degree(G, v)];
}

edge prev_incident_edge(const graph& G, vertex v, edge e) {
    return G.V[v][(G.E[e][ind(G, v, e)][1] + degree(G, v) - 1) % degree(G, v)];
}

vertex new_vertex(graph& G) {
    vertex v = n_vertices(G);
    G.V.push_back({});
    return v;
}

edge new_edge_vertex(graph& G, vertex v, edge e) {
    G.E[e].push_back({v, degree(G, v)});
    G.V[v].push_back(e);
    return e;
}

edge new_edge1(graph& G, vertex v) {
    edge e = n_edges(G);
    G.E.push_back({});
    return new_edge_vertex(G, v, e);
}

edge new_edge(graph& G, vertex v, vertex w) {
    return new_edge_vertex(G, w, new_edge1(G, v));
}

graph new_graph(int n, int m = 0) {
    return graph(n, m);
}


void remove_edge1(graph& G, vertex v, edge e) {
    int i = ind(G, v, e);
    edge f = pop(G.V[v]);
    if (e != f) {
        int j = ind(G, v, f);
        G.E[f][j][1] = G.E[e][i][1];
        G.V[v][G.E[f][j][1]] = f;
    }
    G.E[e][i][1] = -1;
}

void print_vertex(const graph& G, vertex v) {
    std::cout <<  v <<  ":";
    forall_incident_edges(G, v, [&G, v](edge e) {
        std::cout << " (" << e << ")" << opposite(G, v, e);
    });
    std::cout << std::endl;
}

void print_graph(const graph& G, const char *str = "") {
    std::cout << str << n_vertices(G) << " vertices, "
                     << n_edges(G) << " edges" << std::endl;
    forall_vertices(G, [&G](vertex v) {
        print_vertex(G, v);
    });
}

void compact5_traversal(graph& G, compact5_traversal_visitor c5v) {
    std::vector<vertex> S;
    std::vector<bool> small(n_vertices(G), false);

    _f(c5v.begin_traversal)();

    S.reserve(n_vertices(G));
    forall_vertices(G, [&G, &S, &small](vertex v) {
        if (degree(G, v) < 6) {
            S.push_back(v);
            small[v] = true;
        }
    });

    while (S.size() > 0) {
        vertex v = pop(S);

        _f(c5v.begin_vertex)(v);
        forall_incident_edges(G, v, [&G, v, &S, &small, &c5v](edge e) {
            vertex w = opposite(G, v, e);
            _f(c5v.next_edge)(e);
            _f(c5v.next_vertex_edge)(v, e);
            remove_edge1(G, w, e);
            if ((!small[w]) && (degree(G, w) < 6)) {
                S.push_back(w);
                small[w] = true;
            }
        });
        _f(c5v.end_vertex)(v);
    }
    _f(c5v.end_traversal)();
}

edge compact5_find(const graph& C, vertex v, vertex w) {
    auto res = std::find_if(C.V[v].cbegin(), C.V[v].cend(), [&C, v, w](edge e) {
        return (opposite(C, v, e) == w);
    });
    if (res != C.V[v].cend()) {
        return *res;
    }
    res = std::find_if(C.V[w].cbegin(), C.V[w].cend(), [&C, v, w](edge e) {
        return (opposite(C, w, e) == v);
    });
    if (res != C.V[w].cend()) {
        return *res;
    }
    return -1;
}

graph from_adjacency_list(const std::vector<std::vector<vertex>>& L) {
    graph C = new_graph(L.size());

    for (vertex v = 0; v < static_cast<int>(L.size()); ++v) {
        std::for_each(L[v].cbegin(), L[v].cend(), [&C, v](vertex w) {
            if (v < w) {
                new_edge(C, v, w);
            }
        });
    }

    compact5_traversal(C, {});

    if (max_degree(C) > 5) {
        return empty_graph();
    }

    graph G = new_graph(L.size());

    for (vertex v = 0; v < static_cast<int>(L.size()); ++v) {
        std::for_each(L[v].cbegin(), L[v].cend(), [&C, &G, v](vertex w) {
            if (v < w) {
                new_edge1(G, v);
            } else {
                edge e = compact5_find(C, v, w);
                assert(e != -1);
                new_edge_vertex(G, v, e);
            }
        });
    }

    return G;
}

graph from_adjacency_list_lookup(const std::vector<std::vector<vertex>>& L) {
    graph G = new_graph(L.size());

    #define choose2(n) ((n) * ((n) + 1) / 2)
    std::vector<edge> lookup(choose2(L.size()), -1);;

    for (vertex v = 0; v < static_cast<int>(L.size()); ++v) {
        for (int j = 0; j < static_cast<int>(L[v].size()); ++j) {
            vertex w = L[v][j];

            if (v < w) {
                lookup[choose2(w) + v] = new_edge1(G, v);
            } else {
                edge e = lookup[choose2(v) + w];
                if (e == -1) {
                    return empty_graph();
                }
                new_edge_vertex(G, v, e);
            }
        }
    }

    return G;
}

std::vector<int> six_coloring(graph& G) {
    std::vector<vertex> S;
    std::vector<int> col = filled_vector(n_vertices(G), -1);
    std::vector<int> mc = {0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0, 4,
                           0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0, 5,
                           0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0, 4,
                           0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0};

    S.reserve(n_vertices(G));
    compact5_traversal(G, { 0, 0,  /*begin_vertex*/ [&S](vertex v) {
        S.push_back(v);
    }});

    while (S.size() > 0) {
        int bs = 0;
        vertex v = pop(S);
        forall_incident_edges(G, v, [&G, &col, v, &bs](edge e) {
            bs |= 1 << col[opposite(G, v, e)];
        });
	assert(bs < static_cast<int>(mc.size()));
        col[v] = mc[bs];
    }
    return col;
}


std::vector<vertex> face_vertices(const graph& Emb, vertex v, edge e) {
    edge o = e;
    std::vector<vertex> face;
    do {
        v = opposite(Emb, v, e);
        e = next_incident_edge(Emb, v, e);
        face.push_back(v);
    } while (e != o);
    return face;
}

void traverse_face(const graph& G, std::vector<std::array<bool, 2>>& visited,
                   vertex v, edge e, int i,
                   planar_face_traversal_visitor& pftv) {
    while (!visited[e][i]) {
        visited[e][i] = true;
        _f(pftv.next_vertex)(v);
        _f(pftv.next_edge)(e);
        _f(pftv.next_vertex_edge)(v, e);
        v = opposite(G, v, e);
        e = next_incident_edge(G, v, e);
        i = ind(G, v, e);
    }
}

void check_traverse(const graph& G, std::vector<std::array<bool, 2>>& visited,
                    vertex v, edge e, planar_face_traversal_visitor pftv) {
    int i = ind(G, v, e);
    if (!visited[e][i]) {
        _f(pftv.begin_face)();
        traverse_face(G, visited, v, e, i, pftv);
        _f(pftv.end_face)();
    }
}

void check_traverse2(const graph& G, std::vector<std::array<bool, 2>>& visited,
                     edge g, planar_face_traversal_visitor pftv) {
    check_traverse(G, visited, source(G, g), g, pftv);
    check_traverse(G, visited, target(G, g), g, pftv);
}

void planar_face_traversal(const graph& G, planar_face_traversal_visitor pftv) {
    std::vector<std::array<bool, 2>> visited(n_edges(G),
                                           std::array<bool, 2>({false, false}));
    _f(pftv.begin_traversal)();

    forall_edges(G, [&G, &visited, &pftv](edge g) {
        check_traverse2(G, visited, g, pftv);
    });

    _f(pftv.end_traversal)();
}

bool is_embedding(const graph& G) {
    int nfaces = 0;

    planar_face_traversal(G, { 0, 0, /*begin_face*/ [&nfaces]() {
        nfaces += 1;
    }});

    return n_vertices(G) - n_edges(G) + nfaces == 2;
}

std::vector<std::vector<vertex>> pentagons(const graph& Emb) {
    std::vector<std::vector<vertex>> pent;
    std::vector<vertex> face;

    planar_face_traversal(Emb, { 0, 0, /*begin_face*/ [&face]() {
        face.clear();
    }, /*end_face*/  [&pent, &face]() {
        if (face.size() == 5) {
            pent.push_back(face);
        }
    }, /*next_vertex*/ [&face](vertex v) {
        face.push_back(v);
    }});

    return pent;
}

graph dual_graph(const graph& G) {
    int last_face = -1;
    graph D = new_graph(n_faces_planar(G), n_edges(G));

    planar_face_traversal(G, { 0, 0, /*begin_face*/ [&last_face]() {
        last_face += 1;
    }, 0, 0, /*next_edge*/ [&D, &last_face](edge e) {
        new_edge_vertex(D, last_face, e);
    }});

    return D;
}

bool is_identical_graph(const graph& G, const graph& H) {
    if (n_vertices(G) != n_vertices(H)) {
        return false;
    }
    if (n_edges(G) != n_edges(H)) {
        return false;
    }
    bool ret = true;
    forall_vertices(G, [&G, &H, &ret](vertex v) {
        if (degree(G, v) != degree(H, v)) {
            ret = false;
        }
        for (int i = 0; i < static_cast<int>(G.V.size()); ++i) {
            if (G.V[v][i] != H.V[v][i]) {
                ret = false;
            }
        }
    });
    forall_edges(G, [&G, &H, &ret](edge e) {
        if (G.E[e].size() != H.E[e].size()) {
            ret = false;
        }
        for (int i = 0; i < static_cast<int>(G.E[e].size()); ++i) {
            if (G.E[e][i].size() != H.E[e][i].size()) {
                ret = false;
            }
            for (int j = 0; j < static_cast<int>(G.E[e][i].size()); ++j) {
                if (G.E[e][i][j] != H.E[e][i][j]) {
                    ret = false;
                }
            }
        }
    });
    return ret;
}
#endif  // _HOME_PI_PLANAR_GRAPH_PLAYGROUND_CPP_UNDIRECTED_GRAPH_HPP_
