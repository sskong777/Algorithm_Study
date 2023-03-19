# [145680] 2017 연세대학교 프로그래밍 경시대회

# 영훈(a)
# 남규(b): b >= a+2
# 택희(c): 짝수개 받기

num = int(input())
count = 0

for a in range(num):
    for b in range(num):
        for c in range(num):
            if b >= a+2 and a >= 1 and c >= 1:
                if c % 2 == 0:
                    if a + b + c == num:
                        count += 1
print(count)


"""
# 다른 풀이 
# range(start, stop, step)

남규가 영훈이보다 더 가져가야할 사탕 2개를 미리 빼둔다.
택희가 가져가야될 사탕(= i)은 2의 배수이다.

num = int(input())
count = 0
for i in range(2, num-1, 2):
    count += (num - i - 2)
print(count)
"""
