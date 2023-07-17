from collections import deque
def solution(priorities, l):
    d = deque(priorities)
    find = d[l]
    tot = 0
    while d:
        # 실행해야할 최고 우선순위
        lvl = max(d)
        # 체크해야할 프로세스
        c = d.popleft()
        # 위치 한칸 앞으로
        l -= 1
        # 총 프로세스 일단 + 1
        tot += 1
        
        # 우리 프로세스 중요도랑 최고 우선순위가 일치하면
        if c == lvl:
            # 우리가 찾는 프로세스가 출력되었고 중요도가 일치하면
            if l == -1 and c == find:
                return tot
        else:
            # 우선순위가 낮으면 다시 뒤로 추가
            d.append(c)
            # 프로세스 끝낸게 아니니까 다시 tot + 1
            tot -= 1
            # 만약 우선순위가 아닌데 우리 프로세스가 출력된 경우
            # 위치는 뒤로 다시 길이로
            if l == -1:
                l = len(d)-1
        # print(d)
        # print('l ',l, 'lvl ', lvl, 'tot ', tot)
    return tot
        
            
                
                
            