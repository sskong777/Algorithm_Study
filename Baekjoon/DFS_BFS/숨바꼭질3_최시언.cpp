#include <stdio.h>
#include <stdlib.h>
 
int map[101][101] = {0};
int S; //subin
int K; //subin K

void walk(int n){
    ans++;
    visit[n] = 1;
    for (int i=1; i<=computer_num; i++){
        if (map[n][i] && !visit[i])        
            dfs(i);
    }
}

void teleport(int n){
    
    }


void dfs(int n){
    walk or teleport
    dfs (n+1)
}
 
int main(){
    int n;
    int x, y;
    scanf("%d %d", &computer_num, &n);
    for (int i=0; i<n; i++){
        scanf("%d %d", &x, &y);
        map[x][y] = map[y][x] = 1;
    }
 
    dfs(1);
    printf("%d\n", ans - 1);
 
 
}
