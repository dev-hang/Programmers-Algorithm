def park(mats, park):
    n = len(park)
    m = len(park[0])
    mats.sort(reverse=True)

    for mat in mats:
        for r in range(n-mat+1):
            for c in range(m-mat+1):
                if all(park[i][j] == '-1' for i in range(r, r+mat) for j in range(c, c+mat)):
                    return mat

    return -1



print(park([5,3,2], [["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))
# result = 3