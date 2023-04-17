
from itertools import combinations


from itertools import*
n,_,m=input()
*starmap(print,combinations(range(1,int(n)+1),int(m))),

'''
다른 풀이  : 백트래킹

n, m = list(map(int, input().split()))

s  =[]


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)

'''