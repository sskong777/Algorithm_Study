def solution(prices):
    ret = []
    
    for i in range(len(prices)):
        t = 0 # 시간
        for j in range(i+1, len(prices)):
            t+=1
            # 다음 주식 값이 현재 주식값보다 떨어진 경우
            if prices[j] < prices[i]:
                break
        ret.append(t)

        
    return ret