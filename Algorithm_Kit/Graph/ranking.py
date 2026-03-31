def ranking(n, results):
    answer = 0
    INF = 1e9
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for a, b in results:
        graph[a][b] = 1

    for a in range(n+1):
        for b in range(n+1):
            if a == b:
                graph[a][b] = 0

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

    for a in range(1, n+1):
        cnt = 0
        for b in range(1, n+1):
            if graph[a][b] != INF or graph[b][a] != INF:
                cnt += 1
        if cnt == n:
            answer += 1

    return answer


print(ranking(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) # result = 2