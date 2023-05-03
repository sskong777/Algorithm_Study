# [12605] 단어순서 뒤집기

n = int(input())

sentence = []
answer = []
for _ in range(n):
    words = input().split(" ")
    sentence.append(words)  # this is a test -> ["this", "is",  "a",  "test"]

# print(sentence)
for i, words in enumerate(sentence):  # 출력 형식이 Case #1 -> 문장의 인덱스(i) 필요해서
    stack = []
    for word in words:
        stack.append(word)

    answer = []
    while stack:
        answer.append(stack.pop())
    print(f"Case #{i + 1}: {' '.join(answer)}")
    # print(f"Case #{i + 1}:  {answer}")
    # print(*answer)
