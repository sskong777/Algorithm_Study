# [11728] 배열합치기

n, m = map(int, input().split())

# 배열 합치기
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_ab = list_a + list_b
answer_list = sorted(list_ab)
print(*answer_list)
