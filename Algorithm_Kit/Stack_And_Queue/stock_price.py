from collections import deque

def stock_price(prices):
    answer = []
    prices = deque(prices)

    while prices:
        price = prices.popleft()
        time = 0
        for p in prices:
            time += 1
            if p < price:
                break
        answer.append(time)

    return answer





print(stock_price([1, 2, 3, 2, 3])) # result = [4, 3, 1, 1, 0]