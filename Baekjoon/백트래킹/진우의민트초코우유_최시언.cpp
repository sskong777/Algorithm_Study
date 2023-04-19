#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
using pii = pair<int, int>;

vector<pii> vegetables;
pii start_location;
int field_size, initial_time, travel_range, max_vegetables_collected;
bool visited[12];

int distance(pii a, pii b) { return abs(a.first - b.first) + abs(a.second - b.second); }

void collect_vegetables(pii current_location, int remaining_time, int vegetables_collected) {
if (remaining_time >= distance(current_location, start_location)) {
max_vegetables_collected = max(max_vegetables_collected, vegetables_collected);
}
for (int i = 0; i < vegetables.size(); i++) {
if (!visited[i]) {
visited[i] = true;
if (remaining_time - distance(current_location, vegetables[i]) >= 0) {
collect_vegetables(vegetables[i], remaining_time - distance(current_location, vegetables[i]) + travel_range, vegetables_collected + 1);
}
visited[i] = false;
}
}
}

int main() {
scanf("%d %d %d", &field_size, &initial_time, &travel_range);
for (int i = 0; i < field_size; i++) {
for (int j = 0; j < field_size; j++) {
int input; scanf("%d", &input);
if (input == 1) start_location = {i, j};
else if (input == 2) vegetables.push_back({i, j});
}
}
collect_vegetables(start_location, initial_time, 0);
printf("%d", max_vegetables_collected);
}
