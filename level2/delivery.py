import heapq

def dijkstra(distance, adj):
    hq = []
    heapq.heappush(hq, [0, 1])

    while hq:
        cost, node = heapq.heappop(hq)
        for c, n in adj[node]:
            if cost + c < distance[n]:
                distance[n] = cost + c
                heapq.heappush(hq, [cost+c, n])

def delivery(N, road, K):
    answer = []
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    adj = [[] for _ in range(N+1)]

    for a, b, c in road:
        adj[a].append([c, b])
        adj[b].append([c, a])

    dijkstra(distance, adj)

    for dis in distance:
        if dis <= K:
            answer.append(dis)

    return len(answer)




print(delivery(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))	# result = 4
print(delivery(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))	# result = 4