
n = int(input())

def dfs(total, i ):
    global n 
    if total + (3**i) > n:
        return 0
    
    if total + (3**i) == n:
        return 1

    if dfs(total+(3**i),i+1) :
        return 1
    
    if dfs(total,i+1):
        return 1

print( "YES" if dfs(0,0) else "NO")
