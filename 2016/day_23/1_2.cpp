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
    vector<string> container;
    while (getline(file, ln)) {
        data.push_back(ln);
    }
    return data;
}

int main() {
    int cursor = 0;
    // For part 2 set a to 12 and wait a LONG time, alternatively do it by hand
    map<string, unsigned long long> reg = {{"a", 7}, {"b", 0}, {"c", 0}, {"d", 0}};
    vector<string> instructions = read_file();
    string next_inst;
    vector<string> container;
    while (cursor < instructions.size()) {
        next_inst = instructions[cursor];
        split(container, next_inst, is_any_of(" "));
        if (container[0] == "cpy") {
            string x = container[1];
            int x_val;
            if (reg.find(x) != reg.end()) {
                x_val = reg[x];
            } else {
                x_val = stoi(x);
            }
            string y = container[2];
            if (reg.find(y) != reg.end()) { // Otherwise invalid command do nothing
                reg[y] = x_val;
            }
        } else if (container[0] == "inc") {
            if (reg.find(container[1]) != reg.end()) {
                reg[container[1]]++;
            }
        } else if (container[0] == "dec") {
            if(reg.find(container[1]) != reg.end()) {
                reg[container[1]]--;
            }

        } else if (container[0] == "jnz") {
            int jumper;
            if (reg.find(container[1]) != reg.end()) {
                jumper = reg[container[1]];
            } else {
                jumper = stoi(container[1]);
            }
            
            if (jumper != 0) {
                int jump_dist;
                if (reg.find(container[2]) != reg.end()) {
                    jump_dist = reg[container[2]];
                } else {
                    jump_dist = stoi(container[2]);
                }
                cursor += jump_dist;
                continue;
            } 
        } else if (container[0] == "tgl") {
            int dist;
            if (reg.find(container[1]) != reg.end()) {
                dist = reg[container[1]];
            } else {
                dist = stoi(container[1]);
            }
            if ((cursor + dist) < instructions.size()) {
                string instruction_to_toggle = instructions[cursor + dist];
                split(container, instruction_to_toggle, is_any_of(" "));
                
                string new_inst = "";
                if (container.size() == 2) {
                    if (container[0] == "inc") {
                        new_inst = "dec";
                    } else {
                        new_inst = "inc";
                    }
                    instructions[cursor + dist] = new_inst + " " + container[1];
                }
                if (container.size() == 3) {
                    if (container[0] == "jnz") {
                        new_inst = "cpy";
                    } else {
                        new_inst = "jnz";
                    }
                    instructions[cursor + dist] = new_inst + " " + container[1] + " " + container[2];
                }
            }
        }
        cursor++;
    }
    cout << "Solution: " << reg["a"] << endl;
    return 0;
}