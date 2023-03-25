N, K ,A, B = map(int,input().split())

def check():
    flag = True
    for i in range(N):
        if arr[i] <= 0:
            flag = False
            break
    return flag


arr = [K] * N

count = 0
n = 0
while check():
    for i in range(A):
        if n > N-1:
            n -= N
        arr[n] += B
        n += 1
    for i in range(N):
        arr[i] -= 1
    count += 1
print(count)