//색종이의 수가 3개가 아닌 100개 이하라는 점을 알고 있어야 함.

#include <stdio.h>
#include <iostream>

using namespace std;

int main(void) {

	
	int n;
	int x, y;
	int count = 0;
	int paper[100][100] = {0,};
	
	cin >> n; //전체 색종이의 개수를 입력받는다.

	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		for (int j = x; j < x+10; j++) {
			for (int k = y; k < y+10; k++) {
				paper[j][k] = 1;
			}
		}
	}

	for (int l = 0; l < 100; l++) {
		for (int m = 0; m < 100; m++) {
			if (paper[l][m]==1) {
				count++;
			}
		}
	}

	cout << count;
}
