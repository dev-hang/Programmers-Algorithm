def wrapping_bandage(bandage, health, attacks):
    t, x, y = bandage[0], bandage[1], bandage[2]
    cur, con = 0, 0
    max_health = health

    for attack in attacks:
        tm, amt = attack[0], attack[1]
        while tm > cur:
            cur += 1
            if cur == tm:
                health -= amt
                con = 0
                if health <= 0:
                    return -1
            else:
                health += x
                con += 1
                if con == t:
                    health += y
                    con = 0
                if health > max_health:
                    health = max_health

    return health


print(wrapping_bandage([5, 1, 5],	30,	[[2, 10], [9, 15], [10, 5], [11, 5]])) # result = 5
print(wrapping_bandage([3, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]])) # result = -1
print(wrapping_bandage([4, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]])) # result = -1
print(wrapping_bandage([1, 1, 1],	5,	[[1, 2], [3, 2]])) # result = 3