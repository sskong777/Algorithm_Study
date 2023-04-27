N,K = map(int,input().split(' '))

list_N=[]
for i in range(2,N+1):
    list_N.append(int(i))
i=list_N[0]
j=0
pop_list=[]
L=len(list_N)
while K>0:
    if j==L:
        i=list_N[0]
        j=0
    if list_N[j]%i==0:
        K-=1
        pop_list.append(list_N[j])
        list_N.pop(j)
        L=len(list_N)
    else:
        j+=1   
print(pop_list.pop())
