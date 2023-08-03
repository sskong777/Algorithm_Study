#deque를 이용한 rotate 방법 실패
def solution(name):
    answer = 0
    _len=len(name)
    #한방향으로 쭉갔을때를 설정
    min_length = _len-1
    
    #각 순번에서 A의 위치를 찾고 그 위치에서 -> <- 로 진행할지 <- -> 로 진행할지 최소값 찾기
    for idx, char in enumerate(name):
        #A부터 가는게 작을지 Z부터 가는게 작을지 위아래 선택
        answer+=min((ord(char) - ord('A')),(ord('Z')-ord(char)+1))
        
        #A찾기(연속된값이 있을수 있으니 while 사용)
        _next = idx+1
        while _next<_len and name[_next]=='A':
            _next+=1
        #A찾은 위치에서 idx를 왔다갔다 한것에서 뒤로 돌아간 길이/ 뒤로 먼저 가서 다시 앞으로 돌아오는 길이 비교
        min_length = min(min_length, 2*idx+_len-_next,2*(_len-_next)+idx)
        
    answer+=min_length
    
    
    return answer
