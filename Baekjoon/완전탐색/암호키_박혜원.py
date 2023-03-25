# [1816] 암호키
# 10^6 이하로 나누어 진다면 적절하지 않은 암호키 이다. (NO)
# 시간초과 --> verify = False 추가


N = int(input())
answer = []

for _ in range(N):
    num = int(input())
    verify = False
    for i in range(2, 1000001):
        if num % i == 0:
            answer.append("NO")
            verify = True
            break
    if verify is False:
        answer.append("YES")


for i in answer:
    print(i)
