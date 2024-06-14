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

void add_commands_to_map(vector<string> bot_commands,  map<int, pair<pair<string, string>, pair<int, int>>>& m) {
    for(string lowhigh : bot_commands) {
        int giver_bot = stoi(lowhigh.substr(4, 3));
        
        string low_string = "gives low to ";
        string high_string = "and high to ";
        int low = lowhigh.find(low_string);
        int high = lowhigh.find(high_string);
        
        string low_dest = lowhigh.substr(low + low_string.size(), high - low - low_string.size());
        string high_dest = lowhigh.substr(high + high_string.size(), lowhigh.size());
        trim(low_dest);
        trim(high_dest);
        
        m.emplace(giver_bot, make_pair(make_pair(low_dest, high_dest), make_pair(-1, -1)));
    }
}

void add_bot_givens_to_map(vector<string> givens, map<int, pair<pair<string, string>, pair<int, int>>>& m) {
    for(string g: givens) {
        string vstring = "value ";
        int val = stoi(g.substr(g.find(vstring) + vstring.size(), 2));
        string bstring = " goes to bot ";
        int b_dest = stoi(g.substr(g.find(bstring) + bstring.size(), 3));
        
        auto& bot_buckets = m[b_dest].second;
        if(bot_buckets.first == -1) {
            bot_buckets = make_pair(val, -1);
        } else if(bot_buckets.second == -1) {
            bot_buckets = make_pair(bot_buckets.first, val);
        } else {
            cerr << "Too many elements" << endl;
        }
    }
}

deque<int> get_all_full_bots(map<int, pair<pair<string, string>, pair<int, int>>>& m, set<int>& visited) {
    deque<int> d;
    for(auto iter = m.begin(); iter != m.end(); iter ++) {
        pair<int, int> bucket_data = iter->second.second;
        if ((bucket_data.first != -1 && bucket_data.second != -1) && (visited.count(iter->first) == 0)) {
            // cout << "b1: " << bucket_data.first << " b2: " << bucket_data.second << endl;
            d.push_back(iter->first);
        }
    }
    return d;
}

int slice_bot_string(string bot_string) {
    string sliced = bot_string.substr(bot_string.find(" "), bot_string.size());
    
    return stoi(sliced);
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

int get_bot(vector<string> bot_commands, vector<string> bot_givens) {
    // bot number -> (low_dest, high_dest), (v1, v2)
    map<int, pair<pair<string, string>, pair<int, int>>> bot_map;
    set<int> visited_bots;
    add_commands_to_map(bot_commands, bot_map);
    add_bot_givens_to_map(bot_givens, bot_map);
    deque<int> q;
    auto current_bot = get_all_full_bots(bot_map, visited_bots);
    q.insert(q.end(), current_bot.begin(), current_bot.end());
    
    while(!q.empty()) {
        int next_bot_id = q.front();
        if (visited_bots.count(next_bot_id) != 0 ){
            q.pop_front();
            continue;
        }
        visited_bots.emplace(next_bot_id);
        
        pair<pair<string, string>, pair<int, int>> bot_data = bot_map[next_bot_id];
        int next_low_bot_id = slice_bot_string(bot_data.first.first);
        int next_high_bot_id = slice_bot_string(bot_data.first.second);
        int low = bot_data.second.first;
        int high = bot_data.second.second;
        
        if (low > high) {
            int temp = high;
            high = low;
            low = temp;
        }

        if (low == 17 && high == 61) {
            return next_bot_id;
        }
        
        pair<int, int> low_pair = make_new_bot_pair(bot_map[next_low_bot_id].second, low);
        pair<int, int> high_pair = make_new_bot_pair(bot_map[next_high_bot_id].second, high);

        bot_map[next_low_bot_id].second = low_pair;
        bot_map[next_high_bot_id].second = high_pair;
        auto new_bots = get_all_full_bots(bot_map, visited_bots);
        q.insert(q.end(), new_bots.begin(), new_bots.end());
        q.pop_front();
    }

    return -1;
}

int main() {
    pair<vector<string>, vector<string> > data = read_file();
    int b = get_bot(data.first, data.second);
    cout << b << endl;
    return 0;
}