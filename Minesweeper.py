def updateBoard(board, click):

    if not board:
        return []

    m, n = len(board), len(board[0])
    i, j = click[0], click[1]    
    print(board[i][j]) 

    if board[i][j] == 'M':
        board[i][j] = 'X'
        return board

    dfs(board, i, j)

    return board

def dfs(board, i, j):

    if board[i][j] != 'E':
        return
    print(board[i][j])
    m, n = len(board), len(board[0])       
    directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
    mine_count = 0

    for d in directions:
        print(i,j,d[0],d[1])
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':        
            mine_count += 1

    if mine_count == 0:
        board[i][j] = 'B'
    else:
        board[i][j] = str(mine_count)
        return

    for d in directions:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < m and 0 <= nj < n:
            dfs(board, ni, nj)


       

board =  [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]

click = [3,0]
print(updateBoard(board,click))

# "B","1","E","1","B"
# "B","1","M","1","B"
# "B","1","1","1","B"
# "B","B","B","B","B"
