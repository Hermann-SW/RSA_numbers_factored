#ifndef _HOME_PI_PLANAR_GRAPH_PLAYGROUND_CPP_UTIL_HPP_
#define _HOME_PI_PLANAR_GRAPH_PLAYGROUND_CPP_UTIL_HPP_
// Copyright: https://mit-license.org/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>

#include <vector>
#include <iostream>

std::vector<std::vector<int>> parse2(char **buf);
char *readFile(const char *name);
std::vector<std::vector<int>> parse2file(const char *name);

template <typename T>
T pop(std::vector<T>&v) {
    T b = v.back();
    v.pop_back();
    return b;
}

template <typename P>
std::vector<P> filled_vector(int n, P v) {
    return std::vector<P>(n, v);
}

template <typename P>
std::vector<std::vector<P>> filled_array(int n, int m, P v) {
    std::vector<std::vector<P>> zm(n);
    for (int j = 0; j < m; ++j) {
        zm[j] = filled_array(m, 1, v);
    }
    return zm;
}
#endif  // _HOME_PI_PLANAR_GRAPH_PLAYGROUND_CPP_UTIL_HPP_
