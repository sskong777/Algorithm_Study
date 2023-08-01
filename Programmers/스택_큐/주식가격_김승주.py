'''
주석을 지워야 효율성 통과!
더 효율적으로 풀 수 있는 방법이 있을 듯 함! 다시 풀어보기!
'''
def solution(prices): 
    answer = []
    for i in range(len(prices)):
        count = 1
        for j in range(i+1, len(prices)): 
            if prices[i] > prices[j]: # 가격이 떨어진 경우
                answer.append(count)
                break
            if j == len(prices)-1: # 가격이 끝까지 안떨어진 경우 
                answer.append(count)
                break
            else: # 가격이 안떨어진 경우
                count+=1
    answer.append(0) 
    return answer