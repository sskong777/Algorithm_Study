N = int(input())

for i in range(N):
    arr = input().split(' ')[::-1]
    print("Case #{}: {}".format(i+1, ' '.join(arr)))