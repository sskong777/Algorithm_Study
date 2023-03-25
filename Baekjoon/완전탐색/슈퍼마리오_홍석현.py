arr = [int(input()) for _ in range(10)]

ssum = 0
for i in arr:
    if abs(100-ssum) < abs(100-(ssum+i)):
        break
    ssum += i
print(ssum)
