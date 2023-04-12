import sys
input = sys.stdin.readline

def findPos(pos, p):
    s = 0
    e = len(pos) - 1
    m = 0
    
    while s <= e:
        m = (s + e) // 2
        
        if pos[m] == p:
            return True
        elif pos[m] > p:
            e = m - 1
        elif pos[m] < p:
            s = m + 1
    return False

n = int(input())
a, b = map(int, input().split())

pos = [list(map(int, input().split())) for _ in range(n)]

pos = sorted(pos, key = lambda x : (x[0], x[1]))
answer = 0
for p1 in pos:
    x, y = p1
    
    p2 = [x+a, y]
    p3 = [x, y+b]
    p4 = [x+a, y+b]

    if findPos(pos, p2) and findPos(pos, p3) and findPos(pos, p4):
        answer += 1

print(answer)

'''
set 쓰면 in 연산 쓰면 O(1) 로 가능
'''