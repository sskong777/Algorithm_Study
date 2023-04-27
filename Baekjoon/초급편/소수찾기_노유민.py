n=int(input())

list_n=list(map(int,input().split(' ')))
count=0
if_ok=True

for i in list_n:
    if i==1:
        continue

    for j in range(2,i):
        if i%j==0:
            if_ok=False
            break
    if(if_ok==True):
        count+=1
        
    if_ok=True
print(count)
    