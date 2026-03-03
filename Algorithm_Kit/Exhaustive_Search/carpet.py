def carpet(brown, yellow):
    answer = []
    total = brown + yellow
    cases = []

    for i in range(1, total + 1):
        if total % i == 0:
            cases.append((i, total // i))

    for case in cases:
        w, h = case
        if w >= h:
            if 2 * w + 2 * h - 4 == brown and (w - 2) * (h - 2) == yellow:
                return [w, h]

    return answer






print(carpet(10,	2)) # result = [4, 3]
print(carpet(8,	1)) # result = [3, 3]
print(carpet(24,	24)) # result = [8, 6]