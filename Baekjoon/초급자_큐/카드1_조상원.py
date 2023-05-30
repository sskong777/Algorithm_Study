from collections import deque

n = int(input())

q = deque([i for i in range(1, n+1)])

i = 1
ret = []
while len(q) > 1:    
    isThrow = i % 2
    if isThrow:
        ret.append(q.popleft())
    else:
        q.append(q.popleft())
    i+=1
ret.append(q[0])
print(' '.join(map(str, ret)))