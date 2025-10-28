def reverse_3_digit(n):
    answer = 0
    num = ''

    while n > 0:
        num += str(n % 3)
        n = n // 3

    i = len(num) - 1
    j = 0

    while i >= 0:
        answer += int(num[i]) * (3 ** j)
        i -= 1
        j += 1

    return answer


print(reverse_3_digit(45)) # result = 7
print(reverse_3_digit(125)) # result = 229