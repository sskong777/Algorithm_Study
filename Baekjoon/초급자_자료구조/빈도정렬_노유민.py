import sys

input = sys.stdin.readline

n, c = map(int, input().split())

li = map(int, input().split())

dic = {}

for i in li:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1

sorted_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)

for i in sorted_dic:
    print((str(i[0])+" ") * i[1], end="")
