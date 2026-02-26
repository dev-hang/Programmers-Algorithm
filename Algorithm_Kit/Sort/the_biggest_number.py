def the_biggest_number(numbers):
    answer = ''
    numbers = sorted([str(num) for num in numbers], key=lambda x:(x*4)[:4], reverse=True)
    answer = ''.join(numbers)
    return answer if answer[0] != '0' else '0'





print(the_biggest_number([6, 10, 2])) # result = "6210"
print(the_biggest_number([3, 30, 34, 5, 9])) # result = "9534330"
