def triangular_snail(n):
    answer = []
    arr = [[0] * n for _ in range(n)]
    dr, dc = [1, 0, -1], [0, 1, -1]
    i, j, k, d = 0, 0, 0, 0

    if n < 2: return [1]

    while arr[i][j] == 0:
        k += 1
        arr[i][j] = k
        ni, nj = i + dr[d], j + dc[d]

        if ni >= n or nj >= n or arr[ni][nj] != 0:
            d = (d + 1) % 3
            i += dr[d]
            j += dc[d]
        else:
            i, j = ni, nj

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                answer.append(arr[i][j])

    return answer



print(triangular_snail(4)) # result = [1,2,9,3,10,8,4,5,6,7]
print(triangular_snail(5)) # result = [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(triangular_snail(6)) # result = [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]