from itertools import product

def emoji_discount_event(users, emoticons):
    answer = []
    d = [10, 20, 30, 40]
    discount_list = list(product(d, repeat=len(emoticons)))

    for discounts in discount_list:
        cnt, amount = 0, 0

        for user in users:
            all_sales = [int(emoticons[i] * (100-discounts[i])/100) for i in range(len(discounts))]
            purchase = []

            for discount in discounts:
                if discount >= user[0]:
                    purchase.append(1)
                else:
                    purchase.append(0)

            all_purchase = [purchase[i] * all_sales[i] for i in range(len(all_sales))]
            total = sum(all_purchase)

            if total >= user[1]:
                cnt += 1
            else:
                amount += total

        answer.append([cnt, amount])

    answer.sort(key=lambda x:(x[0], x[1]), reverse=True)

    return answer[0]





print(emoji_discount_event([[40, 10000], [25, 10000]],[7000, 9000]))
# result = [1, 5400]
print(emoji_discount_event([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
# result = [4, 13860]