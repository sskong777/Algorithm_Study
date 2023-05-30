import sys

input = sys.stdin.readline

t, s = map(int, input().split())

isLunch = False
isAlc = False

if 12 <= t <= 16:
    isLunch = True

if s == 1:
    isAlc = True

if not isLunch or isAlc:
    print(280)
elif isLunch and not isAlc:
    print(320)
