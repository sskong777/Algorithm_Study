def gcd(a,b):
    if a%b==0:
        return b
    elif a>=b:
        return gcd(b,a%b)
    else:
        a,b=b,a
        return gcd(a,b)
    
n=int(input())
gcdSum=0
k=1
j=2
arr=[list(map(int,input().split())) for _ in range(n)]

for i in arr:
    if len(i)==2:
        gcdSum+=i[1]
    while k<len(i)-1:
        if j <len(i):
            num=gcd(i[k],i[j])
            gcdSum+=num
            j+=1
        else:
            k+=1
            j=k+1
            
    print(gcdSum)
    gcdSum=0
    k=1
    j=2
