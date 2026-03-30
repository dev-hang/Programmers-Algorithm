from collections import deque

def furthest_node(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    q = deque([1])
    visited[1] = 1

    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = visited[node] + 1
                q.append(i)

    answer = visited.count(max(visited))

    return answer


print(furthest_node(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # result = 3