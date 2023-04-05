
n, m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = []
a_p , b_p = 0,0

while True :
    if a_p == n or b_p == m:
        break
    
    if a[a_p] < b[b_p] :
        ans.append(a[a_p])
        a_p+=1
    elif a[a_p] > b[b_p]:
        ans.append(b[b_p])
        b_p+=1
    else:
        ans.append(a[a_p])
        ans.append(b[b_p])
        a_p+=1
        b_p+=1

if a_p !=n:
    for i in range(a_p,n):
        ans.append(a[i])
if b_p!=m:
    for i in range(b_p,m):
        ans.append(b[i])


for x in ans:
    print(x, end=' ')