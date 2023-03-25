A, B, C, N = map(int,input().split())

answer = 0
for a in range(100):
    for b in range(100):
        for c in range(100):
            if N % A == 0 or N % B == 0 or N % C ==0:
                answer = 1
                break
            if a*A + b*B + c*C == N:
                answer = 1
                break
print(answer)