n = int(input())
str = list(input())
cnt = 0

for i in range(n // 2) :
    if str[i] != str[-1-i] :
        cnt += 1

print(cnt)
