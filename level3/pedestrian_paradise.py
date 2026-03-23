def pedestrian_paradise(m, n, citymap):
    answer = 0
    MOD = 20170805
    dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(2)]
    dp[0][0][0] = 1

    for i in range(m):
        for j in range(n):
            if citymap[i][j] == 0:
                dp[0][i+1][j] += (dp[0][i][j] + dp[1][i][j]) % MOD
                dp[1][i][j+1] += (dp[0][i][j] + dp[1][i][j]) % MOD
            elif citymap[i][j] == 2:
                dp[0][i+1][j] += dp[0][i][j]
                dp[0][i+1][j] %= MOD
                dp[1][i][j+1] += dp[1][i][j]
                dp[1][i][j+1] %= MOD

    answer = (dp[0][m-1][n-1] + dp[1][m-1][n-1]) % MOD

    return answer



print(pedestrian_paradise(3, 3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])) # result = 6
print(pedestrian_paradise(3, 6, [[0, 2, 0, 0, 0, 2], [0, 0, 2, 0, 1, 0], [1, 0, 0, 2, 2, 0]])) # result = 2
