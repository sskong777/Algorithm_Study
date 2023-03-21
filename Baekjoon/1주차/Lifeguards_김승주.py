
import sys
input = sys.stdin.readline

n = int(input())

life_guards =[]
for _ in range(n):
    start,end = map(int,input().split())
    life_guards.append((start,end))

life_guards.sort(key=lambda x : (x[0],x[1]))

ans =0
for i in range(n): 
    count = 0
    check = [0]*(1001)    
    for j in range(n):
        if i==j:
            continue
        for k in range(life_guards[j][0],life_guards[j][1]):
            if check[k] == 0 :
                check[k] += 1
                count+=1
    ans = max(ans, count)

print(ans)
