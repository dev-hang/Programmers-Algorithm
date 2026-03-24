def move_110(s):
    answer = []

    for num in s:
        stack, cnt = [], 0
        for i in range(len(num)):
            stack.append(num[i])
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack = stack[:-3]
                cnt += 1

        stack = ''.join(stack[::-1])
        idx = stack.find('0')

        if idx != -1:
            result = stack[:idx] + '011' * cnt + stack[idx:]
        else:
            result = stack + '011' * cnt

        answer.append(''.join(result[::-1]))

    return answer



print(move_110(["1110","100111100","0111111010"])) # result = ["1101","100110110","0110110111"]