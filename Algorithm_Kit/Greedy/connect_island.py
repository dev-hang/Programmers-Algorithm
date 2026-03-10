def connect_island(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    link = set([costs[0][0]])

    while len(link) != n:
        for a, b, c in costs:
            if a in link and b in link:
                continue
            if a in link or b in link:
                link.update([a, b])
                answer += c
                break

    return answer




print(connect_island(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # result = 4