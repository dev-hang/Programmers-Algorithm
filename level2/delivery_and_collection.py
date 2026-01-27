def delivery_and_collection(cap, n, deliveries, pickups):
    answer = 0
    delivery, pickup = 0, 0

    for i in range(n - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]

        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += (i + 1) * 2

    return answer



print(delivery_and_collection(4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0]))
# result = 16
print(delivery_and_collection(2,	7,	[1, 0, 2, 0, 1, 0, 2],	[0, 2, 0, 1, 0, 2, 0]))
# result = 30