//응 시간초과야 ^^;;

// 20!에 곱해진 2의 개수

// 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
//   1   1   1   1    1     1     1     1     1     1 #2가 곱해진 개수 5개
//       1       1          1           1           1 #2가 곱해진 개수 3개
//               1                      1	     #2가 곱해진 개수 2개


#include <iostream>
using namespace std;

int fact(long long n, long long k) {
	int count = 0;
	long long kmult = k;
	while (n >= kmult) {
		count += n / kmult;
		kmult *= k;
	}
	return count;
}

int main(void) {
	long long n;
	long long k;
	cin >> n >> k;
	cout << fact(n,k);
}

//#include <iostream>
//#include <math.h>
//
//using namespace std;
//int count_number(int n, int k);
//int count_fact(int n, int k);
//
//int main(void) {
//
//	int n, k;
//	cin >> n >> k;
//	int count_11, count_2, count_3, count_5, count_7;
//	//n을 소인수분해하면서 가지고 있는 소수의 개수를 입력한다. -> 배열이용
//
//	count_2 = count_fact(n, 2);
//	count_3 = count_fact(n, 3);
//	count_5 = count_fact(n, 5);
//	count_7 = count_fact(n, 7);
//	count_11 = count_fact(n, 11);
//
//	cout << max(count_2,max(count_5, max(count_7, max(count_3,count_11))));
//	
//}
//
//int count_number(int n,int k){
//	int count = 0;
//	while(20180825){
//	if ((n % k) == 0) {
//		n = n / k;
//		count++;
//	}
//	else{
//		return count;
//	}
//}
//}
//
//int count_fact(int n, int k) {
//	int count=0;
//	while (20180825) {
//		count += count_number(n, k);
//		n--;
//		if (n == 1)
//			return count;
//	}
//}
//
