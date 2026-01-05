def check_correct(string):
    stack = []

    if string[0] == ')':
        return False

    for s in string:
        if stack:
            if stack[-1] == '(' and s == ')':
                stack.pop()
            elif stack[-1] == s or stack[-1] == ')':
                stack.append(s)
        else:
            stack.append(s)

    if stack:
        return False
    else:
        return True

def divide_string(string):
    left, right = 0, 0

    for i in range(len(string)):
        if string[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return string[:i + 1], string[i + 1:]

    return '', ''

def parentheses_transformation(p):
    answer = ''

    if len(p) == 0:
        return p

    u, v = divide_string(p)

    if check_correct(u):
        return u + parentheses_transformation(v)
    else:
        answer = '(' + parentheses_transformation(v) + ')'

    for s in u[1:-1]:
        if s == '(':
            answer += ')'
        else:
            answer += '('

    return answer



print(parentheses_transformation("(()())()")) # result = "(()())()"
print(parentheses_transformation(")(")) # result = "()"
print(parentheses_transformation("()))((()")) # result = "()(())()"