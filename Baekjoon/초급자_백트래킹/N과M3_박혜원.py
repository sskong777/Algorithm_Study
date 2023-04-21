# [15651] N과M3
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다 -> 중복가능!! (1 1) (2 2)
# 길이가 M개인 수열 출력 하는것.
# num 은 선택한 숫자의 개수


n, m = map(int, input().split())

result = []


def backtracking(num):
    if num == m:  # 종료조건
        print(" ".join(map(str, result)))
        return

    for i in range(1, n+1):
        # if i not in result:  # 중복을 허용하지 않을 때 작성
        result.append(i)
        backtracking(num+1)
        result.pop()


backtracking(0)
