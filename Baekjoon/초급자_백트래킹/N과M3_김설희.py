n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 M개를 고른 수열 (중복 가능)

numslist = []

def dfs(k):
    if k == m: # 검사하는 시작 숫자가 고른 개수랑 같으면
        print(' '.join(map(str, numslist)))
        return

    for i in range(1, n + 1): # 첨부터 다임
        numslist.append(i)
        dfs(k + 1) # k 다음수부터!!
        numslist.pop() # 지우고 다음 뒤 숫자

dfs(0)