#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <utility>
#include <map>

using namespace std;

vector<string> read_file() {
    string filename = "input.txt";
    vector<string> data;

    std::ifstream file(filename);
    if (!file) {
        cerr << "failed to open file" << endl;
    }

    string line;

    while (getline(file, line)) {
        std::istringstream iss(line);
        string ln;
        while (iss >> ln) {
            data.push_back(ln);
        }
    }

    return data;
}

string get_most_freq(vector<string> signals) {
    string res = "";
    // assume the size of each row is the same so just look at the first element
    map<char, int> buckets[signals.front().size()];
    char max_char_count[signals.front().size()];
    for (string sig : signals) {
        for (int i=0; i < sig.size(); i++) {
            char c = sig[i];
            char mc = max_char_count[i];
            if (buckets[i].find(c) == buckets[i].end()) {
                buckets[i][c] = 0;
            } else {
                buckets[i][c]++;
            }
            if (buckets[i][c] > buckets[i][mc]) {
                max_char_count[i] = c;
            }
        }
    }

    for (char cc : max_char_count) {
        res += cc;
    }
    return res;
}

int main() {
    vector<string> data = read_file();
    string res = get_most_freq(data);
    cout << res << endl;
}