import sys

n, m = map(int, sys.stdin.readline().split())


user = list()
menu = list()
ans = []
for _ in range(n):
    sushi = dict()
    li = list(map(int, sys.stdin.readline().split()))
    ans.append(0)

    for cnt in range(1, li[0]+1):
        sushi[li[cnt]] = False
    user.append(sushi)

menu = list(map(int, sys.stdin.readline().split()))

for m in menu:
    for u in range(len(user)):
        if m in user[u] and not user[u][m]:
            user[u][m] = True
            ans[u] +=1
            break

for i in ans:
    print(i, end=' ')
