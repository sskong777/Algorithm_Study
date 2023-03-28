import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = ['1','2','3','4','5','6','7','8','9']

all_numbers = list(permutations(nums,3))

for i in range(n): # 테스트 개수 만큼
    number, s, b = map(int,input().split()) # 넘버 받아오고
    number = list(str(number))
    rcount =0
    for j in range(len(all_numbers)): # 모든 경우의 수 
        ball, strike = 0,0
        j = j - rcount # 아래에서 제거되면 다음 j의 위치가 변경됨.
        for k in range(3):
            if number[k] == all_numbers[j][k]:
                strike +=1
            elif all_numbers[j][k] in number:
                ball+=1
        if ball !=b or strike !=s:
            all_numbers.remove(all_numbers[j])
            rcount +=1
                
print(len(all_numbers))