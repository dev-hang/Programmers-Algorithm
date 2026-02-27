def mock_test(answers):
    answer = []
    n = len(answers)

    f = [1, 2, 3, 4, 5] * n
    s = [2, 1, 2, 3, 2, 4, 2, 5] * n
    t = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * n

    i, j, k = 0, 0, 0
    for idx in range(n):
        if answers[idx] == f[:n][idx]:
            i += 1
        if answers[idx] == s[:n][idx]:
            j += 1
        if answers[idx] == t[:n][idx]:
            k += 1

    if i == max(i, j, k):
        answer.append(1)
    if j == max(i, j, k):
        answer.append(2)
    if k == max(i, j, k):
        answer.append(3)

    return answer


print(mock_test([1, 2, 3, 4, 5]))  # result = [1]
print(mock_test([1, 3, 2, 4, 2]))  # result = [1,2,3]
