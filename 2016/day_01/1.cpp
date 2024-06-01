#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <cmath>

using namespace std;

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


int taxicab_blocks_away(std::vector<std::string> raw_directions) {
    int current_direction = 0;
    
    int x_coord = 0;
    int y_coord = 0;

    int directions[4] = {1, 1, -1, -1};
    
    for (string element : raw_directions) {
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
            y_coord = y_coord + (steps_to_take * directions[current_direction]);
        } else {
            x_coord = x_coord + (steps_to_take * directions[current_direction]);
        }

    }
    return abs(x_coord) + abs(y_coord);
}

int main() {
    std::vector<std::string> dirs = read_file();
    
    int soln;
    soln = taxicab_blocks_away(dirs);

    cout << soln << endl;

    return 0;
}