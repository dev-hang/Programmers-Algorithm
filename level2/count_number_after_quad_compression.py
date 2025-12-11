def count_number_after_quad_compression(arr):
    answer = [0, 0]

    def quad_tree(i, j, k, a):
        divided = [a[x][j:j+k] for x in range(i, i+k)]
        n = len(divided)
        if all(row == [0] * n for row in divided):
            answer[0] += 1
        elif all(row == [1] * n for row in divided):
            answer[1] += 1
        else:
            quad_tree(0, 0, n//2, divided)
            quad_tree(0, n//2, n//2, divided)
            quad_tree(n//2, 0, n//2, divided)
            quad_tree(n//2, n//2, n//2, divided)

    quad_tree(0, 0, len(arr), arr)

    return answer



print(count_number_after_quad_compression([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# result = [4,9]
print(count_number_after_quad_compression([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
# result = [10,15]

