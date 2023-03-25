//조건을 가장 빠르게 줄어드는 순서대로 정의 하면 되지 않을까.

#include <stdio.h>
#include <iostream>

using namespace std;

int main(void) {
	int a, b, c =0; //택희, 영훈, 남규
	int N;
	int count = 0;

	//1. c >= b + 2;
	//2. a,b,c != 0
	//3. a%2!=1

	cin >> N;

	for (a = 2; a < N; a=a+2) {
		for (b = 1; b < N; b++) {
			for (c = b + 2; c < N; c ++) {
				if ((a + b + c) == N) {
					count++;
				}
			}
		}
	}
	cout << count;
}
