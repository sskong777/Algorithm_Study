def solution(answers):
    p1 = [1,2,3,4,5] * 2000 # 10000 길이에 해당하는 패턴 전부 생성
    p2 = [2,1,2,3,2,4,2,5] * 1250
    p3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    answer = [0]*3
    for i,x,y,z in zip(answers, p1, p2, p3):
        answer[0] += i==x
        answer[1] += i==y
        answer[2] += i==z
    return [i+1 for i, a in enumerate(answer) if a == max(answer)]