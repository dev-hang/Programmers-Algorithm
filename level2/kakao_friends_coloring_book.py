from collections import deque

def kakao_friends_coloring_book(m, n, picture):
    answer = [0, 0]
    visited = [[False] * n for _ in range(m)]
    result = []

    def bfs(x, y):
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        cnt = 1
        q = deque()
        q.append([x, y])
        visited[x][y] = True

        while q:
            a, b = q.popleft()
            for d in range(4):
                na = a + dx[d]
                nb = b + dy[d]

                if 0 <= na < m and 0 <= nb < n:
                    if not visited[na][nb] and picture[a][b] == picture[na][nb]:
                        visited[na][nb] = True
                        q.append([na, nb])
                        cnt += 1

        result.append(cnt)

    for i in range(m):
        for j in range(n):
            if picture[i][j] and not visited[i][j]:
                bfs(i, j)

    answer[0] = len(result)
    answer[1] = max(result)

    return answer



print(kakao_friends_coloring_book(6, 4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]))
# result = [4, 5]