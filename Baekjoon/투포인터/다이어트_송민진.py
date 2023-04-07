g = int(input())

before, now = 1, int(g**0.5)
answers = []
while True:
    tmp = now**2 - before**2
    if before + 1 >= now and tmp > g:
        break
    else:
        if tmp == g:
            answers.append(now)
            before += 1
        elif tmp > g:
            before += 1
        else:
            now += 1

if answers:
    for ans in answers:
        print(ans)
else:
    print(-1)