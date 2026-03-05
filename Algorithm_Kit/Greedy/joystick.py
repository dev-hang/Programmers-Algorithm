def joystick(name):
    answer = 0
    left, right = 0, 0
    n = len(name)
    cur = n - 1

    while left < n:
        answer += min(ord(name[left])-65, 91-ord(name[left]))
        right = left + 1

        while right < n and name[right] == 'A':
            right += 1

        cur = min(cur, left*2 + n-right, (n-right)*2 + left)
        left = right

    answer += cur

    return answer




print(joystick("JEROEN")) # result = 56
print(joystick("JAN")) # result = 23