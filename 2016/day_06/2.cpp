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

string get_least_freq(vector<string> signals) {
    string res = "";
    // assume the size of each row is the same so just look at the first element
    map<char, int> buckets[signals.front().size()];
    char min_char_count[signals.front().size()];

    for (string sig : signals) {
        for (int i=0; i < sig.size(); i++) {
            char c = sig[i];
            if (buckets[i].find(c) == buckets[i].end()) {
                buckets[i][c] = 1;
            } else {
                buckets[i][c]++;
            }
        }
    }
    // I don't know how to gracefully do this in one loop so loop twice
    for (map<char, int> b : buckets) {
        char candidate;
        int min_count = signals.size() + 1;
        for (auto const& [key, val] : b) {
            if (min_count > val) {
                min_count = val;
                candidate = key;
            }
        }
        res += candidate;
    }

    return res;
}

int main() {
    vector<string> data = read_file();
    string res = get_least_freq(data);
    cout << res << endl;
}