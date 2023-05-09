import sys

input = sys.stdin.readline

n=int(input())

stack_list=[int(input()) for _ in range(n)]

see=stack_list.pop()
count=1
for i in range(n-1):
    num=stack_list.pop()
    if num>see:
        see=num
        count+=1
print(count)
