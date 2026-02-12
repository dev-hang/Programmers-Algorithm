def correct_parentheses(s):
    answer = True
    stack = []

    for p in s:
        if stack and stack[-1] == '(' and p == ')':
            stack.pop()
        else:
            stack.append(p)

    if stack:
        return False

    return answer




print(correct_parentheses("()()")) # result = true
print(correct_parentheses("(())()")) # result = true
print(correct_parentheses(")()(")) # result = false
print(correct_parentheses("(()(")) # result = false