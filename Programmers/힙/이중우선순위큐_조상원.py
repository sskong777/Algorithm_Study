from heapq import heappush, heappop

def solution(operations):
    # 전체 리스트에서 큰 값 반
    minh = []
    # 전체 리스트에서 작은 값 반
    maxh = []

    for w in operations:
        command, num = w.split(' ')
        num = int(num)
        if command == 'I':
            heappush(maxh, -num)
            heappush(minh, num)
        elif command == 'D' and num == 1:
            if minh and maxh:
                rem = -heappop(maxh)
                print('D  1', rem)
                minh.remove(rem)
        elif command == 'D' and num == -1:
            if minh and maxh:
                rem = -heappop(minh)
                print('D  -1', rem)
                maxh.remove(rem)
        
        # print('minh', minh)
        # print('maxh', maxh)
        # print('===================================')
    ret = []
    
    if maxh:
        ret.append(-heappop(maxh))
    else:
        ret.append(0)
    if minh:
        ret.append(heappop(minh))
    else:
        ret.append(0)
    return ret



