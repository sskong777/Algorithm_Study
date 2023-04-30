# [2960] 에라토스테네스의 체
"""
K번째 지워진 수를 출력한다.
"""
N, K = map(int, input().split())  # 7, 3
n_list = [False] * (N+1)
count = 0

for i in range(2, N+1):  # 2,3,4,5,6,7
    if n_list[i] == False:
        for j in range(i, N+1, i):  # [순서] 2의배수 지우기 -> 3의배수 지우기 -> ...
            if n_list[j] == False:  # 지운수는 False -> True로 표시
                n_list[j] = True
                count += 1
                if count == K:
                    print(j)  # 2, 4, "6"
