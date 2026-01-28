from collections import Counter

def collision_risk_prevention(points, routes):
    answer = 0
    paths = []

    for route in routes:
        path = []
        time = 0
        for i in range(len(route)-1):
            from_x, from_y = points[route[i]-1]
            to_x, to_y = points[route[i+1]-1]
            while from_x != to_x:
                path.append((from_x, from_y, time))
                if from_x < to_x:
                    from_x += 1
                else:
                    from_x -= 1
                time += 1
            while from_y != to_y:
                path.append((from_x, from_y, time))
                if from_y < to_y:
                    from_y += 1
                else:
                    from_y -= 1
                time += 1

        path.append((from_x, from_y, time))
        paths.extend(path)

    counter = Counter(paths)

    for v in counter.values():
        if v >= 2:
            answer += 1

    return answer




print(collision_risk_prevention([[3, 2], [6, 4], [4, 7], [1, 4]],	[[4, 2], [1, 3], [2, 4]]))
# result = 1
print(collision_risk_prevention([[3, 2], [6, 4], [4, 7], [1, 4]],	[[4, 2], [1, 3], [4, 2], [4, 3]]))
# result = 9
print(collision_risk_prevention([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]],	[[2, 3, 4, 5], [1, 3, 4, 5]]))
# result = 0