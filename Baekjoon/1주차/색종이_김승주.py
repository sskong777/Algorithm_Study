
import sys
intput = sys.stdin.readline

n = int(input())

papers = [(map(int,input().split())) for _ in range(n)]

graph = [[0] * 101 for _ in range(101)]

for x,y in papers:
    for i in range(x,x+10):
        for j in range(y,y+10):
            graph[i][j]+=1
            
count = 0
for i in range(1,101):
    for j in range(1,101):
        if graph[i][j]!=0:
            count+=1
print(count)