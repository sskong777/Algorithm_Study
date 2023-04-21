n = int(input())

answer = 0
board = [-1] * n

def is_possible(row):
    for checking in range(row):
        if board[checking] == board[row] or abs(board[checking] - board[row]) == abs(checking - row):
            return False
    return True

def dfs(row):
    global answer

    if row == n:
        answer += 1
        return

    for col in range(n):
        board[row] = col
        if is_possible(row):
            dfs(row+1)

dfs(0)

print(answer)