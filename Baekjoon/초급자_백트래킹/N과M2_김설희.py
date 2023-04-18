n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
numslist = []

def dfs(k):
    if len(numslist) == m:
        print(' '.join(map(str, numslist)))

    for i in range(k, n + 1): # 앞 숫자부터 차례대로 넣어야 하니까
        if i not in numslist:
            numslist.append(i)
            dfs(i+1) # 앞 숫자 결정됐고 뒤에부터
            numslist.pop() # 지우고 다음 뒤 숫자

dfs(1)