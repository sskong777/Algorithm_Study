#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    map<string, int> pokemon;
    vector<string> names;

    for (int i = 1; i <= n; i++) {
        string temp;
        cin >> temp;
        pokemon[temp] = i;
        names.push_back(temp);
    }

    vector<string> result;
    for (int i = 0; i < m; i++) {
        string temp;
        cin >> temp;

        if (isupper(temp[0])) {
            result.push_back(to_string(pokemon[temp]));
        } else {
            int index = stoi(temp) - 1;
            result.push_back(names[index]);
        }
    }

    for (const auto& res : result) {
        cout << res << '\n';
    }

    return 0;
}
