def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            idx, _ = stack.pop()
            answer[idx] = i - idx
        stack.append([i, prices[i]])
        
    for i, _ in stack:
        answer[i] = len(prices) - 1 - i
    return answer