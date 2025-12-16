def number_of_server_extension(players, m, k):
    answer = 0
    servers = [0] * len(players)

    for i in range(len(players)):
        if players[i] >= m and players[i] > servers[i] * m:
            cnt = players[i] // m - servers[i]
            for j in range(i, min(len(players), i + k)):
                servers[j] += cnt
            answer += cnt

    return answer




print(number_of_server_extension([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))
# result = 7
print(number_of_server_extension([0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0], 5, 1))
# result = 11
print(number_of_server_extension([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))
# result = 12