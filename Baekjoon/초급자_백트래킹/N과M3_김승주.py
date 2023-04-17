
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ans =[ ]
def back(dep):
    
    if dep == m:    
        print(' '.join(map(str, ans)))
        return 
    
    for i in range(1, n+1):
        ans.append(i)
        back(dep+1)
        ans.pop()


back(0)