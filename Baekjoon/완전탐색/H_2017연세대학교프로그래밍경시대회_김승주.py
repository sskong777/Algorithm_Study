
n = int(input())
count =0
for i in range(1, n+1):
    for j in range(i+2,n-i-1):
        if ( (n- (i+j))%2)==0:
            count+=1

print(count)