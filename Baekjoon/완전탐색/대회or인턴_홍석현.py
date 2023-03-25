N, M, K = map(int,input().split())  # 여, 남, 인원

while K !=0 :
    if N > 2*M:
        N -= 1
    else:
        M -= 1
    K -= 1

answer = 0
while N >= 2 and M >= 1:
    N -= 2
    M -= 1
    answer += 1

print(answer)




