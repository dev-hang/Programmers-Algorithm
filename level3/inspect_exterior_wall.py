from itertools import permutations


def inspect_exterior_wall(n, weak, dist):
    answer = len(dist) + 1
    m = len(weak)

    for i in range(m):
        weak.append(weak[i] + n)

    for st in range(m):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            pos = weak[st] + friends[cnt - 1]
            for i in range(st, st + m):
                if pos < weak[i]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[i] + friends[cnt - 1]

            answer = min(answer, cnt)

    if answer > len(dist):
        return -1

    return answer


print(inspect_exterior_wall(12, [1, 5, 6, 10], [1, 2, 3, 4]))  # result = 2
print(inspect_exterior_wall(12, [1, 3, 4, 9, 10], [3, 5, 7]))  # result = 1
