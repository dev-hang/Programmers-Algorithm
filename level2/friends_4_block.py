def friends_4_block(m, n, board):
    answer = 0
    delete = set()
    board = [list(blocks) for blocks in board]

    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                if not board[i][j]:
                    continue

                if board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][
                    j + 1]:
                    delete.add((i, j))
                    delete.add((i, j + 1))
                    delete.add((i + 1, j))
                    delete.add((i + 1, j + 1))

        if delete:
            answer += len(delete)
            for i, j in delete:
                board[i][j] = 0
            delete = set()
        else:
            break

        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and not board[i + 1][j]:
                        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                        moved = 1
            if moved == 0:
                break

    return answer



print(friends_4_block(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # result = 14
print(friends_4_block(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # result = 15

