from collections import deque


def solution(bridge_length, weight, truck_weights):
    s = 0
    in_bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    current_weight = 0

    while in_bridge:
        current_weight -= in_bridge.popleft()
        s += 1
        if trucks:
            # sum(in_bridge) 쓰니까 테케 5번에서 시간 초과남
            if current_weight + trucks[0] <= weight:
                current_weight += trucks[0]
                in_bridge.append(trucks.popleft())
            else:
                in_bridge.append(0)

    return s