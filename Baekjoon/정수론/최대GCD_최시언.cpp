//입력될 숫자의 개수가 주어지고, 이만큼의 수에서 최대공약수를 구하면 되는 문제다.
//최대 공약수는 max값을 구한다음에 하나씩 낮춰가면서 나머지가 0인 값을 구하면 된다.
//최대공약수의 최대공약수는 결국 그 세수의 최대 공약수라고 할 수 있다!

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int gcd(int a, int b) {
    return !b ? a : gcd(b, a % b);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    int maxGcd = -1;
    int temp;
    string line;
    string num;
    vector<int> v;

    cin >> t;
    cin.ignore();

    while (t--) {
        v.clear();
        maxGcd = -1;

        getline(cin, line);
        stringstream sstream(line);
        while (getline(sstream, num, ' ')) // 문자열 분리
            v.push_back(stoi(num));

        for (int i = 0; i < v.size() - 1; ++i) { // 완전탐색
            for (int j = i + 1; j < v.size(); ++j) {
                temp = gcd(v[i], v[j]);
                maxGcd = maxGcd < temp ? temp : maxGcd;
            }
        }
        cout << maxGcd << '\n';
    }
}
