//결국은 유미가 전부 왔다리 갔다리 하는걸 다 계산해야된다.
//유미가 모든 people에게 이동해야한다. 최솟값을 구해라.

#include <iostream>
#include <stdlib.h> //abs함수를 위해 사용

int meow_walk(int first);
int people_walk(int first, int second);

using namespace std;

int people[2][3];
int cat[2];

int main(void) {
	//입력
	int ans = 0;
	cin >> cat[0];
	cin >> cat[1];

	for (int i = 0; i < 3; i++) {
		cin >> people[0][i];
		cin >> people[1][i];
	}

	meow_walk(1);
	//모든 경우의 수 6가지를 계산.
	//123,132,213,231,312,321

	ans = min((meow_walk(0) + people_walk(0, 1) + people_walk(1, 2)), meow_walk(0) + people_walk(0, 2) + people_walk(2, 1));
	ans = min(ans, meow_walk(1) + people_walk(1, 2) + people_walk(2, 0));
	ans = min(ans, meow_walk(1) + people_walk(1, 0) + people_walk(0, 2));
	ans = min(ans, meow_walk(2) + people_walk(2, 0) + people_walk(0, 1));
	ans = min(ans, meow_walk(2) + people_walk(2, 1) + people_walk(1, 0));

	cout << ans;

}

int meow_walk(int first) {
	int ans = abs(people[0][first] - cat[0]) + abs(people[1][first] - cat[1]); //이동거리
	return ans;
}

int people_walk(int first, int second) {
	int ans = abs(people[0][first] - people[0][second]) + abs(people[1][first] - people[1][second]); //이동거리
	return ans;
}
