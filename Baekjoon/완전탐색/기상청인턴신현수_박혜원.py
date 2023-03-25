# [2435] 기상청인턴신현수
# 1차시도 실패 이유: 12열이 "for j" 반복문안에 있어서 sum 변수가 누적되어 추가되지 않고, 모든 sum 값이 각각의 i에 대한 값으로 추가되었음.

N, K = map(int, input().split())  # 날짜의 수, 연속적인 날짜
temps = list(map(int, input().split()))  # 측정한 온도 리스트

temps_sum = []
for i in range(N-K+1):  # 9번
    sum = 0
    for j in range(i, i+K):  # 2개씩 1,2  2,3  3,4 등등..
        sum += temps[j]
    temps_sum.append(sum)


print(max(temps_sum))
