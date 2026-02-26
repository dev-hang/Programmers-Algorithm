def kth_number(array, commands):
    answer = []
    for cmd in commands:
        i, j, k = cmd
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer





print(kth_number([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])) # result = [5, 6, 3]