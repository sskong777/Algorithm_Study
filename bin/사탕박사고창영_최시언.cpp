//사탕박사 고창영
//가로로 한 번, 세로로 한 번 세면된다.
//>o<

//v
//o
//^

//789
//456
//123

#include <stdio.h>
#include <iostream>

using namespace std;
int main(){
	int t;
	cin >> t;
	while (t--)
	{
		char s[600][600];
		int x, y;
		cin >> x >> y;
		int ans = 0;
		for (int i = 0; i < x; i++)
			cin >> s[i];
		for (int i = 0; i < x; i++)
		{
			for (int j = 0; j < y - 2; j++)
			{
				if (s[i][j] == '>' && s[i][j + 1] == 'o' && s[i][j + 2] == '<') ans++;
			}
		}
		for (int i = 0; i < x - 2; i++)
		{
			for (int j = 0; j < y; j++)
			{
				if (s[i][j] == 118 && s[i + 1][j] == 'o' && s[i + 2][j] == 94) ans++;
			}
		}
		printf("%d\n", ans);
	}
}
