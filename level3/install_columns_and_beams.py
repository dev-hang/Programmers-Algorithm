def check_wall(cases):
    for x, y, a in cases:
        if a == 0:
            if (
                y != 0
                and [x, y - 1, 0] not in cases
                and [x - 1, y, 1] not in cases
                and [x, y, 1] not in cases
            ):
                return False
        else:
            if (
                [x, y - 1, 0] not in cases
                and [x + 1, y - 1, 0] not in cases
                and ([x - 1, y, 1] not in cases or [x + 1, y, 1] not in cases)
            ):
                return False
    return True


def install_columns_and_beams(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        case = [x, y, a]
        if b == 1:
            answer.append(case)
            if not check_wall(answer):
                answer.remove(case)
        else:
            answer.remove(case)
            if not check_wall(answer):
                answer.append(case)

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer


print(
    install_columns_and_beams(
        5,
        [
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [2, 1, 0, 1],
            [2, 2, 1, 1],
            [5, 0, 0, 1],
            [5, 1, 0, 1],
            [4, 2, 1, 1],
            [3, 2, 1, 1],
        ],
    )
)  # result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(
    install_columns_and_beams(
        5,
        [
            [0, 0, 0, 1],
            [2, 0, 0, 1],
            [4, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [2, 1, 1, 1],
            [3, 1, 1, 1],
            [2, 0, 0, 0],
            [1, 1, 1, 0],
            [2, 2, 0, 1],
        ],
    )
)  # result = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
