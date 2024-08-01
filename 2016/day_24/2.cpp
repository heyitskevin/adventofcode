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
#include <climits>

using namespace std;

typedef pair<int, int> Coords;

class Node {
    public:
    // cost variables
    int h;
    int g;
    int f;

    Coords pos; // ROW THEN COL
    
    Node *parent;

    bool operator== (const Node &node);

};

// Need to override equivalence operator to do compares on where we are in the grid
bool Node::operator== (const Node &node) {
    return (node.pos.first == this->pos.first && node.pos.second == this->pos.second);
}

bool node_in_list(Node n, vector<Node> l) {
    for (int i = 0; i < l.size(); i++) {
        if (n  == l[i]) {
            return true;
        }
    }
    return false;
}

vector<vector<char> > read_file() {
    string filename = "input.txt";
    vector<vector<char> > data;
    ifstream file(filename);
    if (!file) {
        cerr << "could not open" << endl;
    }
    string ln;
    while (getline(file, ln)) {
        vector<char> l;
        for (char c : ln) {
            l.push_back(c);
        }
        data.push_back(l);
    }
    return data;
}

map<char, Coords > get_locations(vector<vector<char> >& grid) {
    map<char, Coords > coords;
    for (int i = 0 ; i < grid.size(); i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            if (grid[i][j] != '#' && grid[i][j] != '.') {
                coords[grid[i][j]] = make_pair(i, j);
            }
        }
    }
    return coords;
}

int a_star_dist(vector<vector<char> >& grid, Coords& start, Coords& dest) {
    int i;
    int x;
    int y;
    int ix; // Used for iterating over list of available nodes open_list
    int curr_direction;

    Node start_node;
    Node curr_node;
    Node end_node;

    Node *new_node;

    vector<Node> open_list;
    vector<Node> closed_list;
    int directions[4][2] = {
        {-1, 0},
        {0, -1},
        {1, 0},
        {0, 1}
    };

   start_node.pos = start;
   end_node.pos = dest;

   start_node.g = 0;
   start_node.h = 0;
   start_node.f = 0;

   end_node.g = 0;
   end_node.h = 0;
   end_node.f = 0;

   start_node.parent = nullptr;
   end_node.parent = nullptr;

    open_list.push_back(start_node);

    while (!open_list.empty()) {
        ix = 0;
        curr_node = open_list[0];
        // Pick the node w/ the lowest F cost from available nodes
        for (i = 0 ; i < open_list.size(); i++) {
            if (open_list[i].f < curr_node.f) {
                ix = i;
                curr_node = open_list[i];
            }
        }
        // Remove the selected node from open list and add it to closed list
        open_list.erase(open_list.begin() + ix);
        closed_list.push_back(curr_node);
        // Look up, down, left, right
        for (curr_direction = 0; curr_direction< 4; curr_direction ++) {
            x = curr_node.pos.second + directions[curr_direction][1];
            y = curr_node.pos.first + directions[curr_direction][0];

            // Bounds and wall checks
            if (x < 0 || x > grid[0].size() - 1 || y < 0 || y > grid.size() - 1) {
                continue;
            } else if (grid[y][x] == '#') {
                continue;
            }

            new_node = new Node;
            new_node->pos.first = y;
            new_node->pos.second = x;

            if (node_in_list(*new_node, closed_list)) {
                // We have already visited this node.
                continue;
            } else if (!node_in_list(*new_node, open_list)) {
                // We consider this node if it isn't already being considered
                new_node->parent = &curr_node; // Link it up
                // Calculate f, g, h costs
                new_node->g = curr_node.g + 1; // In our case, we only move in cardinal directions so additional cost is just 1
                new_node->h = abs(new_node->pos.first - dest.first) + abs(new_node->pos.second + dest.second); // Manhattan distance to destination
                new_node->f = new_node->h + new_node->g;
                open_list.push_back(*new_node);
            } else {
                // We are already considering this node, check to see if our current path is better than our recorded path
                if (new_node->g < curr_node.g) {
                    new_node->parent = &curr_node;
                    new_node->g = curr_node.g + 1;
                    new_node->f = new_node->h + new_node->g;
                }
            }
        }
        for (Node n : closed_list) {
            if (n == end_node) {
                return n.g;
            }
        }
    }

    cout << "not found" << endl;
    return -1;
}

int find_fewest_steps(vector<vector<char> > grid) {
    map<char, Coords > nodes = get_locations(grid);
    // since our nodes are all numbers, we can just use a 2x2 adjacency matrix
    vector<vector<int> > adjacency_matrix;

    for (auto const& i: nodes) {
        vector<int> ln;
        for (auto const& j : nodes) {
            ln.push_back(-1);
        }
        adjacency_matrix.push_back(ln);
    }

    int n = adjacency_matrix.size();
    vector<bool> bits(n);

    // for each node in nodes, get a* distance to every other node
    for (int start = 0 ; start < n ; start++) {
        for (int dest = 0; dest < n; dest++) {
            if (start == dest) {
                adjacency_matrix[start][dest] = 0;
            } else {
                adjacency_matrix[start][dest] = a_star_dist(grid, nodes['0' + start], nodes['0' + dest]);
            }
        }
    }

    // We do the travelling salesman problem here
    // Compute all paths that end up at 0,
    vector<int> positions = { 1, 2, 3, 4, 5, 6, 7 };
    int min_dist = 10000000;
    int test_sum;
    int ix;
    
    while(next_permutation(positions.begin(), positions.end())) {
        test_sum = adjacency_matrix[0][positions[0]]; // reset after every iteration
        
        for (ix = 1 ;  ix < positions.size(); ix++) {
            test_sum += adjacency_matrix[positions[ix-1]][positions[ix]];
        }
        test_sum += adjacency_matrix[positions[6]][0]; // shorthand for last value in positions
        min_dist = min(min_dist, test_sum);
    }
    
    cout << "DONE" << endl;;
    return min_dist;
}

int main() {
    vector<vector<char> > grid = read_file();
    int r = find_fewest_steps(grid);
    cout << r << endl;
    return 0;
}