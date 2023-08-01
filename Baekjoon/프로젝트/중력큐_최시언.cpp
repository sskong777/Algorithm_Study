#include <cstdio>
#include <deque>
#include <vector>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    deque<int> queue;
    int state = 0;
    int b = 0;
    int w = 0;
    vector<int> result;

    for (int i = 0; i < n; i++) {
        char cmd[10], opt[10];
        scanf("%s %s", cmd, opt);

        if (cmd[0] == 'p' && cmd[1] == 'o' && cmd[2] == 'p') {
            if (!queue.empty()) {
                int e = queue.front();
                queue.pop_front();
                if (e == 0) {
                    b--;
                } else if (e == 1) {
                    w--;
                }
            }
        } else {
            if (cmd[0] == 'p' && cmd[1] == 'u' && cmd[2] == 's' && cmd[3] == 'h') {
                if (opt[0] == 'b') {
                    queue.push_back(0);
                    b++;
                } else if (opt[0] == 'w') {
                    queue.push_back(1);
                    w++;
                }
            } else if (cmd[0] == 'r' && cmd[1] == 'o' && cmd[2] == 't' && cmd[3] == 'a' && cmd[4] == 't' && cmd[5] == 'e') {
                if (opt[0] == 'l') {
                    state--;
                } else if (opt[0] == 'r') {
                    state++;
                }
                if (state == 4) {
                    state = 0;
                } else if (state == -1) {
                    state = 3;
                }
            } else if (cmd[0] == 'c' && cmd[1] == 'o' && cmd[2] == 'u' && cmd[3] == 'n' && cmd[4] == 't') {
                if (opt[0] == 'b') {
                    result.push_back(b);
                } else if (opt[0] == 'w') {
                    result.push_back(w);
                }
            }

            if (state % 2 == 1) {
                while (!queue.empty() && (queue[(state == 1 ? 0 : queue.size() - 1)]) != 1) {
                    if (state == 1) {
                        queue.pop_front();
                    } else {
                        queue.pop_back();
                    }
                    b--;
                }
            }
        }
    }

    for (int i : result) {
        printf("%d\n", i);
    }

    return 0;
}
