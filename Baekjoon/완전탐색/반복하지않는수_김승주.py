import sys
input = sys.stdin.readline

from itertools import permutations

numbers = [0,1,2,3,4,5,6,7,8,9]
while True:
    n = int(input())
    if n == 0:
        break
    count =0
    p_count = 0
    check =False
    while True:
        for i in range(1,10):
            nums = [item for item in numbers if item != i]
            for j in permutations(nums,p_count):
                count+=1
                if count == n:
                    print(''.join(str(x) for x in [i]+ list(j)))
                    check = True
            if check:
                break
        p_count+=1
        if check :
            break

