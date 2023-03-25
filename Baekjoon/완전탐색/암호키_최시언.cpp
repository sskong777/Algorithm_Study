//스트라이크의 경우 확정, 볼의 경우 사용된 숫자의 사용 가능성을 판단 할 수 있다.
//즉, 볼은 유의미한 정보이며 이를 둘 다 체크해야 한다.
//배열로 관리하되, 사용될 가능성과 위치를 전부 저장해야 한다.
//근데 백터로 처리하고 싶은데 방법이 없을까?
//어쨌든, 가장 쉽게 해결하는 방법은 그냥 모든 숫자를 돌아가면서 이 숫자가 주어진 조건에 맞는지 확인하는 거

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>

using namespace std;

int main(void) {
	long long n;
	int a;
	vector <string> YESNO;

	cin >> a;
	for (int number=0;number<a;number++){
	cin >> n;
	string check = "YES";

	for (int i = 2; i <= 1000000; i++) {
		if (n % i == 0) {
			check = "NO";
			break;
		}
	}
	YESNO.push_back(check);
	}
	for (int j = 0; j < YESNO.size(); j++)
		cout << YESNO[j] << "\n";
}
