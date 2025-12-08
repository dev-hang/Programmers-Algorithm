import math

def calculate_parking_fee(fees, records):
    answer = {}
    times = {}
    min_time, min_cost, unit_time, unit_cost = fees

    for record in records:
        time, num, in_out = record[:5], record[6:10], record[11:]
        if in_out == 'IN':
            if num not in times:
                times[num] = [int(time[:2]) * 60 + int(time[3:])]
            else:
                times[num].append(int(time[:2]) * 60 + int(time[3:]))
        else:
            times[num].append(int(time[:2]) * 60 + int(time[3:]))

    for k in times:
        total = 0
        for i in range(0, len(times[k]) - 1, 2):
            total += times[k][i + 1] - times[k][i]
        if len(times[k]) % 2 == 1:
            total += 23 * 60 + 59 - times[k][-1]

        if total <= min_time:
            cost = min_cost
        else:
            cost = min_cost + math.ceil((total - min_time) / unit_time) * unit_cost
        answer[k] = cost

    answer = sorted(answer.items(), key=lambda x: x[0])

    return [cost[1] for cost in answer]




print(calculate_parking_fee([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# result = [14600, 34400, 5000]
print(calculate_parking_fee([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# result = [0, 591]
print(calculate_parking_fee([1, 461, 1, 10], ["00:00 1234 IN"]))
# result = [14841]