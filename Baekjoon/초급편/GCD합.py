import sys
def gcd(a, b):  # 최대공약수 함수(유클리드 호제법)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))  # 리스트로 받아오기
    temp = 0
    for j in range(1, len(a)):  # 첫 수는 제외
        for k in range(1, len(a)):
            if j < k:  # 모든 쌍을 구할 때(중복 없이)
                temp += gcd(a[j], a[k])
            else:
                pass
    print(temp)