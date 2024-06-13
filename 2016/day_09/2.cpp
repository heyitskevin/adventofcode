#include <vector>
#include <string>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <regex>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/split.hpp>

using namespace std;
using namespace boost;

vector<string> read_file() { // read a oneliner as vector b/c lazy copy/paste
    string filename = "input.txt";
    vector<string> data;

    ifstream file(filename);
    if (!file) {
        cerr << "could not open file" << endl;
    }
    string line;
    while (getline(file, line)) {
        data.push_back(line);
    }
    return data;
}

unsigned long long int get_true_length(string s) {
    unsigned long long int count = 0;
    smatch m; // match_object
    regex r("\\(\\d+x\\d+\\)");
    
    while(regex_search(s, m, r)) {
        int first_ix = m.position();
        count += first_ix;

        string multiplier = s.substr(first_ix + 1, m.length() - 1); // Trim the parentheses
        int x_pos= multiplier.find('x');
        int subsequent_chars = stoi(multiplier.substr(0,x_pos));
        unsigned int iters = stoi(multiplier.substr(x_pos+1, multiplier.size()));
        
        string chunk = s.substr(first_ix + m.length(), subsequent_chars);
        
        unsigned long long int chunk_size = get_true_length(chunk);
        count += (chunk_size * iters); // No need to guard against subsequent chars being longer than end of string b/c nicely formed input
        int new_start = first_ix + m.length() + subsequent_chars;
        s = s.substr(new_start, s.size());
    }
    if (count == 0 && s.size() > 0 && m.empty()) {
        count = s.size();
    }
    return count;
}

int main() {
    vector<string> data = read_file();
    string d = data.front(); 
    
    unsigned long long int ct = get_true_length(d);
    cout << "done" << endl;
    cout<< ct << endl;
    return ct;
}