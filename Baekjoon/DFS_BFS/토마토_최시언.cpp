#include <stdio.h>
#include <stdlib.h>
 
int map[1001][1001] = {0};



void dfs(int n){
    walk or teleport
    dfs (n+1)
}



void tomate(int a, int b){
    int tomate = a*b;
    ans++;
    visit[n] = 1;
    for (int i=1; i<=computer_num; i++){
        if (map[n][i] && !visit[i])        
            dfs(i);
    }
}

 
int main(){
    int n;
    int x, y;
    scanf("%d %d", &x, &y);
    for (int i=0; i<n; i++){
        scanf("%d %d", &x, &y);
        map[x][y] = map[y][x] = 1;
    }
 
    tomato(x,y);
 
 
}
