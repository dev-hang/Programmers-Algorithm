import heapq

def shared_taxi_fare(n, s, a, b, fares):
    answer = 1e9
    graph = [[] * (n+1) for _ in range(n+1)]

    for n1, n2, fare in fares:
        graph[n1].append((n2, fare))
        graph[n2].append((n1, fare))

    def dijkstra(s):
        hq = []
        distance = [1e9] * (n+1)
        heapq.heappush(hq, (0, s))
        distance[s] = 0

        while hq:
            ofare, cur = heapq.heappop(hq)

            if distance[cur] < ofare:
                continue

            for ds in graph[cur]:
                nfare = ofare + ds[1]
                if nfare < distance[ds[0]]:
                    distance[ds[0]] = nfare
                    heapq.heappush(hq, (nfare, ds[0]))

        return distance

    distance_list = [[]] + [dijkstra(i) for i in range(1, n+1)]

    for i in range(1, n+1):
        case = distance_list[s][i] + distance_list[i][a] + distance_list[i][b]
        answer = min(answer, case)

    return answer



print(shared_taxi_fare(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) # result = 82
print(shared_taxi_fare(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])) # result = 14
print(shared_taxi_fare(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])) # result = 18