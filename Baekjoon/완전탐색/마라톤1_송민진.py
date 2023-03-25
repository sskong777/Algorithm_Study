import sys
input = sys.stdin.readline

n = int(input())
answer = 0

points = []
for idx in range(n):
    points.append(list(map(int, input().split())))

def calc_gap(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

def calc_diff(idx):
    return (calc_gap(points[idx], points[idx-1]) + calc_gap(points[idx], points[idx+1])) - calc_gap(points[idx+1], points[idx-1])

max_diff = 0
for i in range(1, n-1):
    diff = calc_diff(i)
    max_diff = max(max_diff, diff)

for j in range(1, n):
    answer += calc_gap(points[j], points[j-1])

print(answer-max_diff)