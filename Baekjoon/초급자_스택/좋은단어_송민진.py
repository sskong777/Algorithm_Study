# # 시도 1 - 오답
# import sys
# input = sys.stdin.readline
#
# cnt = 0
# n = int(input())
# for _ in range(n):
#     valid = True
#     word = list(input().strip())
#     pending = ""
#     if len(word) % 2 != 0:
#         continue
#     while len(word) > 1:
#         if word[-1] == word[-2]:
#             word.pop()
#             word.pop()
#         elif pending == "":
#             pending = word.pop()
#         elif pending != "":
#             if pending == word[-1]:
#                 word.pop()
#                 pending = ""
#             else:
#                 valid = False
#                 break
#     if valid and len(word) == 1 and pending == word[0]:
#         word.pop()
#
#     if len(word) == 0:
#         cnt += 1
#
# print(cnt)

# # 시도 2 -  시간 초과
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# cnt = 0
# for _ in range(n):
#     word = list(input().strip())
#     length = len(word)
#
#     if len(word) % 2 != 0:
#         continue
#
#     iter = 0
#     while word and iter < length:
#         iter += 1
#         for i in range(len(word)-1):
#             if word[i] == word[i+1]:
#                 word.pop(i+1)
#                 word.pop(i)
#                 break
#     if not word:
#         cnt += 1
#
# print(cnt)

# 시도 3
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
stack = []

for _ in range(n):
    word = input().strip()
    for letter in word:
        if not stack or stack[-1] != letter:
            stack.append(letter)
        else:
            stack.pop()
    if not stack:
        cnt += 1
    stack = []

print(cnt)