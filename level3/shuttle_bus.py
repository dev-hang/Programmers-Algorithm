def shuttle_bus(n, t, m, timetable):
    timetable = sorted([int(time[:2])*60 + int(time[3:]) for time in timetable])
    start_time = [9*60 + i*t for i in range(n)]
    con, idx = 0, 0

    for time in start_time:
        cnt = 0
        while cnt < m and idx < len(timetable) and timetable[idx] <= time:
            cnt += 1
            idx += 1
        con = time if cnt < m else timetable[idx-1]-1

    hh = str(con//60).zfill(2)
    mm = str(con%60).zfill(2)

    return hh + ':' + mm





print(shuttle_bus(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])) # result = "09:00"
print(shuttle_bus(2, 10, 2, ["09:10", "09:09", "08:00"])) # result = "09:09"
print(shuttle_bus(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])) # result = "08:59"
print(shuttle_bus(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])) # result = "00:00"
print(shuttle_bus(1, 1, 1, ["23:59"])) # result = "09:00"
print(shuttle_bus(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])) # result = "18:00"