N = int(input())
arr = list(input())

answer = 0
for i in range(N//2):
    if arr[i] != arr[N-i-1]:
        answer += 1
print(answer)