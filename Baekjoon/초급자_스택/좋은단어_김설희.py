n = int(input())
cnt = 0

for _ in range(n):

    word = input()
    stack = []

    for i in word:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    if not stack:
        cnt += 1

print(cnt)