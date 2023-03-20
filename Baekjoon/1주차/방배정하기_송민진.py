a, b, c, n = map(int, input().split())

def solution():
    for roomc in range(n+1):
        for roomb in range(n+1):
            for rooma in range(n+1):
                if a*rooma + roomb*b + roomc*c == n:
                    return 1
    return 0

print(solution())