#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> li(n, 0);
    for (int i = 0; i < m; i++) {
        int num;
        cin >> num;
        li[num] = 1;
    }

    vector<int> temp(n, 0);
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < n; j++) {
            if (li[j] == 1) {
                temp[(j - 1 + n) % n] = (temp[(j - 1 + n) % n] + 1) % 2;
                temp[(j + 1) % n] = (temp[(j + 1) % n] + 1) % 2;
            }
        }
        li = temp;
        temp = vector<int>(n, 0);
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (li[i] == 1) {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
