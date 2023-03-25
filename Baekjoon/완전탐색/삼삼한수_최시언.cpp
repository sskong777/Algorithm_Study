//삼삼한 수
//삼의 거듭제곱의 합으로 나타낼 수 있는 수인지를 묻는 문제
//근데 결국 그냥 3진법으로 쓸 수 있는가를 묻는게 아닌가 싶다.

//각 자리 숫자를 정하는 방법! 수를 3으로 나눈다, 

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

int main(void) {
	int a;
	cin >> a;
	if (a == 0) cout << "NO"; return 0;
	while (!a) {
		if (a % 3 == 2) { //얘는 허용이됨.
			cout << "NO"; return 0;
		}
		a /= 3; //만족했으면 한 번 더 나누기! 언제까지?

	}
	cout << "YES";
}
