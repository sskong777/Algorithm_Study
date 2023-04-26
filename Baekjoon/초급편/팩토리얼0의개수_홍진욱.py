n=int(input())
fac = 1
chk = 0
for i in range(1,n+1):
    fac*=i
while(True):
    if fac%10==0:
        chk+=1
        fac//=10
    else:
        break
print(chk)