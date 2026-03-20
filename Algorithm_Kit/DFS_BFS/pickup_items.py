from collections import deque


def pickup_items(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    path = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    path[i][j] = 0
                elif path[i][j] != 0:
                    path[i][j] = 1

    q = deque([[characterX * 2, characterY * 2]])

    while q:
        cx, cy = q.popleft()

        if cx == itemX * 2 and cy == itemY * 2:
            return visited[cx][cy] // 2

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if path[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[cx][cy]
                q.append([nx, ny])

    return answer


print(
    pickup_items([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
)  # result = 17
print(
    pickup_items([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
)  # result = 11
print(pickup_items([[1, 1, 5, 7]], 1, 1, 4, 7))  # result = 9
print(pickup_items([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))  # result = 15
print(
    pickup_items([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3)
)  # result = 10
