def calculate_money_needed(price, money, count):
    for i in range(1, count + 1):
        money -= i * price

    return 0 if money >= 0 else -1 * money



print(calculate_money_needed(3, 20, 4)) # result = 10