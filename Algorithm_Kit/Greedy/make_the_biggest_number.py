def make_the_biggest_number(number, k):
    stack = []

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)





print(make_the_biggest_number("1924", 2)) # result = "94"
print(make_the_biggest_number("1231234", 3)) # result = "3234"
print(make_the_biggest_number("4177252841", 4)) # result = "775841"