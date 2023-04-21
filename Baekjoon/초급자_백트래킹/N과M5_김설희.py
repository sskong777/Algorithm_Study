n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
numlist = []

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열

def dfs(k):
    if k == m:
        print(' '.join(map(str, numlist)))
        return

    for i in nums:
        if i not in numlist:
            numlist.append(i)
            dfs(k + 1)
            numlist.pop()

dfs(0)