from collections import defaultdict
import heapq

def choose_hiking_course(n, paths, gates, summits):
    summits.sort()
    summits_set = set(summits)
    graph = defaultdict(list)

    for i, j, k in paths:
        graph[i].append((k, j))
        graph[j].append((k, i))

    q = []
    visited = [10000001] * (n + 1)

    for gate in gates:
        heapq.heappush(q, (0, gate))
        visited[gate] = 0

    while q:
        intensity, node = heapq.heappop(q)

        if node in summits_set or intensity > visited[node]:
            continue

        for w, n_node in graph[node]:
            n_intensity = max(intensity, w)
            if n_intensity < visited[n_node]:
                visited[n_node] = n_intensity
                heapq.heappush(q, (n_intensity, n_node))

    min_intensity = [0, 10000001]

    for summit in summits:
        if visited[summit] < min_intensity[1]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]

    return min_intensity



print(choose_hiking_course(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
# result = [5, 3]
print(choose_hiking_course(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
# result = [3, 4]
print(choose_hiking_course(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
# result = [5, 1]
print(choose_hiking_course(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
# result = [5, 6]