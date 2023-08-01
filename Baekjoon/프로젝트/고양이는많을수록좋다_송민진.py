n = int(input())

if n == 0:
    answer = 0
else:
    now = 1
    answer = 1
    while now < n:
        if now * 2 >= n:
            answer += 1
            break
        else:
            now *= 2
            answer += 1

print(answer)