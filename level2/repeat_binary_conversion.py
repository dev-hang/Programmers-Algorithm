def repeat_binary_conversion(s):
    zero = 0
    cnt = 0

    while s != '1':
        cnt += 1
        one = s.count('1')
        zero += len(s) - one
        s = bin(one)[2:]

    return [cnt, zero]



print(repeat_binary_conversion("110010101001")) # result = [3,8]
print(repeat_binary_conversion("01110")) # result = [3,3]
print(repeat_binary_conversion("1111111")) # result = [4,1]