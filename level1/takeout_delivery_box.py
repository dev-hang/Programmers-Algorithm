def takeout_delivery_box(n, w, num):
    answer = 0
    h = n//w + 1
    box = 1
    arr = []

    for i in range(h):
        rows = []
        for j in range(w):
            if box > n:
                rows.append(0)
            else:
                rows.append(box)
            box += 1

        if i % 2 != 0:
            rows.reverse()
        arr.append(rows)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == num:
                k = i
                while k < h and arr[k][j]:
                    answer += 1
                    k += 1

    return answer



print(takeout_delivery_box(22, 6, 8)) # result = 3
print(takeout_delivery_box(13, 3, 6)) # result = 4