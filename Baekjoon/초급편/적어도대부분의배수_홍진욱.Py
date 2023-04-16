num = list(map(int,input().split()))
i=min(num)

while(True):
    check=0
    for j in range(4):
        if(i%num[j]==0):
            check+=1
    if check >=3:
        print(i)
        break
    i+=1