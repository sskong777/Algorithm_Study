import sys
input = sys.stdin.readline

tc = int(input())
for case in range(tc):
    input()
    r, c = map(int, input().strip().split())

    box = []
    candy1 = [">", "o", "<"]
    candy2 = ["v", "o", "^"]
    for _ in range(r):
        box.append(list(input().strip()))

    candy_cnt = 0
    for i in range(r):
        for j in range(c):
            if box[i][j] == ">":
                if i < r and j+1 < c and box[i][j+1] == "o":
                    if i < r and j+2 < c and box[i][j+2] == "<":
                        candy_cnt += 1
            elif box[i][j] == "v":
                if i+1 < r and j < c and box[i+1][j] == "o":
                    if i+2 < r and j < c and box[i+2][j] == "^":
                        candy_cnt += 1

    print(candy_cnt)