import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
toadd = []
tmp = [arr[0]]
idx = 1

while idx < len(arr):
    if arr[idx-1] + 1 == arr[idx]:
        tmp.append(arr[idx])
    else:
        toadd.append(tmp)
        tmp = [arr[idx]]
    idx += 1
    
toadd.append(tmp)
ret = 0
for l in toadd:
    ret += l[0]
print(ret)
