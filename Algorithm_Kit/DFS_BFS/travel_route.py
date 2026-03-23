def travel_route(tickets):
    answer = []
    visited = [False for _ in range(len(tickets))]

    def dfs(start, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for i in range(len(tickets)):
            if tickets[i][0] == start and not visited[i]:
                visited[i] = True
                dfs(tickets[i][1], path + [tickets[i][1]])
                visited[i] = False

    dfs('ICN', ['ICN'])
    answer.sort()

    return answer[0]




print(travel_route([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# result = ["ICN", "JFK", "HND", "IAD"]
print(travel_route([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# result = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]