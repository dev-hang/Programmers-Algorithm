def make_star_at_the_intersection(line):
    answer = []
    min_x = min_y = int(1e10)
    max_x = max_y = -int(1e10)
    point = []

    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i+1, len(line)):
            c, d, f = line[j]
            if a * d - b * c != 0:
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)
                if int(x) == x and int(y) == y:
                    x, y = int(x), int(y)
                    point.append([x, y])
                    min_x = min(min_x, x)
                    min_y = min(min_y, y)
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)

    star = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in point:
        nx = x + abs(min_x) if min_x < 0 else x - min_x
        ny = y + abs(min_y) if min_y < 0 else y - min_y
        star[ny][nx] = '*'

    for item in star:
        answer.append(''.join(item))

    return answer[::-1]






print(make_star_at_the_intersection([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])) # result = ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
print(make_star_at_the_intersection([[0, 1, -1], [1, 0, -1], [1, 0, 1]])) # result = ["*.*"]
print(make_star_at_the_intersection([[1, -1, 0], [2, -1, 0]])) # result = ["*"]
print(make_star_at_the_intersection([[1, -1, 0], [2, -1, 0], [4, -1, 0]])) # result = ["*"]