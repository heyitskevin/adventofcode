#include <vector>
#include <string>
#include <utility>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <boost/algorithm/string.hpp>
#include <boost/algorithm/string/split.hpp>

using namespace std;
using namespace boost;

vector<string> read_file() {
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

vector<char> rotate_oneD_array(vector<char> arr, int rot) {
    int size = arr.size();
    
    vector<char> result(size);
    for (int ix=0; ix < size; ix++) {
        result[(ix + rot) % size] = arr[ix];
    }
    return result;
}

void draw_rect(vector<vector<char> >& sc, int width, int height) {
    for (int h=0; h < height; h++) {
        for (int w=0; w < width; w++) {
            sc[h][w] = '*';
        }
    }
}

void rotate_row_col(vector<vector<char> >& sc, int ix, int rotate_by, bool is_row) {
    if (is_row) {
        vector<char> new_arr = rotate_oneD_array(sc[ix], rotate_by);
        sc[ix] = new_arr;
    } else {
        vector<char> new_input;
        for (vector<char> row : sc) {
            new_input.push_back(row[ix]);
        }
        vector<char> new_arr = rotate_oneD_array(new_input, rotate_by);
        for (int x=0; x < new_arr.size(); x++) {
            sc[x][ix] = new_arr[x];
        }
    }
}

void do_cmd(vector<vector<char> >& sc, string cmd){
    vector<string> split_container; 
    boost::split(split_container, cmd, is_any_of(" "));
    if (split_container[0] == "rect") {
        vector<string> coords_container;
        boost::split(coords_container, split_container[1], is_any_of("x"));
        draw_rect(sc, stoi(coords_container[0]), stoi(coords_container[1]));
    } else if (split_container[0] == "rotate") {
        bool is_row = true;
        if (cmd.find("column") != string::npos) {
            is_row = false;
        }
        vector<string> rotation_cmds;
        boost::split(rotation_cmds, cmd, is_any_of("="));
        int ix = stoi(rotation_cmds[1].substr(0, rotation_cmds[1].find(" by ")));
        
        int rotate_by = stoi(rotation_cmds[1].substr(rotation_cmds[1].find(" by ") + 3, rotation_cmds[1].size()));
        
        rotate_row_col(
            sc,
            ix,
            rotate_by,
            is_row
        );
    }
}

int count_pixels(vector<vector<char> >& sc) {
    int res = 0;
    for (vector<char> r : sc) {
        for (char c : r) {
            if (c == '*') {
                res++;
            }
        }
    }
    return res;
}

void print_screen(vector<vector<char> >& sc) {
    for (vector<char> r : sc) {
        for (char c : r) {
            cout << c << ' ';
        }
        cout << endl;
    }
}

int main() {
    vector<string> cmds = read_file();
    vector<vector<char> > screen(6, vector<char>(50, '.'));
    for (string c: cmds) {
        do_cmd(screen, c);
    }
    int soln = count_pixels(screen);
    print_screen(screen);
    cout << soln << endl;
    return 0;
}