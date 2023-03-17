#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

int main(void) {
	int count = 0;
    int a;
	int now_number = 1;
	vector <int> number_vector;

	for (int i = 0; i < 5; i++){
		cin >> a;
        number_vector.push_back(a);
	}

	while (20180825) {
		count = 0;
		for (int j = 0; j < 5; j++) {
			if (0 == (now_number % number_vector[j]))
				count++;
				}
		if (count >= 3) {
			break;
		}

		now_number++;
	}
	cout << now_number;

}
