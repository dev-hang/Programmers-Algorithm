def crane_dolls_game(board, moves):
    answer = 0
    basket = []

    for move in moves:
        for i in range(len(board)):
            doll = board[i][move - 1]
            if doll > 0:
                if basket:
                    if basket[-1] == doll:
                        basket.pop()
                        answer += 2
                    else:
                        basket.append(doll)
                else:
                    basket.append(doll)
                board[i][move - 1] = 0
                break

    return answer



print(crane_dolls_game([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
# result = 4