import sys
input = sys.stdin.readline

digits = [["###", "#.#", "#.#", "#.#", "###"],  # 0
          ["..#", "..#", "..#", "..#", "..#"],  # 1
          ["###", "..#", "###", "#..", "###"],  # 2
          ["###", "..#", "###", "..#", "###"],  # 3
          ["#.#", "#.#", "###", "..#", "..#"],  # 4
          ["###", "#..", "###", "..#", "###"],  # 5
          ["###", "#..", "###", "#.#", "###"],  # 6
          ["###", "..#", "..#", "..#", "..#"],  # 7
          ["###", "#.#", "###", "#.#", "###"],  # 8
          ["###", "#.#", "###", "..#", "###"]]  # 9
def check_possible(now, target):
    for i in range(5):
        for j in range(3):
            if now[i][j] != target[i][j] and now[i][j] == "#":
                return False
    return True

def convert(now_diode):
    for target_diode in digits:
        if now_diode == target_diode:
            return digits.index(target_diode)
        if check_possible(now_diode, target_diode):
            return digits.index(target_diode)

hhmm = [[] for _ in range(4)]
for _ in range(5):
    s = list(input().strip().split())
    for i in range(4):
        hhmm[i].append(s[i])

answer = ''
for h in range(2):
    answer += str(convert(hhmm[h]))
answer += ":"
for m in range(2, 4):
    answer += str(convert(hhmm[m]))

print(answer)