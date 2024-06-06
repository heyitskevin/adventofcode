#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <utility>
#include <functional>
#include <algorithm>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/trim_all.hpp>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/join.hpp>
#include <map>

using namespace std;
using namespace boost;


std::vector<string> read_file() {
    string filename = "input.txt";
    std::vector<string> data;

    std::ifstream file(filename);
    if (!file) {
        std::cerr<< "failed to open file" << std::endl;
    }

    string line;

    while (std::getline(file, line)) {
        trim_all(line);
        data.push_back(line);
    }
    file.close();

    return data;
}

void decrypt(string encrypted) {
    vector<string> container;
    split(container, encrypted, is_any_of("-"));

    string last = container.back();
    string checksum = last.substr(last.find("[")+1);
    int sector = stoi(last.substr(0, last.find("[")));

    checksum.pop_back();
    container.pop_back();
    int a = 'a';
    int z = 'z';

    string together = boost::join(container, " ");
    vector<string> decrypted;
    int shift = sector % 26;
    for (char c : together) {
        if (c != ' ') {
            int as_int = c;
            int shifted = shift + as_int;
            if (shifted > z) {
                shifted = (shifted - z) + a - 1;
            }
            char dec = shifted;
            string ds = string(1, dec);
            decrypted.push_back(ds);
        } else {
            decrypted.push_back(" ");
        }
    }
    string res = boost::join(decrypted, "");
    if (res.find("north") != string::npos) {
        cout << res << " " << sector << endl;
    }
    
}

int main() {
    vector<string> d = read_file();
    for (string s : d) {
        decrypt(s);
    }
}