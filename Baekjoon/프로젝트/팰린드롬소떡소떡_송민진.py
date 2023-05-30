n = int(input())
arr = list(input())
cnt = 0
for i in range(n//2):
    if arr[i] != arr[n-i-1]:
        cnt += 1

print(cnt)