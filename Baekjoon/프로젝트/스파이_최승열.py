f=lambda:map(int,input().split())
N,M=f()
P=list(f())+list(f())
def dfs(n,m,l):
  if m<=0:return 6**n
  elif n==0:return 0
  return sum(dfs(n-1,m-P[p]+(P[p]*1/2*(l in[p,(p+3)%6])),p)for p in range(6))
print(dfs(N,M,-1))