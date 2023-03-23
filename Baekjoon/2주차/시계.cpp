//코레스코 콘도가 누군데 이 씹덕아
//1부터 체크하는 방식으로 가야한다. 아예 시간 체크가 불가능한 경우는 없다.
//항상 최소로 가고 싶음으로, 절대 존재해서는 안되는걸 하나하나 체크하자. 앞에 있는 중복을 제외하고.

// (clock[checking_time * 4 + 0][0] != '*' && clock[checking_time * 4 + 1][0] != '*' && clock[checking_time * 4 + 2][0] != '*' &&
//	clock[checking_time * 4 + 0][1] != '*' && clock[checking_time * 4 + 1][1] != '*' && clock[checking_time * 4 + 2][1] != '*' &&
//	clock[checking_time * 4 + 0][2] != '*' && clock[checking_time * 4 + 1][2] != '*' && clock[checking_time * 4 + 2][2] != '*' &&
//	clock[checking_time * 4 + 0][3] != '*' && clock[checking_time * 4 + 1][3] != '*' && clock[checking_time * 4 + 2][3] != '*' &&
//	clock[checking_time * 4 + 0][4] != '*' && clock[checking_time * 4 + 1][4] != '*' && clock[checking_time * 4 + 2][4] != '*'
//	) {
//	return 0;
//}

#include <iostream>
using namespace std;

void professor_cungang(int a);
int time_check(int checking_time,char clock[15][5]);

int main(void) {

	char clock[15][5] = {0};
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 15; j++) {
			if (j == 3 || j == 7 || j == 11) {
				continue; //j++ 사용시 아래있는 공백이 실행됨
			}
			cin >> clock[j][i];
		}
	}
	

	int first = time_check(0,clock);
	int second = time_check(1, clock);
	int third = time_check(2, clock);
	int fourth = time_check(3, clock);

	cout << first << second << ":" << third << fourth;

}

int time_check(int checking_time,char clock [15][5]) { //시간 순서의 입력은 0부터 받는다고 가정한다.
		if (clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 1][2] != '#' && clock[checking_time * 4 + 1][3] != '#') 
			return 0;
		if (clock[checking_time * 4 + 0][0] != '#' && clock[checking_time * 4 + 1][0] != '#' && clock[checking_time * 4 + 0][1] != '#' && clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 0][2] != '#' && clock[checking_time * 4 + 1][2] != '#' && clock[checking_time * 4 + 0][3] != '#' && clock[checking_time * 4 + 1][3] != '#'&& clock[checking_time * 4 + 0][4] != '#' && clock[checking_time * 4 + 1][4] != '#' )
			return 1;
		if (clock[checking_time * 4 + 0][1] != '#' && clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 1][3] != '#' && clock[checking_time * 4 + 2][3] != '#')
			return 2;
		if (clock[checking_time * 4 + 0][1] != '#' && clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 0][3] != '#' && clock[checking_time * 4 + 1][3] != '#')
			return 3;
		if (clock[checking_time * 4 + 1][0] != '#' && clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 0][3] != '#' && clock[checking_time * 4 + 1][3] != '#' && clock[checking_time * 4 + 0][4] != '#' && clock[checking_time * 4 + 1][4] != '#')
			return 4;
		if (clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 2][1] != '#' && clock[checking_time * 4 + 0][3] != '#' && clock[checking_time * 4 + 1][3] != '#')
			return 5;
		if (clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 2][1] != '#' && clock[checking_time * 4 + 1][3] != '#')
			return 6;
		if (clock[checking_time * 4 + 0][1] != '#' && clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 0][2] != '#' && clock[checking_time * 4 + 1][2] != '#' && clock[checking_time * 4 + 0][3] != '#' && clock[checking_time * 4 + 1][3] != '#' && clock[checking_time * 4 + 0][4] != '#' && clock[checking_time * 4 + 1][4] != '#')
			return 7;
		if (clock[checking_time * 4 + 1][1] != '#' && clock[checking_time * 4 + 1][3] != '#')
			return 8;
		else
			return 9;
}
