# def factorial(n):
#     memo = [0] * (n+1)  # memo 배열 초기화
#     memo[0] = 1  # 0!은 1이므로 초기값 설정
#     for i in range(1, n+1):
#         memo[i] = i * memo[i-1]  # 이미 계산한 값을 저장하여 재사용
#     return memo[n]


# 팩토리얼로 풀면 메모리 초과 남 -> 팩토리얼로 푸는 문제가 아니다!

def sol(n, a):
    count = 0
    while n > 0:
        count += n // a
        n //= a
    return count

N, A = map(int,input().split())
ans = sol(N,A)
print(ans)

