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

#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/trim_all.hpp>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/join.hpp>

using namespace std;
using namespace boost;

vector<vector<int> > read_file() {
    string filename = "processed_input.txt";
    vector<vector<int> > data;
    ifstream file(filename);
    if (!file) {
        cerr << "could not open" << endl;
    }

    string ln;
    vector<string> container;
    while (getline(file, ln)) {
        // I think I might be getting too sussy w / these neseted function calls but whatever
        split(container, ln , is_any_of(" "));
        vector<int> d;
        for (string s : container) {
            d.push_back(stoi(s));
        }
        data.push_back(d);
    }

    return data;
}

int mod(int a, int b) {
    return (b + a % b) % b;
}
// position P(t) is (t+offset) % slots
// we want P to be 0, -1, -2, -3, -4, -5
int crt(vector<vector<int> > data) {
    // We solve for t0 = time when at the first ring so true solution is t0-1
    vector<int> divisors;
    vector<int> dividend;
    int time_offset = 0;
    for (vector<int> v : data) {
        divisors.push_back(v[1]);
        time_offset = -(v[0] - 1);

        dividend.push_back(mod(v[1] - v[2] + time_offset, v[1]));
    }
    int X = 1;
    bool found = false;
    while (!found) {
        int i = 0;
        for (i ; i < dividend.size(); i++) {
            if (mod(X, divisors[i]) != dividend[i]) {
                break;
            }
        }
        if (i == dividend.size()) {
            found = true;
            break;
        }
        X++;
    }
    
    return X;
}

int main() {
    vector<vector<int> > d = read_file();
    vector<vector<int> > ex = {{1, 5, 4}, {2, 2, 1}};
    int r = crt(d);
    cout  << "soln: " << r - 1 << endl;
    return 0;
}