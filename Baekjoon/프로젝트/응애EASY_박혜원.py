# [28088] 응애(EASY)
# 시간초과
"""
동아리원의 수 N, 
처음에 인사를 하는 사람들의 수 M, 
인사를 진행하는 횟수 K, 
M명의 동아리원이 인사를 시작하는 위치
"""
N, M, K = map(int, input().split())
# 동아리원 인사하는지 안하는지 리스트 초기화. 0->인사안함 1->인사함
hi = [0] * N

# 다음 인사를 준비하는 동아리원 리스트
next_hi = [0] * N

# 처음에 인사하는 동아리원 번호를 1로 바꾸기
for _ in range(M):
    hi[int(input())] = 1

# K번 인사 진행
for _ in range(K):
    next_hi = [0] * N

    for i in range(N):
        if hi[i]:
            next_hi[(i+1) % N] += 1  # 오른쪽
            next_hi[(i-1) % N] += 1  # 왼쪽

    # 다음 인사 상황: 양 옆에서 동시에 인사를 받지 않은 동아리원만 인사를 한다.
    hi = [1 if nh == 1 else 0 for nh in next_hi]

# 1의 개수 세기
print(hi.count(1))
