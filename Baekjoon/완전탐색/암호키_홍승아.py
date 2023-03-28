# [1816] 암호 키
import sys
input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]

for s in S:
    flag = True
    for i in range(2, 1000001):
        if s % i == 0:
            flag = False
            break
    
    if flag == True:
        print("YES")
    else:
        print("NO")