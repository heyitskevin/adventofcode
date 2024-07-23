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

#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/trim_all.hpp>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/join.hpp>

using namespace std;
using namespace boost;

deque<pair<unsigned long, unsigned long> > read_file() {
    string filename = "input.txt";
    deque<pair<unsigned long, unsigned long> > data;
    ifstream file(filename);
    if (!file) {
        cerr << "could not open" << endl;
    }
    string ln;
    deque<string> container;
    while (getline(file, ln)) {
        split(container, ln, is_any_of("-"));
        data.push_back(make_pair(
            stoul(container[0]), 
            stoul(container[1])
        ));
    }
    return data;
}

bool validate_ip(unsigned long ip, deque<pair<unsigned long, unsigned long> >& remaining) {
    for (auto b: remaining) {
        if ((b.first <= ip) && (ip <= b.second)) {
            return false;
        }
    }
    return true;
}

unsigned long count_allowed(deque<pair<unsigned long, unsigned long> > b) {
    bool valid_val = false;
    bool in_interval = false;
    unsigned long res = 0;
    int valid_numbers = 0;
    unsigned long max_ip = 4294967295;
    while(res <= max_ip) {
        while (!valid_val) {
            in_interval = false;
            for (int i = 0; i < b.size(); i++) {
                auto interval = b[i];
                if ((interval.first <= res) && (res <= interval.second)) {
                    res = interval.second + 1;
                    b.erase(b.begin() + i);
                    in_interval = true;
                    break;
                }
            }
            if (!in_interval) {
                valid_numbers++;
                res++;
                break;
            }
        }

        while(validate_ip(res, b) && res <= max_ip) {
            valid_numbers++;
            res++;
        }
    }
    
    return valid_numbers - 1; // One extra count of while loop
}

int main() {
    deque<pair<unsigned long, unsigned long> > blacklists = read_file();
    unsigned long ans = count_allowed(blacklists);
    cout << ans << endl;
    return 0;
}


