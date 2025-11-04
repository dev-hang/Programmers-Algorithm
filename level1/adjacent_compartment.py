def adjacent_compartment(board, h, w):
    answer = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]

    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if 0 <= nh < len(board) and 0 <= nw < len(board):
            if board[h][w] == board[nh][nw]:
                answer += 1

    return answer




print(adjacent_compartment([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
# result = 2
print(adjacent_compartment([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]],0,1))
# result = 1