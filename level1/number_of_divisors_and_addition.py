def number_of_divisors_and_addition(left, right):
    answer = 0

    for i in range(left, right + 1):
        if int(i ** (1 / 2)) == i ** (1 / 2):
            answer -= i
        else:
            answer += i

    return answer


print(number_of_divisors_and_addition(13, 17)) # result = 43
print(number_of_divisors_and_addition(24, 27)) # result = 52