//주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

#include <iostream>

using namespace std;

int main(void) {
	
	int n;
	int this_num;
	int check = 0;
	int count = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		check = 0;
		cin >> this_num;
		if (this_num == 1)
			check = 1;
		for (int j = 2; j < this_num; j++) { //소수인지 소수가 아닌지 체크한다.
			if (this_num % j == 0) {
				check = 1; //소수가 아니다.
			}
		}
		if (check ==0) {
			count++;
		}
	}
	cout << count;
}
