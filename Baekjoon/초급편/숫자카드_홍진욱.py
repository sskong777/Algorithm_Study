n = int(input())
cards = set(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
