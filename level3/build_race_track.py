from collections import deque

def build_race_track(board):
    def bfs(start):
        N = len(board)
        visited = [[1e9 for _ in range(N)] for _ in range(N)]
        dx, dy = [1,0,-1,0], [0,1,0,-1]
        visited[0][0] = 0
        q = deque([start])
        while q:
            x, y, cost, d = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<N and not board[nx][ny]:
                    if i == d:
                        ncost = cost + 100
                    else:
                        ncost = cost + 600
                    if visited[nx][ny] > ncost:
                        visited[nx][ny] = ncost
                        q.append([nx, ny, ncost, i])
        return visited[N-1][N-1]

    return min(bfs((0,0,0,0)), bfs((0,0,0,1)))







print(build_race_track([[0,0,0],[0,0,0],[0,0,0]])) # result = 900
print(build_race_track([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])) # result = 3800
print(build_race_track([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])) # result = 2100
print(build_race_track([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])) # result = 3200