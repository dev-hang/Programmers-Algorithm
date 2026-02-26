def h_index(citations):
    h = 0
    for num in sorted(citations, reverse=True):
        if num > h:
            h += 1
        if num == h:
            break
    return h





print(h_index([3, 0, 6, 1, 5])) # result = 3