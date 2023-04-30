# [1292] 쉽게푸는문제

a, b = map(int, input().split())
li = []
for i in range(46):
    for _ in range(i):
        li.append(i)

answer = li[a-1:b]
answer = sum(answer)
print(answer)

# print(li)
# print(len(li))
