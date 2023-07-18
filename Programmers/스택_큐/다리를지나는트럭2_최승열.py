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
            movement = 1 # 움직임은 1
        else:
            # weight가 없다면, 가장 앞에 있는 트럭을 기준으로 도착지점까지 이동하는데 걸리는 시간을 계산
            movement = bridge_length - dq[0][1] 
        
        # 모든 트럭을 movement만큼 이동
        for t in dq:
            t[1] += movement
        
        # 앞에 있는 트럭이 도착했다면, pop
        if dq and dq[0][1] >= bridge_length:
            weight_sum -= dq.popleft()[0]
            passed += 1
        
        time += movement
        
    return time