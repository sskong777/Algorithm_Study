n = int(input())

li = list(map(int, input().split()))

v = 0

for i in li:
    v = 1-(1-v)*(1-(i/100))
    print(round(v*100, 6))
