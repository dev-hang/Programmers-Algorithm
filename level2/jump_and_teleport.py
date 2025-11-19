def jump_and_teleport(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans



print(jump_and_teleport(5)) # result = 2
print(jump_and_teleport(6)) # result = 2
print(jump_and_teleport(5000)) # result = 5