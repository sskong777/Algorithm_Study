
import sys
input = sys.stdin.readline

n = int(input())
candidate = [ int(input()) for _ in range(n)]

if n ==1:
    print(0)
    exit()

count =0
while 1:
    if candidate.index(max(candidate))== 0:
        if candidate.count(max(candidate))!=1:
            print(count+1)
        else:
            print(count)
        exit()
    else:
        candidate[candidate.index(max(candidate))]-=1
        candidate[0]+=1
        count+=1