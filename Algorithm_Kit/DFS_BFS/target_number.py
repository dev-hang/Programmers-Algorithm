def dfs(idx, value, numbers, target):
    result = 0

    if idx == len(numbers):
        if value == target:
            return 1
        else:
            return 0

    result += dfs(idx+1, value+numbers[idx], numbers, target)
    result += dfs(idx+1, value-numbers[idx], numbers, target)

    return result


def target_number(numbers, target):
    return dfs(0, 0, numbers, target)




print(target_number([1, 1, 1, 1, 1], 3)) # result = 5
print(target_number([4, 1, 2, 1], 4)) # result = 2