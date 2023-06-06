from collections import deque

s = deque(list(input()))
kor = deque(list("KOREA"))
yon = deque(list("YONSEI"))

while kor and yon:
    letter = s.popleft()
    if letter == kor[0]:
        kor.popleft()
    if letter == yon[0]:
        yon.popleft()
    if not kor:
        print("KOREA")
        break
    elif not yon:
        print("YONSEI")
        break

