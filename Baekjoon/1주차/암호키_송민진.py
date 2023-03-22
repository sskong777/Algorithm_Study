import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = int(input())

    # # 1. 소수 구하기
    # def is_prime(n):
    #     if

    tmp_s = s
    for num in range(2, int(1e6)+1):
        if tmp_s == 0:
            break
        elif tmp_s % num == 0:
            tmp_s //= num
    if s == tmp_s and tmp_s > int(1e6):
        print("YES")
    else:
        print("NO")