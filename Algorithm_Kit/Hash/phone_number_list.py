def phone_number_list(phone_book):
    answer = True
    nums = {}

    for num in phone_book:
        nums[num] = 1

    for num in phone_book:
        tmp = ''
        for c in num[:-1]:
            tmp += c
            if tmp in nums:
                return False

    return answer




print(phone_number_list(["119", "97674223", "1195524421"])) # result = false
print(phone_number_list(["123","456","789"])) # result = true
print(phone_number_list(["12","123","1235","567","88"])) # result = false