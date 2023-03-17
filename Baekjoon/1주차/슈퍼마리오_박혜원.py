list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list = [40, 40, 40, 40]
list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# # 순서대로 더하면서 100보다 가까운지를 비교해나기
list = []
for i in range(10):
    list.append(int(input()))

score, cursor = 0, 0

while True:
    score += list[cursor]
    try:
        if abs(100 - (score + list[cursor+1])) > 100 - score:
            break
    except:
        break
    cursor += 1

print(score)
