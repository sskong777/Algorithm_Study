import sys

input = sys.stdin.readline

num = int(input())


check = [int(input()) for _ in range(num)]
s=[]
pointer=1
ret = []
isno = 0
for c in check:

    while pointer <= c:
        s.append(pointer)
        # print('+')
        ret.append('+')
        pointer+=1
    if s[-1] == c:
        # print('-')
        ret.append('-')
        s.pop()
        continue
    # if c < pointer:
    else:
        isno=1
        break

if isno:
    print('NO')
else:
    for l in ret:
        print(l)    
