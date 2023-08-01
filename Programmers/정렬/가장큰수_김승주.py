
def solution(numbers):
    tmp = list(map(str, numbers))
    tmp = sorted(tmp, key=lambda x: x * 3, reverse=True) # number가 1000 이하 숫자
    return str(int(''.join(tmp)))


'''
시간 초과 발생 -> 테케 / 일부 통과 
from itertools import permutations # 순열
def solution(numbers):
    answer= []
    for x in list(permutations(numbers)):
        ans =''
        for y in x:
            ans+=str(y)
        answer.append(int(ans))
    return str(max(answer))

'''