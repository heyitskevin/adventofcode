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
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/split.hpp>

using namespace std;
using namespace boost;


pair<vector<string>, vector<string> > read_file() {
    string filename = "input.txt";
    pair<vector<string>, vector<string> > data;

    ifstream file(filename);
    if (!file) {
        cerr << "could not open file" << endl;
    }
    string line;
    while (getline(file, line)) {
        if(line.find("gives low") != string::npos) {
            data.first.push_back(line);
        } else {
            data.second.push_back(line);
        }
    }
    
    return data;
}

pair<int, int> make_new_bot_pair(pair<int, int> in_pair, int candidate) {
    if (in_pair.first == -1) {
        return make_pair(candidate, -1);
    } else if (in_pair.second == -1) {
        return make_pair(in_pair.first, candidate);
    } else {
        return in_pair;
    }
}

void populate_map(
    map<string, pair<int, int>>& m, 
    vector<string> direction_rules, 
    vector<string> start_configs,
    map<string, pair<string, string>>& d
) {
    string first_split = " gives low to ";
    string second_split = " and high to ";
    for (string instruction : direction_rules) {
        int first_ix = instruction.find(first_split);
        int second_ix = instruction.find(second_split);

        string b1 = instruction.substr(0, first_ix);
        string b2 = instruction.substr(first_ix + first_split.size(), second_ix - first_ix - first_split.size());
        string b3 = instruction.substr(second_ix + second_split.size(), instruction.size());

        trim(b1);
        trim(b2);
        trim(b3);

        m.emplace(b1, make_pair(-1, -1));
        m.emplace(b2, make_pair(-1, -1));
        m.emplace(b3, make_pair(-1, -1));

        d.emplace(b1, make_pair(b2, b3));
    }

    string v_split = " goes to ";
    for (string s : start_configs) {
        int v_ix = s.find(v_split);
        
        int val = stoi(s.substr(6, 4));
        string k_bot = s.substr(v_ix + v_split.size(), s.size());
        trim(k_bot);
        pair<int, int> new_pair = make_new_bot_pair(m[k_bot], val);
        m[k_bot] = new_pair;
    }
}

void do_cascade(map<string, pair<int, int>>& m, map<string, pair<string, string>>& d) {
    deque<string> q;
    set<string> visited;
    // Just hard code bot 17 as first bot b/c we know it starts there
    q.push_back("bot 17");
    while(!q.empty()) {
        string current_bot_name = q.front();
        
        if (visited.count(current_bot_name) != 0) {
            q.pop_front();
            continue;
        }
        visited.emplace(current_bot_name);
        pair<int, int> current_bot_data = m[current_bot_name];
        pair<string, string> lowhigh = d[current_bot_name];
        // Hot swap our ints
        int low = current_bot_data.first;
        int high = current_bot_data.second;
        if (low > high) {
            int temp = high;
            high = low;
            low = temp;
        }

        m[lowhigh.first] = make_new_bot_pair(m[lowhigh.first], low);
        m[lowhigh.second] = make_new_bot_pair(m[lowhigh.second], high);
        
        
        for (auto it = m.begin(); it != m.end(); it++) {
            
            auto data = it->second;
            if (data.first != -1 && data.second != -1) {
                q.push_back(it->first);
            }
        }
        q.pop_front();
    }
}

int main() {
    pair<vector<string>, vector<string>> data = read_file();
    map<string, pair<int, int>> m;
    map<string, pair<string, string>> directions;
    populate_map(m, data.first, data.second, directions);
    do_cascade(m, directions);
    
    int zero = m["output 0"].first;
    int one = m["output 1"].first;
    int two = m["output 2"].first;

    cout << zero * one * two << endl;
}