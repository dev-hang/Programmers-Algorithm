def dfs(v, visited, graph):
    cnt = 1
    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            cnt += dfs(node, visited, graph)

    return cnt

def divide_power_grid_in_two(n, wires):
    answer = 1e9
    graph = [[] for _ in range(n+1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(len(wires)):
        visited = [False] * (n+1)
        v1, v2 = wires[i]
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        left = dfs(v1, visited, graph)
        right = dfs(v2, visited, graph)

        graph[v1].append(v2)
        graph[v2].append(v1)

        answer = min(answer, abs(left-right))

    return answer







print(divide_power_grid_in_two(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) # result = 3
print(divide_power_grid_in_two(4, [[1,2],[2,3],[3,4]])) # result = 0
print(divide_power_grid_in_two(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) # result = 1