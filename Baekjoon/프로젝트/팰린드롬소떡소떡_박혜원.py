# [24530] 팰린드롬 소떡소떡
# s 소세지 t 떡

N = int(input())
stst = list(input())
count = 0

for i in range(N//2):
    if stst[i] != stst[-1-i]:
        count += 1
print(count)
