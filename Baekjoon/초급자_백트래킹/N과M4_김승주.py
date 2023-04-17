
n, m = map(int,input().split())

ans = []
def back(dep,i):
    
    if dep == m:
        print(' '.join(map(str, ans)))
        return

    for j in range(i, n+1):
        ans.append(j)
        back(dep+1, j)
        ans.pop()
        

back(0,1)