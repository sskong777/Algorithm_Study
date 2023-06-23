# 숏코딩
f,r=lambda:map(int,input().split()),range;N,D=f()
p,cut=[0]*(D+1),{}
for _ in r(N):s,e,d=f();cut.setdefault(e,[]).append((s,e,d))
for i in r(1,D+1):t=p[i-1]+1;p[i]=min(t,min(p[s]+d for s,e,d in cut[i]))if i in cut else t
print(p[-1])

# 원본

# import sys
# N, D = map(int, input().split())

# dp = [0] * (D+1)
# cut = {}

# for l in sys.stdin.readlines():
#     s,e,d = map(int, l.strip().split())
#     cut.setdefault(e, []).append((s,e,d))
    
# for i in range(1, D+1):
#     if i not in cut:
#         dp[i] = dp[i-1]+1
#         continue
#     dp[i] = min(dp[i-1]+1, min(dp[s]+d for s, e, d in cut[i]))

# print(dp[-1])
