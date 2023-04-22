
'''
치킨 거리
치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리 
도시의 치킨 거리는 모든 집의 치킨 거리의 합

도시에 있는 치킨 집 중에서 최대 m 개를 고르고 나머지 치킨집은 모두 폐업 시킨다
도시의 친킨 거리가 가장 작게 되도록!
'''

# 백트래킹 
n, m = map(int,input().split())

house=[]
chick = []

# 치킨과 집 정보 저장
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1 : # 집
            house.append((i,j))
        elif tmp[j]==2: # 치킨집
            chick.append((i,j))

def calc(choosen): # 각 집별로 가장 가까운 치킨집 거리 다 더하기!
    ans = 0
    result = 0
    for h in house:
        result = int(1e9)
        for c in choosen:
            result = min(result,(abs(h[0]-c[0]) + abs(h[1]-c[1])))
        ans += result
    return ans

answer =int(1e9)
def back(depth,choosen,count):
    global answer
    if count ==m:# m개가 되었을 경우
        answer= min(answer, calc(choosen))
        return
    
    if depth == len(chick) : # 끝까지 왔는데 m 개 이상 못고른 경우
        return
    
    back(depth+1, choosen+[chick[depth]],count+1) # 현재 위치의 치킨집을 선택한 경우
    back(depth+1, choosen, count)  # 현재 위치의 치킨집을 선택하지 않은 경우 

back(0,[],0)
print(answer)