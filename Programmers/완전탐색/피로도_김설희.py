
# 순서를 순열로 뽑아냈음
def dfs(v, dungeons, k, check, result, max_cnt):
    n = len(dungeons)

    if v == n:
        cnt = 0
        for dungeon in result:
            need, consume = dungeon
            if need <= k:
                k -= consume
                cnt += 1
            else:
                break
        max_cnt[0] = max(max_cnt[0], cnt)
        return

    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                result[v] = dungeons[i]
                dfs(v + 1, dungeons, k, check, result, max_cnt)
                check[i] = 0

def solution(k, dungeons):

    n = len(dungeons)
    check = [0] * n
    result = [0] * n
    max_cnt = [0] # 값을 저장하려면 정수가 아니라 배열로

    dfs(0, dungeons, k, check, result, max_cnt)
    return max_cnt[0]

print(solution(100, [[80, 8], [90, 9], [100, 10]]))
