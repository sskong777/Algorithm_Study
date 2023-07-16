from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    total = 0
    queue = deque([])
    truck_weights = deque(truck_weights)
    
    cur = 1

    while True:
        while True:
            if len(queue) == 0:
                break
            
            if queue[0][1] == cur:
                total -= queue[0][0]
                queue.popleft()
                break
            elif queue[0][1] != cur:
                break
        
        
        if len(truck_weights) > 0:
            if truck_weights[0] + total <= weight:
                total += truck_weights[0]
                queue.append([truck_weights.popleft(), cur + bridge_length])
        if len(truck_weights) == 0 and len(queue) == 0:
            break

        
        cur += 1
        
    answer = cur
    return answer