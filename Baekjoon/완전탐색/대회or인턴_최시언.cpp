//2명의N과 1명의M이 한 팀이 될 수 있다.
//K명은 인턴을 나가야 한다. 인턴에 나간 사람은 대회에 참여하지 못한다.
//그리디 알고리즘을 사용한다.

#include <stdio.h>
#include <iostream>

using namespace std;

int main(void) {

	
	int n, m, k;
	cin >> n >>m >> k;
	
	cout << min(min(n / 2, m), (n + m - k) / 3) << "\n";

}
