#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <cmath>
#include <unordered_set>
#include <utility>

using namespace std;

struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};


std::vector<std::string> read_file() {
    std::string filename = "input.txt";
    std::vector<std::string> data;

    std::ifstream file(filename);
    if (!file) {
        std::cerr << "failed to open file" << std::endl;
    }

    std::string line;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::string w;
        while (iss >> w) {
            string subs = w;
            if (w.find(',') != std::string::npos) {
                subs = w.substr(0, w.size() - 1);
            }
            if (subs.size() > 0) {
                data.push_back(subs);
            }
        }
    }

    file.close();

    return data;
}

int first_revisit(vector<string> directions) {
    int current_direction = 0;
    
    int x_coord = 0;
    int y_coord = 0;

    pair<int, int> first = make_pair(x_coord, y_coord);
    std::unordered_set<std::pair<int, int>, pair_hash> visited;
    visited.insert(first);

    int cardinal[4] = {1, 1, -1, -1};

    for (string element : directions) {
        char turn = element[0];
        string steps = element.substr(1);
        int steps_to_take = std::stoi(steps);
        if (turn == 'L') {
            current_direction--;
        } else {
            // Default to R
            current_direction++;
        }
        current_direction = (4 + (current_direction % 4)) % 4;
        
        if (current_direction == 0 || current_direction == 2) {
            for (int i=1; i <= steps_to_take; i++) {
                int y_step = y_coord + i * cardinal[current_direction];
                pair<int, int> a_step = make_pair(x_coord, y_step);
                if (visited.count(a_step) > 0){
                    return abs(x_coord) + abs(y_step);
                } else {
                    visited.insert(a_step);
                }
            }
            // We are lazy about updating this code to be optimal b/c we are reusing code from part 1
            y_coord = y_coord + (steps_to_take * cardinal[current_direction]);
        } else {
            for (int i=1; i <= steps_to_take; i++) {
                int x_step = x_coord + i * cardinal[current_direction];
                pair<int, int> a_step = make_pair(x_step, y_coord);
                if (visited.count(a_step) > 0){
                    return abs(x_step) + abs(y_coord);
                } else {
                    visited.insert(a_step);
                }
            }
            x_coord = x_coord + (steps_to_take * cardinal[current_direction]);
        }
        
    }
    cout << "Double coordinate not found" << endl;
    return -1;
}

int main() {
    std::vector<std::string> dirs = read_file();
    
    int soln;
    soln = first_revisit(dirs);

    cout << soln << endl;

    return 0;
} // 133