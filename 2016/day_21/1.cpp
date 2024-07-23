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

vector<string> read_file() {
    string filename = "input.txt";
    vector<string> data;
    ifstream file(filename);
    if (!file) {
        cerr << "could not open" << endl;
    }
    string ln;
    while (getline(file, ln)) {
        data.push_back(ln);
    }
    return data;
}

void swap_pos(string& s, int pos1, int pos2) {
    swap(s[pos1], s[pos2]);
}

void swap_letter(string& s, char c1, char c2) {
    int ix1 = s.find(c1);
    int ix2 = s.find(c2);

    swap(s[ix1], s[ix2]);
}

void rotate_left(string& s, int steps) {
    rotate(s.begin(), s.begin() + steps, s.end());
}

void rotate_right(string& s, int steps) {
    rotate(s.rbegin(), s.rbegin() + steps, s.rend());
}

void rotate_on_character(string& s, char c) {
    int ixc = s.find(c);
    int steps = 1;
    if (ixc >= 4) {
        steps = 2;
    }
    rotate(s.rbegin(), s.rbegin() + (ixc + steps)%s.size(), s.rend());
}

void reverse_through(string& s, int x, int y) {
    if (y == s.size() - 1) {
        reverse(s.begin() + x, s.end());
    } else {
        reverse(s.begin() + x, s.begin() + y + 1);
    }
}

void move_position(string& s, int x, int y) {
    char c = s[x];
    s.erase(s.begin() + x);
    s.insert(y, 1, c);
}

void manage_instruction(string inst, string& s) {
    vector<string> container;
    split(container, inst, is_any_of(" "));
    
    if (inst.find("swap position") != string::npos) {
        int x = stoi(container[2]);
        int y = stoi(container[container.size() - 1]);
        swap_pos(s, x, y);
    } else if (inst.find("swap letter") != string::npos) {
        char x = container[2][0];
        char y = container[container.size() - 1][0];
        swap_letter(s, x, y);
    } else if (inst.find("rotate left") != string::npos) {
        int steps = stoi(container[container.size() - 2]);
        rotate_left(s, steps);
    } else if (inst.find("rotate right") != string::npos) {
        int steps = stoi(container[container.size() - 2]);
        rotate_right(s, steps);
    } else if (inst.find("rotate based on position") != string::npos) {
        rotate_on_character(s, container[container.size() - 1][0]);
    } else if (inst.find("reverse positions") != string::npos) {
        int px = stoi(container[2]);
        int py = stoi(container[container.size() - 1]);

        reverse_through(s, px, py);
    } else if (inst.find("move position") != string::npos) {
        int px = stoi(container[2]);
        int py = stoi(container[container.size() - 1]);

        move_position(s, px, py);
    }
}

int main() {
    string s = "abcdefgh";
    vector<string> i = read_file();

    for (string ist : i) {
        manage_instruction(ist, s);
    }

    cout << s << endl;
    return 0;
}