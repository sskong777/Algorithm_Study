
board = []

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, -1, 0, 1, 1, -1]

def count_omok(i,j):   
    for d in range(8):
        if board[i][j] =="X":
            count = 1
        else: # 0 또는 . 인 경우
            count =0
        if board[i][j]==".": # 놓을 수 있는 경우
            empty = 1
        else: # 놓지도 못하는 경우, 또는 이미 놓아져 있는 경우
            empty = 0
        
        start_x, start_y = i,j
        for k in range(4): # 4개 진행
            nx,ny = start_x + dx[d], start_y+dy[d]

            if 0<=nx<10 and 0<=ny<10:
                if board[nx][ny]=="X":
                    count+=1
                elif board[nx][ny]==".":
                    empty+=1
            else:
                break
            if empty > 1: # 더 놔야하는 경우가 1개 이상일 경우
                break
            start_x ,start_y= nx,ny
        
        # count 가 4 이상인 경우 중간에 o를 포함하고 있을 수 있으므로 empty가 무조건 1이어야
        # count 가 5 이상인 경우 empty는 0이어야 함!
        if (count >=4 and empty ==1) or (count>=5 and empty ==0):
            return True
    return False
        
for i in range(10):
    board.append(list(input()))

for i in range(10):
    for j in range(10):
        if count_omok(i,j):
            print(1)
            exit()
print(0)
