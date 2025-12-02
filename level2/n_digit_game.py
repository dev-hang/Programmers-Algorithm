def n_digit_game(n, t, m, p):
    answer = '0'
    mapped = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    for i in range(1, t * m):
        n_digit = ''
        while i > 0:
            num = i % n
            if 10 <= num <= 15:
                num = mapped[num]
            n_digit = str(num) + n_digit
            i //= n
        answer += n_digit

    return answer[p - 1:t * m:m]



print(n_digit_game(2, 4, 2, 1)) # result = "0111"
print(n_digit_game(16, 16, 2, 1)) # result = "02468ACE11111111"
print(n_digit_game(16, 16, 2, 2)) # result = "13579BDF01234567"
