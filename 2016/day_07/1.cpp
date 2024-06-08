#include <vector>
#include <string>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>

using namespace std;
vector<string> read_file() {
    string filename = "input.txt";
    vector<string> data;

    ifstream file(filename);
    if (!file) {
        cerr << "could not open file" << endl;
    }
    string line;
    while (getline(file, line)) {
        data.push_back(line);
    }
    return data;
}

bool is_abba(string test) {
    string rev = test.substr(2, 2);
    std::reverse(rev.begin(), rev.end());
    if (test[0] == test[1]) {
        return false;
    }
    return test.substr(0, 2) == rev;
}

int count_valid_ips(string ip) {
    int valid = 0;
    bool in_bracket = false;
    for (int i=0; i<ip.size() - 3; i++) {
        if (ip[i] == '[') {
            in_bracket = true;
        }
        if (ip[i] == ']') {
            in_bracket = false;
        }
        string lookahead = ip.substr(i, 4);
        if (in_bracket && is_abba(lookahead)) {
            return 0;
        }
        if (!in_bracket && is_abba(lookahead)) {
            valid++;
        }
    }
    if (valid > 0) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    vector<string> dat = read_file();
    int res = 0;
    for (string d : dat) {
        res += count_valid_ips(d);
    }
    cout << res << endl;
    return 0;
}