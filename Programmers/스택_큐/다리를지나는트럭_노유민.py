from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    bridge = deque(bridge)
    truck_weights = deque(truck_weights)
    bridgeWeight = 0
    while bridge:
        answer += 1
        delWeight = bridge.popleft()
        bridgeWeight -= delWeight
        if truck_weights:
            if bridgeWeight + truck_weights[0] <= weight:
                newWeight = truck_weights.popleft()
                bridge.append(newWeight)
                bridgeWeight += newWeight
            else:
                bridge.append(0)
    return answer
