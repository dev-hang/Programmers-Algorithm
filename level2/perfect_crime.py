def dfs(a, b, idx, info, n, m, dp):
    global answer

    if a >= n or b >= m:
        return
    if (a, b, idx) in dp:
        return
    else:
        dp.add((a, b, idx))

    if idx >= len(info):
        answer = min(answer, a)
        return

    dfs(a+info[idx][0], b, idx+1, info, n, m, dp)
    dfs(a, b+info[idx][1], idx+1, info, n, m, dp)

def perfect_crime(info, n, m):
    global answer
    answer = n
    dp = set()
    dfs(0, 0, 0, info, n, m, dp)

    if answer >= n:
        return -1

    return answer





print(perfect_crime([[1, 2], [2, 3], [2, 1]], 4, 4)) # result = 2
print(perfect_crime([[1, 2], [2, 3], [2, 1]], 1, 7)) # result = 0
print(perfect_crime([[3, 3], [3, 3]], 7, 1)) # result = 6
print(perfect_crime([[3, 3], [3, 3]], 6, 1)) # result = -1