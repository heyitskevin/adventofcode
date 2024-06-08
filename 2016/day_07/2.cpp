#include <vector>
#include <string>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>

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

bool valid(string test) {
    return (test[0] == test[2]) && (test[0] != test[1]);
}

int is_super_secret(string ip) {
    set<string> ABA;
    set<string> BAB;
    bool in_brackets = false;

    for (int i=0; i < ip.size() - 2; i++) {
        if (ip[i] == '[') {
            in_brackets = true;
        }
        if (ip[i] == ']') {
            in_brackets = false;
        }

        string lookahead = ip.substr(i, 3);
        if (valid(lookahead)) {
            if (in_brackets) {
                BAB.insert(lookahead);
            } else {
                ABA.insert(lookahead);
            }
        }
    }

    if (ABA.size() == 0) {
        return 0;
    }
    int supporters = 0;
    for (string a : ABA) {
        string flip({a[1], a[0], a[1]});
        if (BAB.find(flip) != BAB.end()) {
            return 1;
        }
    }

    return 0;
}

int main() {
    vector<string> data = read_file();
    int s = 0;
    for (string d : data) {
        s += is_super_secret(d);
    }

    cout << s << endl;
    return 0;
}