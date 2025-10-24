def add_non_existed_number(numbers):
    return sum(range(10)) - sum(numbers)


print(add_non_existed_number([1,2,3,4,6,7,8,0])) # reuslt = 14
print(add_non_existed_number([5,8,4,0,6,7,9])) # result = 6