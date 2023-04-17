# [5568] 카드 놓기
from itertools import permutations

n = int(input())   # 카드의 개수
k = int(input())   # 선택할 카드의 개수

cards = [int(input()) for _ in range(n)]

result = set()

for i in permutations(cards, k):
    result.add(''.join(map(str, i)))    # 1, 2 --> 12   # 각 원소를 문자열로 변환 후 사용

print(len(result))
