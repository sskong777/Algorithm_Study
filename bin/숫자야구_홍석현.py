from itertools import permutations

N = int(input())

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# numbers = [map(str,j) for j in range(1,10)]/
num = list(permutations(numbers, 3))

for _ in range(N):
    test_num, test_strike, test_ball = map(int, input().split())
    test_num = list(str(test_num))
    rm_cnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= rm_cnt
        for j in range(3):
            if num[i][j] == test_num[j]:
                strike += 1
            elif test_num[j] in num[i]:
                ball += 1

        if (strike != test_strike) or (ball != test_ball):
            num.remove(num[i])
            rm_cnt += 1

print(len(num))