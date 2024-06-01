#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <utility>

using namespace std;

std::vector<std::vector<char> > read_file() {
    string filename = "input.txt";
    std::vector<std::vector<char> > data;

    std::ifstream file(filename);
    if (!file) {
        std::cerr<< "failed to open file" << std::endl;
    }

    string line;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::string element;
        while (iss >> element) {
            if (element.size() > 0) {
                std::vector<char> a(element.begin(), element.end());
                data.push_back(a);
            }
        }
    }
    file.close();

    return data;
}

pair<int, int> do_move(pair<int, int> start, char move) {
    switch(move) {
        case 'U':
            if (start.first == 0) {
                break;
            } else {
                start.first = start.first - 1;
                break;
            }
        case 'D':
            if (start.first == 2) {
                break;
            } else {
                start.first = start.first + 1;
                break;
            }
        case 'L':
            if (start.second == 0) {
                break;
            } else {
                start.second = start.second - 1;
                break;
            }
        case 'R':
            if (start.second == 2) {
                break;
            } else {
                start.second = start.second + 1;
            }
    }
    
    return start;
}

pair<int, int> process_line(vector<char> line, pair<int, int> start_coords) {
    pair<int, int> ending_coords = start_coords;

    for (char move : line) {
        ending_coords = do_move(ending_coords, move);
    }

    return ending_coords;
}

int main() {
    vector<vector<char> > instructions = read_file();

    int board[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    pair<int, int> coords = make_pair(1, 1);
    for (vector<char> line : instructions) {
        coords = process_line(line, coords);
        cout << board[coords.first][coords.second] << endl;
    }

    return 0;
}

// 53255