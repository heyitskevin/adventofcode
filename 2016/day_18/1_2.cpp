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

const char safe = '.';
const char trap = '^';

string read_file() {
    string filename = "input.txt";
    string data;
    ifstream file(filename);
    if (!file) {
        cerr << "could not open" << endl;
    }
    string ln;
    vector<string> container;
    while (getline(file, ln)) {
        data = ln;
    }
    return data;
}

char make_tile(char left, char right, char center) {
    if ((left == trap) && (center == trap) && (right == safe)) {
        return trap;
    }
    if ((left == safe) && (center == trap) && (right == trap)) {
        return trap;
    }
    if ((left == trap) && (center == safe) && (right == safe)) {
        return trap;
    }
    if ((right == trap) && (center == safe) && (left == safe)) {
        return trap;
    }
    return safe;
}

pair<string, int> make_next_row(string prev_row) {
    int safe_tiles = 0;
    string next_row = "";

    for (int i = 0; i < prev_row.size(); i++) {
        char left, right, center;
        if (i == 0) {
            left = safe;
        } else {
            left = prev_row[i-1];
        }
        if (i == prev_row.size() - 1) {
            right = safe;
        } else {
            right = prev_row[i + 1];
        }
        center = prev_row[i];
        char next_tile = make_tile(left, right, center);
        if (next_tile == safe) {
            safe_tiles++;
        }
        next_row += next_tile;
    }
    return make_pair(next_row, safe_tiles);
}

int main() {
    string row = read_file();
    int s = 0;
    for (char c : row) {
        if (c == safe) {
            s++;
        }
    }
    int count = 1;
    while (count < 400000) {
        pair<string, int> nxt = make_next_row(row);
        s += nxt.second;
        row = nxt.first;
        count++;
    }
    cout << s << endl;
}