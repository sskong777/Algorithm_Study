from collections import defaultdict


def solution(N, number):
    dp = defaultdict(set)

    for i in range(1, 9):  # 8보다 크면 어짜피 결과 -1
        dp[i].add(int(str(N)*i))  # 5,55,555
        for j in range(1, i):
            for x in dp[j]:

                for y in dp[i - j]:  # 3번째부터는 계산이 2번째 계산한 수와 첫번째 계산한수/ 첫번째 계산한 수와 두번쨰 계산한 수의 결과
                    # 4번째는 1-3/2-2/3-1 식으로 쭉 추가
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        if number in dp[i]:
            return i

    return -1  # 최솟값이 8번보다 클 경우
