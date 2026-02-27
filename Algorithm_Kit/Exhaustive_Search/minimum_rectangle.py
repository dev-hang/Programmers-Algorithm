def minimum_rectangle(sizes):
    max_w, max_h = 0, 0

    for size in sizes:
        w, h = size
        if w > h:
            max_w = max(w, max_w)
            max_h = max(h, max_h)
        else:
            max_w = max(h, max_w)
            max_h = max(w, max_h)

    return max_w * max_h


print(minimum_rectangle([[60, 50], [30, 70], [60, 30], [80, 40]]))
# result = 4000
print(minimum_rectangle([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# result = 120
print(minimum_rectangle([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
# result = 133
