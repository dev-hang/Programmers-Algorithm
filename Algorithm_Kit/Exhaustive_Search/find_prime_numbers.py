from itertools import permutations


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def find_prime_numbers(numbers):
    answer = 0
    num_arr = []
    comb = set()
    n = len(numbers)

    for i in range(n):
        num_arr.append(numbers[i])

    for i in range(1, n + 1):
        for nums in permutations(num_arr, i):
            comb.add(int("".join(list(nums))))

    for num in comb:
        if is_prime(num):
            answer += 1

    return answer


print(find_prime_numbers("17"))  # result = 3
print(find_prime_numbers("011"))  # result = 2
