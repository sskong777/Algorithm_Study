N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


# ans = set()
ans = A + B
ans.sort()
print(*ans)