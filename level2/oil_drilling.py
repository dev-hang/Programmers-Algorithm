from collections import deque

def oil_drilling(land):
    m, n = len(land), len(land[0])
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[False for _ in range(n)] for _ in range(m)]
    result = [0 for _ in range(n)]

    def dfs(pos):
        q = deque()
        q.append(pos)
        x, y = pos
        visited[x][y] = True
        cnt = 1

        c_set = set()
        c_set.add(y)

        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < m and 0 <= ny < n and land[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
                    c_set.add(ny)

        for c in c_set:
            result[c] += cnt

    for i in range(m):
        for j in range(n):
            if land[i][j] == 1 and not visited[i][j]:
                dfs((i, j))

    return max(result)



print(oil_drilling([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
# result = 9
print(oil_drilling([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]	))
# result = 16
