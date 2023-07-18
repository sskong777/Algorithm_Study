def DFS(x):
    if x > 0:
        # print(x, end=" ") # 3 2 1
        DFS(x-1)
        print(x, end=" ") # 1 2 3

n = int(input()) # 3
DFS(n)

'''
매개변수
지역변수
복귀 주소
=> 스택 프레임
 
'''