//근의 공식을 이용한 풀이방식.


#include<iostream>
#include <string>
#include <cmath> //sqrt를 위해 추가

using namespace std;

int main(void) {
	int a, b;
	cin >> a >> b;
	int plus=	-a+sqrt(a*a-b);
	int minus = -a - sqrt(a * a - b);
	
	if (plus == minus) {
		cout << plus << '\n';
	}
	else
		cout << minus << " " << plus << '\n';
	return 0;
}
