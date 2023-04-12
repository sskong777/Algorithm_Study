
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
trees = list(map(int, input().split()))


start = 1
end = max(trees)

while start <= end :
    mid = (start + end )//2
    t_sum = 0
    for tree in trees:
        if tree >mid :
            t_sum += (tree-mid)
    
    if t_sum >= m:
        start = mid +1
    else:
        end = mid -1
print(end)

