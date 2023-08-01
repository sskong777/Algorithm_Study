import heapq as h,sys;m,r=lambda:map(int,sys.stdin.readline().split()),range;N,M=m()
g=[[]for _ in r(N+1)]
for _ in r(M):s,e,d=m();g[s].append((d,e));g[e].append((d,s))
I=1e8;D=[I]*(N+1);D[1]=0
q=[(0,1)]
while q:
 d,n=h.heappop(q)
 if D[n]<d:continue
 for l,e in g[n]:
  t=d+l
  if t<D[e]:D[e]=t;h.heappush(q,(t,e))
print(D[N])