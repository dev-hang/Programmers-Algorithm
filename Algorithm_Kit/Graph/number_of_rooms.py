def number_of_rooms(arrows):
    answer = 0
    d = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

    visited, routes = set(), set()
    x, y = 0, 0
    visited.add((x, y))

    for arr in arrows:
        for _ in range(2):
            nx, ny = x + d[arr][0], y + d[arr][1]

            if (nx, ny) in visited and (x, y, nx, ny) not in routes:
                answer += 1

            visited.add((nx, ny))
            routes.add((x, y, nx, ny))
            routes.add((nx, ny, x, y))

            x, y = nx, ny

    return answer



print(number_of_rooms([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])) # result = 3