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

int main() {
    int start = 3005290;     
    int base = 1;
    while (base < start) {
        base *= 2;
    }
    base = base / 2;
    int diff = start - base;
    int i  = 1;
    int N = (2*diff) + 1;
    cout << N << endl;
    return 0;
}