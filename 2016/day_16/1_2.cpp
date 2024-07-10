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

string dragon(string s) {
    string b = s; 
    reverse(b.begin(), b.end());
    string d;
    for (char c : b) {
        if (c == '1') {
            d += '0';
        } else {
            d += '1';
        }
    }
    return s + '0' + d;
}

string checksum(string s) {
    string c;
    for (int i  = 0 ; i < s.size() - 1 ; i+=2) {
        char f = s[i];
        char e = s[i+1];
        if (f == e) {
            c += '1';
        } else {
            c += '0';
        }
    }
    return c;
}

int main() {
    string s = read_file();
    int disk_size = 35651584;

    while (s.size() < disk_size) {
        s = dragon(s);
    }
    s = s.substr(0, disk_size);
    
    while ((s.size() % 2) == 0) {
        s = checksum(s);
    }
    cout << s << endl;
    return 0;
}