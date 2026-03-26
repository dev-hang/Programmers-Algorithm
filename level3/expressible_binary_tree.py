def check_parent(bin_num):
    mid = len(bin_num) // 2

    if mid == 0:
        return True
    elif bin_num[mid] == '0' and '1' in bin_num:
        return False
    else:
        return check_parent(bin_num[:mid]) and check_parent(bin_num[mid+1:])

def expressible_binary_tree(numbers):
    answer = []

    for num in numbers:
        bin_num, height = bin(num)[2:], 0

        while 2 ** height <= len(bin_num):
            height += 1

        bin_num = bin_num.zfill(2 ** height - 1)

        answer.append(1) if check_parent(bin_num) else answer.append(0)

    return answer



print(expressible_binary_tree([7, 42, 5])) # result = [1, 1, 0]
print(expressible_binary_tree([63, 111, 95])) # result = [1, 1, 0]

