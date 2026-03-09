def pop_ballons(a):
    remain = [False] * len(a)
    start, end = 1e9, 1e9

    for i in range(len(a)):
        if a[i] < start:
            start = a[i]
            remain[i] = True
        if a[-1-i] < end:
            end = a[-1-i]
            remain[-1-i] = True

    return sum(remain)



print(pop_ballons([9,-1,-5])) # result = 3
print(pop_ballons([-16,27,65,-2,58,-92,-71,-68,-61,-33])) # result = 6
