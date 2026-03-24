def dfs(i, j, n, k, table, group):
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    if i < 0 or j < 0 or i >= n or j >= n:
        return
    if table[i][j] == k:
        table[i][j] = 1-k
        group.append([i, j])
        for d in range(4):
            dfs(i + dx[d], j + dy[d], n, k, table, group)

def spin(board):
    n, m = len(board), len(board[0])
    result = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = board[i][j]
    return result

def adjust(n, board, l):
    arr = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == l:
                group = []
                dfs(i, j, n, l, board, group)
                min_x = min(group, key=lambda x: x[0])[0]
                min_y = min(group, key=lambda x: x[1])[1]

                for k in range(len(group)):
                    group[k][0] -= min_x
                    group[k][1] -= min_y

                max_x = max(group, key=lambda x: x[0])[0]
                max_y = max(group, key=lambda x: x[1])[1]

                matrix = [[0 for _ in range(max_y+1)] for _ in range(max_x+1)]

                for x, y in group:
                    matrix[x][y] = 1

                arr.append(matrix)
    return arr

def fill_puzzle_pieces(game_board, table):
    answer = 0
    n = len(table)

    blocks = adjust(n, table, 1)
    empty_board = adjust(n, game_board, 0)

    for b in blocks:
        for s in empty_board:
            if len(b)*len(b[0]) == len(s)*len(s[0]):
                block = b
                find = False
                for _ in range(4):
                    if block == s:
                        for c in block:
                            answer += c.count(1)
                        s[0][0] = -1
                        find = True
                    else:
                        block = spin(block)
                if find:
                    break
    return answer




print(fill_puzzle_pieces([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
# result = 14
print(fill_puzzle_pieces([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))
# result = 0