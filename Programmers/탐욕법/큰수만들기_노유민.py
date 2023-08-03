# 이중 while문으로 탐색 4문제 시간초과
def solution(number, k):
    answer = '' 
    for i in number:
        while k>0 and answer and answer[-1]<i:
            answer = answer[:-1]
            k-=1
        answer+=i
    return answer[:len(number)-k]