def light_path_cycle(grid):
    answer = []
    n, m = len(grid), len(grid[0])
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                if not visited[i][j][k]:
                    cnt = 0
                    x, y, d = i, j, k

                    while True:
                        visited[x][y][d] = True
                        x = (x+dx[d]) % n
                        y = (y+dy[d]) % m
                        cnt += 1

                        if grid[x][y] == 'S':
                            d = d
                        elif grid[x][y] == 'L':
                            d = (d + 1) % 4
                        elif grid[x][y] == 'R':
                            d = (d + 3) % 4

                        if visited[x][y][d]:
                            answer.append(cnt)
                            break
    return sorted(answer)




print(light_path_cycle(["SL","LR"])) # result = [16]
print(light_path_cycle(["S"])) # result = [1,1,1,1]
print(light_path_cycle(["R","R"])) # result = [4,4]