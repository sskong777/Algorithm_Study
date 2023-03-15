'''
문제 : 통학의 신 ( 17945 ) - 완전탐색
'''
import sys
input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())
    ans =[]

    for i in range(-1000, 10001):
        if i*(2*a-i) == b:
            ans = list(set([-i, -(2*a-i)]))

    print(*sorted(ans))

solution()