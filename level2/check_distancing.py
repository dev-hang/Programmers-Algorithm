from itertools import combinations

def check_distancing(places):
    answer = [1] * len(places)

    for k in range(len(places)):
        person = []
        for i in range(len(places[k])):
            for j in range(len(places[k][i])):
                if places[k][i][j] == 'P':
                    person.append([i, j])

        for x, y in list(combinations(person, 2)):
            manhattan = abs(x[0] - y[0]) + abs(x[1] - y[1])
            if manhattan == 1:
                answer[k] = 0
                break

            elif manhattan == 2:
                min_r, min_c = min(x[0], y[0]), min(x[1], y[1])
                max_r, max_c = max(x[0], y[0]), max(x[1], y[1])

                for a in range(min_r, max_r + 1):
                    for b in range(min_c, max_c + 1):
                        if places[k][a][b] == 'O':
                            answer[k] = 0
                            break
                    if answer[k] == 0:
                        break
            if answer[k] == 0:
                break

    return answer



print(check_distancing([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# result = [1, 0, 1, 1, 1]