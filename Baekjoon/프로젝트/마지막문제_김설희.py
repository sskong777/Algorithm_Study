import sys

n = int(sys.stdin.readline())
test = list(map(int, sys.stdin.readline().split()))

test.sort()

All = [i for i in range(test[0] + 1, test[-1]) if i not in test]

print(test)
print(All)

result = []
realresult = []
for i in All:
    for j in test:
        result.append(abs(i-j))
    realresult.append(min(result))
    result = []

check = False # realresult 안에 모든 요소가 같을 경우 체크

if len(realresult) == 0:
    print(-1)
else:
    for i in range(len(realresult)-1):
        if realresult[i] < realresult[i+1]:
            print(All[i+1])
            check = True
            break

if check == False and len(realresult) > 0:
    print(All[0])

