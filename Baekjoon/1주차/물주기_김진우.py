import sys
input = sys.stdin.readline

n, k, a, b = map(int, input().split())
#6 3 2 2
#n개의 화분 
#초기 k만큼의 수분 

date = 0
li = [] #화분
for i in range(n):
    li.append(k)


while 0 not in li:
    for i in range(a):
        li[i] += b
    for i in range(n):
        li[i] -= 1
    li.sort()
    date += 1

print(date)
