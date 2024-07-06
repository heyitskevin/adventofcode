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

using namespace std;

bool is_wall(int x, int y) {
    int f = pow((x + y), 2)+ 3*x + y + 1350;
    return __builtin_popcount(f) % 2;
}

int bfs() {
    int steps = 0;
    int x = 1;
    int y = 1;
    
    set<pair<int, int>> visited;
    deque<tuple<int, int, int> > q; // x coord, y coord, steps so far
    q.push_back({x, y, steps});
    // BFS guarantees shortest path
    while(!q.empty()) {
        x = get<0>(q[0]);
        y = get<1>(q[0]);
        steps = get<2>(q[0]);
        // cout << "visit x: "<<x << " y: " << y << endl;
        q.pop_front();

        if (visited.count(make_pair(x,y))) continue;

        visited.emplace(make_pair(x, y));

        if (steps >= 50) continue;
        steps++;
        // for L, R ,U, D if not wall(x, y) or x, y < 0 add (x,y, steps) to q 
        for (pair<int, int> p : {make_pair(x+1, y), make_pair(x-1, y), make_pair(x, y+1), make_pair(x, y-1)}) {
            if(p.first >=0 and p.second >= 0 and !is_wall(p.first, p.second)) {
                q.push_back({p.first, p.second, steps});
            }
        }

    }
    
    return visited.size();
}

int main() {
    cout << bfs() << endl;
    return 0;
}