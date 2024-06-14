#include <vector>
#include <string>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <regex>
#include <map>
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

deque<int> get_all_full_bots(map<int, pair<pair<string, string>, pair<int, int>>>& m) {
    deque<int> d;
    for(auto iter = m.begin(); iter != m.end(); iter ++) {
        pair<int, int> bucket_data = iter->second.second;
        if (bucket_data.first != -1 && bucket_data.second != -1) {
            // cout << "b1: " << bucket_data.first << " b2: " << bucket_data.second << endl;
            d.push_back(iter->first);
        }
    }
    return d;
}


int get_bot(vector<string> bot_commands, vector<string> bot_givens) {
    // bot number -> (low_dest, high_dest), (v1, v2)
    map<int, pair<pair<string, string>, pair<int, int>>> bot_map;
    
    add_commands_to_map(bot_commands, bot_map);
    add_bot_givens_to_map(bot_givens, bot_map);
    deque<int> q;
    auto current_bot = get_all_full_bots(bot_map);
    q.insert(q.end(), current_bot.begin(), current_bot.end());
    while(!q.empty()) {
        int next_bot_id = q.front();
        cout << "id " << next_bot_id << endl;
        pair<int, int> next_bot_data = bot_map[next_bot_id].second;
                
        if ((next_bot_data.first == 61 && next_bot_data.second == 17) || (next_bot_data.first == 17 && next_bot_data.second == 61)) {
            return next_bot_id;
        }
        // Update the map
        int next_low_bot = -1;
        int next_high_bot = -1;
        int next_low_val = -1;
        int next_high_val = -1;
        if (next_bot_data.first == -1 && next_bot_data.second == -1) {
            cerr << "INCORRECT BOT ADDED" << endl;
        }
        // Just ignore "output" for now
        if (next_bot_data.first < next_bot_data.second) {
            if (bot_map[next_bot_id].first.first.find("output") == string::npos) {
                next_low_bot = stoi(bot_map[next_bot_id].first.first.substr(4, 3));
                next_low_val = next_bot_data.first;
            }
            if (bot_map[next_bot_id].first.second.find("output") == string::npos) {
                next_high_bot = stoi(bot_map[next_bot_id].first.second.substr(4, 3));
                next_high_val = next_bot_data.second;
            }
        } else {
            if (bot_map[next_bot_id].first.second.find("output") == string::npos) {
                next_low_bot = stoi(bot_map[next_bot_id].first.second.substr(4, 3));
                next_low_val = next_bot_data.second;
            }
            if (bot_map[next_bot_id].first.first.find("output") == string::npos) {
                next_high_bot = stoi(bot_map[next_bot_id].first.first.substr(4, 3));
                next_high_val = next_bot_data.first;
            }
        }
        if (next_low_bot != -1) {
            auto& low_bot = bot_map[next_low_bot];
            auto& bot_buckets = low_bot.second;
            cout << "low bck " << bot_buckets.first << " " << bot_buckets.second << endl;
            if(bot_buckets.first == -1) {
                bot_buckets = make_pair(next_low_val, -1);
            } else if(bot_buckets.second == -1) {
                bot_buckets = make_pair(bot_buckets.first, next_low_val);
            } else {
                cerr << "Too many elements" << endl;
            }
        }
        if (next_high_bot != -1) {
            auto& high_bot = bot_map[next_high_bot];
            auto& bot_buckets = high_bot.second;
            if(bot_buckets.first == -1) {
                bot_buckets = make_pair(next_high_val, -1);
            } else if(bot_buckets.second == -1) {
                bot_buckets = make_pair(bot_buckets.first, next_high_val);
            } else {
                cerr << "Too many elements" << endl;
            }
        }
        cout << "----" << endl;
        if (next_bot_data.first != -1 && next_bot_data.second != -1) {
            // We have evaluated a full bot
            bot_map[next_bot_id].second =  make_pair(-1, -1);
        }

        auto new_bots = get_all_full_bots(bot_map);
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