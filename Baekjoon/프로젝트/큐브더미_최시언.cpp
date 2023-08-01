#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#define MAX 7
#define FASTIO cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;
int N, M, X, Y, Z;
bool Cube[MAX][MAX][MAX];
int Answer;

void input() {
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        cin >> X >> Y >> Z;
        Cube[X][Y][Z] = true;
    }
}

void settings() {
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            for (int k = 1; k <= N; k++) {
                if (Cube[i][j][k]) {
                    if (Cube[i + 1][j][k] && Cube[i - 1][j][k] && Cube[i][j + 1][k] && Cube[i][j - 1][k] && Cube[i][j][k + 1] && Cube[i][j][k - 1]) {
                        Answer++;
                    }
                }
            }
        }
    }
}

void find_Answer() {
    cout << Answer << "\n";
}

int main() {
    FASTIO
    input();
    settings();
    find_Answer();

    return 0;
}
