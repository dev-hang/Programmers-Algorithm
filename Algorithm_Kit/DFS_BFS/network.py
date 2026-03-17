from collections import deque


def network(n, computers):
    answer = 0
    visited = [False] * n
    graph = {i: [] for i in range(n)}
    q = deque()
    q.append(0)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)

    while q:
        cur = q.popleft()
        if not visited[cur]:
            visited[cur] = True
            q.extend(graph[cur])
        if not q:
            for i in graph:
                if not visited[i]:
                    q.append(i)
                    break
            answer += 1

    return answer




print(network(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # result = 2
print(network(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # result = 1