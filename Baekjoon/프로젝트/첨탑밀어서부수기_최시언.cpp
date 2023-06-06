#include <iostream>
using namespace std;
int main(){
	ios::sync_with_stdio(false), cin.tie(NULL);
    register int N, t1 = 0, t2, cnt = 0;
    cin >> N;
    for(register int n = 0; n < N; ++n){
        cin >> t2;
        if(t1 <= t2)
            ++cnt;
        t1 = t2;
    }
    cout << cnt;
    return 0;
}
// *&)*@*
