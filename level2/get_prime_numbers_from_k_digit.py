def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def get_prime_numbers_from_k_digit(n, k):
    answer = 0

    kdigit = ''
    while n > k:
        kdigit = str(n % k) + kdigit
        n //= k
    kdigit = str(n) + kdigit

    arr = kdigit.split('0')

    for num in arr:
        if num and is_prime(int(num)):
            answer += 1

    return answer



print(get_prime_numbers_from_k_digit(437674, 3)) # result = 3
print(get_prime_numbers_from_k_digit(110011, 10)) # result = 2