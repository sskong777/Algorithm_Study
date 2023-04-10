import sys 
from collections import defaultdict
t = int(input())
input = sys.stdin.readline

for test in range(t):
    n = int(input())

    dots = sorted(list(map(int,input().split())))
    dotdict = defaultdict(int)

    for dot in dots:
        dotdict[dot] =1
        
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            start = dots[i]
            mid = dots[j]
            end = (mid*2)-start
            if dotdict[end] == 1:
                count+=1

    print(count)