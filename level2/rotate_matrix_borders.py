def rotate_matrix_borders(rows, columns, queries):
    answer = []
    arr = [[i + j for i in range(1, columns + 1)] for j in range(0, columns * rows, columns)]

    for query in queries:
        min_value = []
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        for i in range(x1, x2):
            arr[i][y1], arr[i + 1][y1] = arr[i + 1][y1], arr[i][y1]
            min_value.append(arr[i][y1])
            min_value.append(arr[i + 1][y1])
        for i in range(y1, y2):
            arr[x2][i], arr[x2][i + 1] = arr[x2][i + 1], arr[x2][i]
            min_value.append(arr[x2][i])
            min_value.append(arr[x2][i + 1])
        for i in range(x2, x1, -1):
            arr[i][y2], arr[i - 1][y2] = arr[i - 1][y2], arr[i][y2]
            min_value.append(arr[i][y2])
            min_value.append(arr[i - 1][y2])
        for i in range(y2, y1 + 1, -1):
            arr[x1][i], arr[x1][i - 1] = arr[x1][i - 1], arr[x1][i]
            min_value.append(arr[x1][i])
            min_value.append(arr[x1][i - 1])

        answer.append(min(min_value))

    return answer





print(rotate_matrix_borders(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # result = [8, 10, 25]
print(rotate_matrix_borders(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # result = [1, 1, 5, 3]
print(rotate_matrix_borders(100, 97, [[1,1,100,97]])) # result = [1]