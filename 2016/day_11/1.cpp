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
#include <climits>

using namespace std;

// THIS CODE DOESN'T WORK READ THE EMOTIONALLY CHARGED README FOR AN EXPLANATION


int FLOOR_SIZE = 10;

vector<vector<int> > combo_int(int n, int k) {
    string b(k, 1); // k eligible slots
    b.resize(n, 0); // of size n
    vector<vector<int> > combo;
    do {
        vector<int> ele;
        for (int i = 0 ; i < n ; i++) {
            if (b[i]) ele.push_back(i) ;
        }
        combo.push_back(ele);
    } while(prev_permutation(b.begin(), b.end()));

    return combo;
}

vector<vector<int> > get_valid_indexes(vector<int> floor) {
    vector<vector<int> > index_combos = combo_int(FLOOR_SIZE, 2);
    vector<vector<int> > pick_ones = combo_int(FLOOR_SIZE, 1);
    index_combos.insert(index_combos.end(), pick_ones.begin(), pick_ones.end());
    
    vector<vector<int> > res;
    for (vector<int> c : index_combos) {
        bool valid = true;
        for (int ix : c) {
            if (!floor[ix]) valid = false;
        }
        if (valid){
            res.push_back(c);
        }
    }
    return res;
}

vector<vector<int> > make_map_with_given_indexes_and_floor(
    vector<vector<int> > m,
    int curr_floor,
    int dest_floor,
    vector<int> candidate_indexes
) {
    vector<vector<int> > new_map = m;
    for(int ix : candidate_indexes) {
        new_map[curr_floor][ix] = 0;
        new_map[dest_floor][ix] = 1;
    }
    return new_map;
}

bool validate_map(vector<vector<int>> m) {
    int half = FLOOR_SIZE/2;
    for (vector<int> floor : m) {
        vector<int> chips(floor.begin(), floor.begin() + half);
        vector<int> gens(floor.begin() + half, floor.end());
        
        for (int i = 0; i < half; i++) {
            if (chips[i] & !gens[i]) {
                    for (int j = 0 ; j < half; j++) {
                        if ((j != i) && gens[j]) {
                            return false;
                        }
                    }
            }
        }
    }
    return true;
}

vector<vector<int> > read_file() {
    string filename = "grouped_input.txt";
    vector<vector<int> > data;

    ifstream file(filename);
    if (!file) {
        cerr << "could not open file" << endl;
    }
    string line;
    while (getline(file, line)) {
        pair<vector<int>, vector<int> > ln;
        for(int i=0; i<FLOOR_SIZE/2; i++) {
            ln.first.push_back(line[i] - '0');
            ln.second.push_back(line[i+(FLOOR_SIZE/2)] - '0');
        }
        // patchy way to refactor our code
        ln.first.insert(ln.first.end(), ln.second.begin(), ln.second.end());
        data.push_back(ln.first);
    }
    
    return data;
}


string map_to_string(vector<vector<int> > m) {
    stringstream ss;
    
    for (vector<int> r : m) {
        for (int i : r) {
            ss << i;
        }
    }
    return ss.str();
}

vector<pair<vector<vector<int> >, int > > get_valid_map_states(
    vector<vector<int> > m, int floor
) {
    vector<pair<vector<vector<int> >, int > > res;
    vector<vector<int> > things_to_take_in_elevator = get_valid_indexes(m[floor]);
    for (vector<int> candidate_ix : things_to_take_in_elevator) {
        // Elevator can only move up or down one
        for (int f : {floor - 1, floor + 1}) {
            if (f != -1 and f != FLOOR_SIZE) {
                // We can move a thing to this floor
                // Create a new map with the moved things
                // Validate if this map is good or not according to problem constraints
                vector<vector<int> > candidate_map = make_map_with_given_indexes_and_floor(m, floor, f, candidate_ix);
                
                if (validate_map(candidate_map)) {
                    res.push_back(make_pair(candidate_map, f));
                }
            }
        }
    }
    
    return res;
}


int search_space(vector<vector<int> > space) {
    deque<tuple<vector<vector<int> >, int, int> > q; // map, current floor, number of steps
    string res = map_to_string({
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
    });
    // string res = "0000000000001111";
    int dist = INT_MAX;
    set<string> visited;
    q.push_back({space, 0, 0});
    while (!q.empty()) {
        tuple<vector<vector<int> >, int, int>  current = q.at(0);
        string as_string = map_to_string(get<0>(current));
        if (as_string == res) {
            cout << "dest" << endl;
            if (get<2>(current) < dist) {
                cout << "new dist" << get<2>(current) << endl;
                dist = get<2>(current);
                q.pop_front();
                continue;
            }
        }
        if (visited.count(as_string)) {
            q.pop_front();
            continue;
        }

        visited.insert(as_string);
        vector<pair<vector<vector<int> >, int > > next_maps = get_valid_map_states(
            get<0>(current),
            get<1>(current)
        );
        int next_dist = get<2>(current) + 1;
        q.pop_front();
        for (auto nm : next_maps) {
            q.push_back({nm.first, nm.second, next_dist});
        }
    }
    return dist;
}

int main() {
    auto data = read_file();
    // vector<vector <int> > example = {
    //     {1,1,0,0},
    //     {0,0,1,1},
    //     {0,0,0,0},
    //     {0,0,0,0}
    // };
    cout << "read data" << endl;
    cout << search_space(data) << endl;
    cout << "finished" << endl;
    return 0;
}