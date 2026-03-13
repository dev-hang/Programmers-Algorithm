def four_fundamental_arithmetic_operations(arr):
    answer = 0
    INF = int(1e9)
    n = len(arr) // 2 + 1
    min_dp = [[INF for _ in range(n)] for _ in range(n)]
    max_dp = [[-INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        min_dp[i][i] = int(arr[i * 2])
        max_dp[i][i] = int(arr[i * 2])

    for cnt in range(1, len(max_dp)):
        for start in range(len(max_dp) - cnt):
            end = start + cnt
            for idx in range(start, end):
                if arr[idx * 2 + 1] == "+":
                    max_dp[start][end] = max(
                        max_dp[start][end], max_dp[start][idx] + max_dp[idx + 1][end]
                    )
                    min_dp[start][end] = min(
                        min_dp[start][end], min_dp[start][idx] + min_dp[idx + 1][end]
                    )
                elif arr[idx * 2 + 1] == "-":
                    max_dp[start][end] = max(
                        max_dp[start][end], max_dp[start][idx] - min_dp[idx + 1][end]
                    )
                    min_dp[start][end] = min(
                        min_dp[start][end], min_dp[start][idx] - max_dp[idx + 1][end]
                    )

    answer = max_dp[0][-1]

    return answer


print(
    four_fundamental_arithmetic_operations(["1", "-", "3", "+", "5", "-", "8"])
)  # result = 1
print(
    four_fundamental_arithmetic_operations(
        ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
    )
)  # result = 3
