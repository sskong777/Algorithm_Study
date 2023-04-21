//차이를 최대로 하는 문제, 처음에 솔트 한 다음에 징검징검하면될듯.

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <stdlib.h> //abs
#include <vector>

//i + 0 N - 0
//i + 1 N - 0
//i + 1 N - 1

using namespace std;

int main(void) {

	int N;
	int array[8];
	int sum = 0;
	int sum_G = 0;
	cin >> N;
	int tmp;

	vector <int> VEcTor;

	for (int i = 0; i < N; i++) {

		cin >> tmp;
		VEcTor.push_back(tmp);
	}

	sort(VEcTor.begin(), VEcTor.end()); //N까지 정렬

	//int i = 0;
	//int j = 0;

	do {
		sum_G = 0;
		for (int i = 0 ; i< N-1 ; i++)
			sum_G += abs(VEcTor[i] - VEcTor[i + 1]);
		if (sum_G >= sum)
			sum = sum_G;
	} 
	while (next_permutation(VEcTor.begin(), VEcTor.end()));

	cout << sum;

}
