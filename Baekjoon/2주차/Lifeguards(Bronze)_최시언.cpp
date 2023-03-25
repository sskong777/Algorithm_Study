//여ㅕㅇ엉ㅇ거ㅓ가시헝요
//하나씩 빼보면서, 최댓값을 출력해면됨. max~

#include <iostream>
using namespace std;

int N, s[101], e[101], t[1001];

int main() {

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> s[i] >> e[i];
        for (int j = s[i]; j < e[i]; j++) t[j]++;
    }

    int ans = 0;
    for (int i = 0; i < N; i++) {
        for (int j = s[i]; j < e[i]; j++)
            t[j]--;

        int cnt = 0;
        for (int j = 0; j <= 1000; j++)
            if (t[j]) cnt++;
        ans = max(ans, cnt);

        for (int j = s[i]; j < e[i]; j++)
            t[j]++;
    }

    cout << ans << '\n';
    return 0;
}
