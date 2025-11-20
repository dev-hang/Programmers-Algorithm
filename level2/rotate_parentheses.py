def check_correct(s):
    stack = []
    pair = {']': '[', ')': '(', '}': '{'}
    for a in s:
        if len(stack) > 0:
            if a in pair:
                if stack[-1] == pair[a]:
                    stack.pop()
            else:
                stack.append(a)
        else:
            stack.append(a)
    if len(stack) > 0:
        return False
    return True

def rotate_parentheses(s):
    answer = 0

    for i in range(len(s)):
        if check_correct(s):
            answer += 1
        s = s[1:] + s[0]

    return answer



print(rotate_parentheses("[](){}")) # result = 3
print(rotate_parentheses("}]()[{")) # result = 2
print(rotate_parentheses("[)(]")) # result = 0
print(rotate_parentheses("}}}")) # result = 0