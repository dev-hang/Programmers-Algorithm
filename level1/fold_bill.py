def fold_bill(wallet, bill):
    answer = 0

    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1

    return answer


print(fold_bill([30, 15], [26, 17])) # result = 1
print(fold_bill([50, 50], [100, 241])) # result = 4