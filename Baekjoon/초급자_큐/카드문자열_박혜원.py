# [13417] 카드문자열
from collections import deque
T = int(input())

for _ in range(T):
    num = int(input())  # 5
    cards = list(input().split())  # ['A', 'S ', 'D',  'F',  'G']
    # print(cards)

    q = deque()
    q.append(cards[0])
    standard = cards[0]  # 기준

    for i in range(1, num):

        if standard >= cards[i]:
            q.appendleft(cards[i])
            standard = cards[i]
        else:
            q.append(cards[i])

    print("".join(q))


"""
1. 문자열 합치는 join 함수

'(문자열을 이어주는 문자)'.join(리스트)

lst = ['K', 'C', 'E']

#1. 따닥따닥 붙여서 잇는 경우
print(''.join(lst)) #KCE

#2. 띄어쓰기로 잇는 경우
print(' '.join(lst)) #K C E
print(*q)
#3. 별로 잇는 경우
print('*'.join(lst)) #K*C*E
 """
