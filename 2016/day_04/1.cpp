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

int validate(string test_string) {
    vector<string> container;
    split(container, test_string, is_any_of("-"));

    string last = container.back();
    string checksum = last.substr(last.find("[")+1);
    int sector = stoi(last.substr(0, last.find("[")));

    checksum.pop_back();
    container.pop_back();

    string together = boost::join(container, "");
    auto charMap = std::map<char, int>();
    
    for (char c : together) {
        charMap[c]++;
    }
    vector<std::pair<char, int> > sortedChars;
    for (std::pair<char, int> cm : charMap) {
        sortedChars.push_back(cm);
    }

    std::sort(
        sortedChars.begin(),
        sortedChars.end(),
        [](pair<char, int> a, pair<char, int> b) {
            if (a.second == b.second) {
                return a.first < b.first; 
            }
            return a.second > b.second; 
        }
    );

    for (int i=0; i<checksum.size(); i++) {
        if(checksum[i] != sortedChars[i].first) {
            return 0;
        }
    }
    return sector;
}

int main() {
    vector<string> d = read_file();
    int sum = 0;
    for (string s : d) {
        auto a = validate(s);
        sum += a;
    }
    cout << sum << endl;
}