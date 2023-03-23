# [2503] 숫자 야구 (실버 3)
import sys
input = sys.stdin.readline

import itertools
per_list = list(map(''.join, itertools.permutations(list(map(str, range(1,10))), 3)))
per_list = list(set(map(int, per_list)))

N = int(input()) # 1~100
# 질문 세자리 수 / 영수 스트라이크 개수 / 볼의 개수
i_list = []
cnt=0
for n in range(N):
    i_list.append(list(map(int, input().split())))

for i in range(len(per_list)):
    tmp = list(str(per_list[i]))
    flag = 1
    for j in range(N):
        tmp2 = list(str(i_list[j][0]))
        s2, b2 = i_list[j][1], i_list[j][2]
        s, b = 0, 0
        for n in range(3):
            if tmp[n] == tmp2[n]:
                s+=1
            elif tmp2[n] in tmp:
                b+=1
        if s!=s2 or b!=b2:
            flag = 0
    
    if flag == 1:
        cnt += 1

print(cnt)