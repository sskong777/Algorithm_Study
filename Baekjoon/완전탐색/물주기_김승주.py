import sys
input = sys.stdin.readline

n,k,a,b = map(int,input().split())

kkatnip = [k] * n

count = 0
while 1:
    kkatnip.sort()
    count+=1
    for i in range(a):
        kkatnip[i]+=b
    
    for i in range(n):
        kkatnip[i]-=1
        if kkatnip[i] <= 0:
            print(count)
            exit()

