def cut_n_squared_array(n, left, right):
    answer = []

    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)

    return answer



print(cut_n_squared_array(3, 2, 5)) # result = [3,2,2,3]
print(cut_n_squared_array(4, 7, 14)) # result = [4,3,3,3,4,4,4,4]