#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
	int res = 0;
	int sum = 0;

	for (int i = 0; i < 10; ++i)
	{
		int t;
		scanf("%d", &t);

		sum += t;
		if (abs(100 - sum) <= abs(100 - res))
		{
			res = sum;
		}
	}

	printf("%d\n", res);

	return 0;
}