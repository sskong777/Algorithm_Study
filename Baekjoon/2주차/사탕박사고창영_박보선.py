t = int(input())

for i in range(t):
    candy_cnt = 0
    candy_box = []
    candy = 0
    blank = input()
    r, c = map(int, input().split())
    for j in range(r):
        candy = input()
        candy_box.append(list(candy))


    for k in range(r):
        for s in range(c):
            if candy_box[k][s] == '>':
                if s + 2 <= c-1:
                    candy = candy_box[k][s] + candy_box[k][s+1] + candy_box[k][s+2]
                    if candy == '>o<':
                        candy_cnt += 1
            if candy_box[k][s] == 'v':
                if k + 2 <= r-1:
                    candy = candy_box[k][s] + candy_box[k+1][s] + candy_box[k+2][s]
                    if candy == 'vo^':
                        candy_cnt += 1
    print(candy_cnt)