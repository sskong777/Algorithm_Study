#include<iostream>
#include<queue>
#include<algorithm>

using namespace std;

int dist[100001]; // 0<=  n   <= 100000

int m, n;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> m >> n;
    
    queue<int> Q;
    
    fill(dist, dist+100001, -1); // 0~ 100000까지 -1
    
    
    dist[m] = 0;
    Q.push(m);
    
    while(!Q.empty()){
        int cur = Q.front();
        Q.pop();
        
        
        if(cur-1 >= 0 && dist[cur-1] < 0){
            dist[cur-1] = dist[cur] + 1;
            Q.push(cur-1);
        }
        if(cur+1 <= 100000 && dist[cur+1] < 0){
            dist[cur+1] = dist[cur] + 1;
            Q.push(cur+1);
        }
        if(cur*2 <= 100000 && dist[cur*2] < 0){
            dist[cur*2] = dist[cur] + 1;
            Q.push(cur*2);
        }
        
        if(dist[n] != -1){
            cout<<dist[n];
            break;
        }
        
    }

    
}
