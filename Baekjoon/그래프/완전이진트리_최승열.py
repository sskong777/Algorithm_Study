I=input
K=int(I())
T=list(map(int,I().split()))
A=[[]for _ in range(K)]
def s(l,r,d):
 if l==r:A[d].append(T[l]);return
 m=(l+r)//2;A[d].append(T[m])
 s(l,m-1,d+1);s(m+1,r,d+1)
s(0,len(T)-1,0)
print("\n".join(" ".join(map(str,a))for a in A))