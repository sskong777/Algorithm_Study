# [9613] GDC합
"""
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
"""

# 유클리드 호제법 -> 최대공약수 함수


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


n = int(input())

for _ in range(n):
    num_list = list(map(int, input().split()))
    answer = 0
    # 1을 제와하는 이유 : 테스트케이스 n개 + n개의 수가 한 라인에 주어진다.
    for i in range(1, len(num_list)):
        for j in range(i+1, len(num_list)):
            if i < j:
                answer += gcd(num_list[i], num_list[j])
            else:
                pass
    print(answer)
