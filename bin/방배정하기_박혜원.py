# [14697] 방배정하기
# a, b, c인실   n명
# a인실 i명
# ax + by + cz = n


a, b, c, student = map(int, input().split())

answer = 0  # 조건을 만족하는 경우 answer을 1로 변경

for i in range(student//a + 1):
    for j in range(student//b + 1):
        for k in range(student//c + 1):
            if a*i + b*j + c*k == student:
                answer = 1
                break  # 모든 반복문을 종료


if answer == 1:
    print(1)
else:
    print(0)


"""
# 부분 정답(이유는 모르겠음)
a, b, c, n = map(int, input().split())


def room():
    for z in range(1, 51):
        for y in range(z, 51):
            for x in range(y, 51):
                if (a * x) + (b * y) + (c * z) == n:
                    return 1

    return 0


print(room())
"""
