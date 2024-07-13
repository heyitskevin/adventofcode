#include <vector>
#include <string>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <regex>
#include <map>
#include <set>
#include <cmath>

using namespace std;

int brute_rotate(int length) {
    int start = length; 
    vector<int> s(start);
    for (int ix = 0; ix<start; ix++) {
        s[ix] = ix + 1;
    }
    int offset = 0;
    while (s.size() > 1) {
        int div_ix = s.size() / 2;
        s[div_ix] = 0;
        vector<int> nx;
        for (int v = 0; v < s.size(); v++) {
            if(s[v]) {
                nx.push_back(s[v]);
            }
        }
        rotate(nx.begin(), nx.begin() + 1, nx.end());
        s = nx;
        offset++;
    }
    return s[0];
}


int main() {
    int big = 3005290;
    // for (int i = 28; i < 84; i++) {
    //     cout << i << " " << brute_rotate(i) << " " << 2*i - 81 << endl;
    // }
    // cout << big << " " << func(big) << endl;
    int P = 1;
    while (P < big) {
        P *= 3;
    }
    P /= 3;
    int D = big - P;
    if (P <= D <= 2*P) {
        cout << D << endl;
    } else {
        cout << 2*big - 3*P << endl;
    }
    // for some value N, take the largest power of 3 LTE N as P
    // then if diff D is between P and 2P inclusive output D
    // else output P + (D - P)*2
    // P + 2D - 2P
    // 2D - P
    // 2(N - P) - P
    // 2N - 3P
    // cout 
    return 0;
}