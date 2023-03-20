
import sys
input = sys.stdin.readline

numbers = list(map(int,input().split()))

min_num = 1

while 1:
    count = 0
    for number in numbers:
        if min_num % number == 0 :
            count+=1
    if count >= 3:
        print(min_num)
        break
    min_num+=1