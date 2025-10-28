def budget(d, bg):
    d.sort()
    i = 0

    for i in range(len(d)):
        bg -= d[i]
        if bg < 0:
            return i
        elif bg == 0:
            return i + 1

    return i + 1


print(budget([1,3,2,5,4], 9))  # result = 3
print(budget([2,2,3,3], 10))  # result = 4