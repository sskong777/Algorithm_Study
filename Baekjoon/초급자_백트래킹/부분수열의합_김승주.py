'''
n 개의 정수로 이루어진 수열
부분 수열 중 그 수열의 원소를 모두 더한 값이 s 가 되는 경우의 수 구하기 
'''

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

count =0

def back(idx,nSum):
    global count
    if idx >=n :
        return
    
    tmp = nSum + numbers[idx]

    if tmp == s:
        count +=1
    
    back(idx+1, nSum+numbers[idx]) # 현재꺼 선택한 경우
    back(idx+1, nSum)

back(0, 0)
print(count)