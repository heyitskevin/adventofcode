#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <utility>
#include <boost/algorithm/string/trim_all.hpp>

using namespace std;
using namespace boost;


std::vector<std::vector<int> > read_file() {
    string filename = "input.txt";
    std::vector<std::vector<int> > data;

    std::ifstream file(filename);
    if (!file) {
        std::cerr<< "failed to open file" << std::endl;
    }

    string line;

    while (std::getline(file, line)) {
        trim_all(line);
        std::istringstream iss(line);
        std::string element;
        vector<int> vec;
        while (iss >> element) {
            if (element.size() > 0) {
                int number = stoi(element);
                vec.push_back(number);
            }

        }
        data.push_back(vec);
    }
    file.close();

    return data;
}


bool is_triangle(vector<int> sides) {
    // Rely on faith that each line has 3 sides b/c input is friendly
    int s1 = sides[0];
    int s2 = sides[1];
    int s3 = sides[2];

    if (
        s1 + s2 > s3 && s2 + s3 > s1 && s3 + s1 > s2 
    ) {
        return true;
    } else {
        return false;
    }
}

int main() {
    vector<vector<int> > data = read_file();
    int count = 0;
    vector<vector<int> > transpose(3, vector<int>(data.size()));
    for (int i=0; i < data.size(); i++) {
        for (int j=0; j < data[i].size(); j++) {
            transpose[j][i] = data[i][j];
        }
    }
    for (vector<int> row : transpose) {
        for (int i=0; i <= row.size() - 3; i+=3) {
            vector<int> proxy_triangle;
            for (int j=i; j<i+3; j++) {
                proxy_triangle.push_back(row[j]);
            }
            if (is_triangle(proxy_triangle)) {
                count++;
            }
        }
    }
    cout << count << endl;
}
