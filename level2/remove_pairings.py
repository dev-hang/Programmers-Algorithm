def remove_pairings(s):
    answer = 1
    stack = [s[0]]

    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if stack:
        answer = 0

    return answer


print(remove_pairings('baabaa')) # result = 1
print(remove_pairings('cdcd')) # result = 0