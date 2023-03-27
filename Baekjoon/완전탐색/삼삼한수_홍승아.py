# [17252] 삼삼한 수 (실버 3)
N = int(input())
flag = True
if N == 0:
    flag = False
else:
    while N>0:
        if N % 3 == 2:
            flag = False
            break
        N = N//3

if flag:
    print("YES")
else:
    print("NO")
