from collections import deque

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def update_storage(n, m, graph):
    check = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    check[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
                if graph[nx][ny] == '0':
                    q.append((nx, ny))
                    check[nx][ny] = True
                elif graph[nx][ny] == '1':
                    q.append((nx, ny))
                    check[nx][ny] = True
                    graph[nx][ny] = '0'


def crane(n, m, container, graph):
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] == container:
                graph[i][j] = '1'

    update_storage(n, m, graph)


def lift(n, m, container, graph):
    tmp = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] == container:
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '0':
                        tmp.append((i, j))
                        break
    for ti, tj in tmp:
        graph[ti][tj] = '0'

    update_storage(n, m, graph)


def lift_and_crane(storage, requests):
    answer = 0
    n, m = len(storage) + 2, len(storage[0]) + 2
    graph = [['0'] * m for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            graph[i][j] = storage[i - 1][j - 1]

    for rqst in requests:
        if len(rqst) == 1:
            lift(n, m, rqst, graph)
        elif len(rqst) == 2:
            crane(n, m, rqst[0], graph)

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if graph[i][j] not in ['0', '1']:
                answer += 1

    return answer


print(lift_and_crane(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"])) # result = 11
print(lift_and_crane(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"])) # result = 4