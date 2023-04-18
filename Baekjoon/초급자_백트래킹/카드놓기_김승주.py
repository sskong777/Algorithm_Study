
import sys
input = sys.stdin.readline

n  = int(input()) # 총 카드 수 
k = int(input()) # 선택하는 카드의 개수

cards = [ input().rstrip() for _ in range(n)]

ans = set() # 중복을 제거하고 봐야 하므로 set 사용 

visited =[False] * n 
def back(makeNum, dep):
    
    if dep == k :
        ans.add(makeNum)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            back(makeNum+cards[i], dep+1)
            visited[i] = False

back('', 0)
print(len(ans))

# 메모리 : 31768KB  / 속도 : 44ms

'''

다른 풀이 방법 :  permutation 으로 풀어보기 

from itertools import permutations
n, k , *a = map(int, open(0))
print(len({"".join(map(str,p)) for p in permutations(a,k)}))


'''
