import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

a_card = list(map(int, input().split()))
b_card = list(map(int, input().split()))
c_card = list(map(int, input().split()))

a_card.sort()
b_card.sort()
c_card.sort()
answer = 1000000000

def isNearest(mid, near, target):
    if abs(mid - target) < abs(near - target):
        return True
    
    return False
    

def searchNum(target, card):
    s = 0
    e = len(card) - 1
    m = (s + e) // 2
    near = card[m]
    
    while s <= e:
        m = (s + e) // 2
        if card[m] == target:
            return target
        
        if card[m] < target:
            s = m + 1
        elif card[m] > target:
            e = m - 1
        
        if isNearest(card[m], near, target):
            near = card[m]
    
    return near

for a_n in a_card:
    b_n = searchNum(a_n, b_card)
    c_n1 = searchNum(a_n, c_card)
    c_n2 = searchNum(b_n, c_card)
    
    score1 = abs(max(a_n, b_n, c_n1) - min(a_n, b_n, c_n1))
    score2 = abs(max(a_n, b_n, c_n2) - min(a_n, b_n, c_n2))
    
    answer = min(answer, min(score1, score2))

print(answer)
