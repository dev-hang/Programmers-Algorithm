def rotate(key):
    n = len(key)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = key[i][j]
    return rotated

def check_lock(lock):
    n = len(lock)//3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True

def lock_and_key(key, lock):
    answer = False
    n, m = len(lock), len(key)
    expended = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            expended[i+n][j+n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        expended[x+i][y+j] += key[i][j]
                if check_lock(expended):
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            expended[x+i][y+j] -= key[i][j]
    return answer



print(lock_and_key([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])) # result = true