import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

li = [0 for _ in range(n)]

for _ in range(m):
    i = int(input())
    li[i] = 1


temp=[0 for _ in range(n)]

for i in range(k):
    for j in range(n):
        if li[j]==1:
            temp[(j-1)%n]= (temp[(j-1)%n]+1) %2
            temp[(j+1)%n] = (temp[(j+1)%n]+1) %2
    li=temp.copy()
    temp = [0 for _ in range(n)]

print(li.count(1))