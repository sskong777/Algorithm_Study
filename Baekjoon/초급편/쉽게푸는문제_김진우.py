a, b = map(int,input().split())
arr = []
for i in range(1,b):
    for j in range(i):
        arr.append(i)

if a==1 and b==1 :
    print(1)
else:
    print(sum(arr[a-1:b]))
