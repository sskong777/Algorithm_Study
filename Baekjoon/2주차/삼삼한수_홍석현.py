# sol1 - 재귀

def dfs(i, ssum):
    global N
    if ssum+(3**i) > N: return 0
    if ssum+(3**i) == N: return 1
    if dfs(i+1, ssum): return 1
    if dfs(i+1, ssum+3**i): return 1

N = int(input())
print('YES' if dfs(0, 0) else 'NO')


# sol2 - 반복문
n = int(input())
flag = True
if n == 0:
    flag = False

while n > 0:
    if n % 3 == 2:
        flag = False
    n //= 3

print("YES" if flag else "NO")