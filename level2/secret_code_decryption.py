from itertools import combinations

def secret_code_decryption(n, q, ans):
    answer = 0
    arr = [i for i in range(1, n + 1)]

    for case in list(combinations(arr, 5)):
        result = []
        for nums in q:
            cnt = 0
            for i in range(len(nums)):
                if nums[i] in case:
                    cnt += 1
            result.append(cnt)
        if result == ans:
            answer += 1

    return answer



print(secret_code_decryption(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
# result = 3
print(secret_code_decryption(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))
# result = 5