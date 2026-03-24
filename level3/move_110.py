def move_110(s):
    answer = []

    for num in s:
        stack, cnt = [], 0
        for i in range(len(num)):
            if num[i] == '0':
                if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                    stack.pop()
                    stack.pop()
                    cnt += 1
                else:
                    stack.append(num[i])
            else:
                stack.append(num[i])

        stack = ''.join(stack[::-1])
        idx = stack.find('0')

        if idx != -1:
            result = stack[:idx] + '011' * cnt + stack[idx:]
        else:
            result = stack + '011' * cnt

        answer.append(''.join(result[::-1]))

    return answer



print(move_110(["1110","100111100","0111111010"])) # result = ["1101","100110110","0110110111"]