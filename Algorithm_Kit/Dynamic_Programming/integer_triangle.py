def integer_triangle(triangle):
    answer = 0
    n = len(triangle)

    while n > 1:
        for i in range(len(triangle[n-2])):
            triangle[n-2][i] += max(triangle[n-1][i], triangle[n-1][i+1])
        n -= 1

    answer = triangle[0][0]

    return answer




print(integer_triangle([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # result = 30