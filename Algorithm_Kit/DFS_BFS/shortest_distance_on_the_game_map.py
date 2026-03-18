from collections import deque

def shortest_distance_on_the_game_map(maps):
    m, n = len(maps), len(maps[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    q = deque([(0,0)])
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<m and 0<=ny<n and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

    if maps[m-1][n-1] == 1:
        return -1

    return maps[m-1][n-1]





print(shortest_distance_on_the_game_map([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # result = 11
print(shortest_distance_on_the_game_map([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # result = -1