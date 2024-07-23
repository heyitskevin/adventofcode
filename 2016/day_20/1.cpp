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

unsigned long get_min_val(deque<pair<unsigned long, unsigned long> > b) {
    bool valid_val = false;
    bool in_interval = false;
    unsigned long res = 0;

    /* 
        start with min value 
        if min value is in any interval, update min value to be max of that interval +1
        remove that interval from the scope
        do this again until we find a value that isn't in any interval
    */
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
            valid_val = true;
        }
    }

    return res;
}

int main() {
    deque<pair<unsigned long, unsigned long> > blacklists = read_file();
    unsigned long ans = get_min_val(blacklists);
    cout << ans << endl;
    return 0;
}


