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
    char board[5][5] = {
        {'0', '0', '1', '0', '0'},
        {'0', '2', '3', '4', '0'},
        {'5', '6', '7', '8', '9'},
        {'0', 'A', 'B', 'C', '0'},
        {'0', '0', 'D', '0', '0'}
    };

    switch(move) {
        case 'U':
            if (start.first == 0) {
                break;
            } else if (board[start.first-1][start.second] == '0') {
                break;
            } else {
                start.first = start.first - 1;
                break;
            }
        case 'D':
            if (start.first == 4) {
                break;
            } else if (board[start.first+1][start.second] == '0') {
                break;
            } else {
                start.first = start.first + 1;
                break;
            }
        case 'L':
            if (start.second == 0) {
                break;
            } else if(board[start.first][start.second-1] == '0') {
                break;
            } else {
                start.second = start.second - 1;
                break;
            }
        case 'R':
            if (start.second == 4) {
                break;
            } else if (board[start.first][start.second+1] == '0') { 
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
    
    char board[5][5] = { // Double Instantiation, don't know enough about global vars to give a damn about fixing this
        {'0', '0', '1', '0', '0'},
        {'0', '2', '3', '4', '0'},
        {'5', '6', '7', '8', '9'},
        {'0', 'A', 'B', 'C', '0'},
        {'0', '0', 'D', '0', '0'}
    };

    pair<int, int> coords = make_pair(2, 0);
    
    for (vector<char> line : instructions) {
        coords = process_line(line, coords);
        cout << board[coords.first][coords.second] << ' ';
    }

    return 0;
}