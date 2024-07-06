/*
Since this problem is trivialized by naive evaluation 
we opt to implement a general solution in C++ to expand our skills
*/

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


int main() {
    vector<string> inst_set = read_file();
    int instruction = 0;
    // Initialize registers to store separate memory locations
    int * a = new int(0);
    int * b = new int(0);
    int * c = new int(1);
    int * d = new int(0);
    map<string, int*> lookup;
    lookup["a"] = a;
    lookup["b"] = b;
    lookup["c"] = c;
    lookup["d"] = d;
    // b/c instructions are nicely formed, we can skip a bunch of guardrailing
    while (instruction < inst_set.size()) {
        vector<string> container;
        string curr_inst = inst_set[instruction];
        
        split(container, curr_inst, is_any_of(" "));
        string prefix = container[0];
        
        if (prefix == "cpy") {
            string src = container[1];
            string dest = container[2]; // This is always a register
            int i_s = 0;
            int* i_d = lookup[dest];
            if (lookup.find(src) != lookup.end()) {
                i_s = *lookup[src];
            } else {
                i_s = stoi(src);
            }
            *i_d = i_s;
        } else if (prefix == "inc")
        {
            string reg = container[1];
            (*lookup[reg])++;

        } else if (prefix == "dec")
        {
            string reg = container[1];
            (*lookup[reg])--;
        } else if (prefix == "jnz")
        {
            string comp = container[1];
            int offset = stoi(container[2]);
            int i_c = 0;
            if (lookup.find(comp) != lookup.end()) {
                i_c = *lookup[comp];
            } else {
                i_c = stoi(comp);
            }
            if (i_c > 0) {
                instruction = instruction + offset;
                continue;
            }
        }
        instruction ++;
    }
    cout << "a: " << *a << endl;
    return 0;
}