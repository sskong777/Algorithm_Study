# [10250] ACM호텔
# 호텔의 층 수(H), 각 층의 방 수(W), 몇 번째 손님(N)

num = int(input())

answers = []
for _ in range(num):
    H, W, N = map(int, input().split())
    if N % H == 0:
        answers.append(H*100 + (N // H))
    else:
        answers.append(((N % H))*100 + ((N // H)+1))


for answer in answers:
    print(answer)
