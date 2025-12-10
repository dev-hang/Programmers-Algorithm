def no_more_than_2_bits(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            b = '0' + str(bin(num)[2:])
            result = ''
            for i in range(len(b) - 1, -1, -1):
                if b[i:i + 2] == '01':
                    result = b[:i] + '10' + b[i + 2:]
                    break
            answer.append(int(result, 2))
    return answer




print(no_more_than_2_bits([2,7])) # result = [3,11]