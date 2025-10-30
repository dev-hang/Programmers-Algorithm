def secret_map(n, arr1, arr2):
    answer = []

    for num1, num2 in zip(arr1, arr2):
        result = ''
        s1 = change(n, num1)
        s2 = change(n, num2)

        for i in range(n - 1, -1, -1):
            if s1[i] == '0' and s2[i] == '0':
                result += ' '
            else:
                result += '#'

        answer.append(result)

    return answer


def change(n, num):
    s = ''

    while num > 0:
        s += str(num % 2)
        num = num // 2

    if len(s) < n:
        s += '0' * (n - len(s))

    return s



print(secret_map(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# result = ["#####","# # #", "### #", "# ##", "#####"]

print(secret_map(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
# result = ["######", "### #", "## ##", " #### ", " #####", "### # "]