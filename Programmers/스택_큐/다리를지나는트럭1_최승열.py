from collections import deque

def solution(bridge_length, weight, truck_weights):
    time, passed, pt, weight_sum = 1, 0, 0, 0 # 트럭 탑승은 시간 1부터 시작
    dq = deque()
    
    while passed < len(truck_weights):
        # if (다리에 탑승안한 트럭이 있거나) and (weight가 충분히 남아있을 때)
        if pt < len(truck_weights) and weight_sum + truck_weights[pt] <= weight:
            weight_sum += truck_weights[pt] 
            dq.append([truck_weights[pt], 0])
            pt += 1
        
        # 모든 트럭을 1만큼 이동
        for t in dq:
            t[1] += 1
        
        # 앞에 있는 트럭이 도착했다면, pop
        if dq and dq[0][1] >= bridge_length:
            weight_sum -= dq.popleft()[0]
            passed += 1
        
        time += 1
        
    return time