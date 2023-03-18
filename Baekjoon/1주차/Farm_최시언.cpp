//이거 그 소금물 문제 맞지..

#include <stdio.h>
#include <iostream>
using namespace std;

int main(void) {

	int a, b, n, w;
	int ans=-1;

	cin >> a >> b >> n >> w; //a : 양 b: 소 n:전체 마릿수 w:전체 사료의양

	for (int i = 1; i < n; i++) { //1마리 전체~ 전체 1마리까지 있어야함. 2 1 1
		if (w==(i * a) + ((n - i) * b)) {
			if (ans == -1){ //답이 없는 경우
			ans = i;			}
			else {
				ans = -1;
				break;
			}
		}
	}
	if (ans != -1)
	cout << ans << " " << n - ans;
	else {
		cout << ans;
	}
}
