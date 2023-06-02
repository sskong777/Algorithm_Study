# [25756] 방어율 무시 계산하기
import math

n = int(input())
num_list = map(int, input().split())  # 20 20 20 20 20

defense = 1
for num in num_list:
    defense *= 1-(num/100)
    defense_rate = (1-defense)*100

    print(round(defense_rate, 6))
