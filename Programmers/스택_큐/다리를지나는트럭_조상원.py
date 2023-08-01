from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    d = deque([0]*bridge_length)
    tw = deque(truck_weights)
    # 시간 time
    t = 0
    # 무게 총합 sum
    s = 0
    
    while d:
        # 다리에서 나온 트럭 또는 0
        w = d.popleft()
        # 총합에서 빼기
        s -= w
        # 시간은 + 1
        t+=1
        # 아직 추가해야할 트럭이 남아있을경우
        if tw:
            # 다리에 트럭을 추가할 수 있는지 확인
            if tw[0] + s <= weight:
                l = tw.popleft()
                s += l
                d.append(l)
            else:
                # 다리에 추가할 수 없으면 앞으로 한칸씩 밀기
                d.append(0)
        # print('========================================')
        # print('tw', tw)
        # print('d', d)

    return t 