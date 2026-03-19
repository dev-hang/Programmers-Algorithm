def time_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return 3600 * h + 60 * m + s

def sec_to_time(sec):
    h, m, s = sec//3600, (sec%3600)//60, sec%60
    return f'{h:02}:{m:02}:{s:02}'

def insert_ads(play_time, adv_time, logs):
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    viewers = [0 for _ in range(100*3600+1)]

    for log in logs:
        start, end = map(time_to_sec, log.split('-'))
        viewers[start] += 1
        viewers[end] -= 1

    for i in range(1, len(viewers)):
        viewers[i] += viewers[i-1]

    max_viewer, max_time = sum(viewers[:adv_time]), 0
    cur_viewer = max_viewer

    for i in range(1, len(viewers)-adv_time):
        cur_viewer = cur_viewer - viewers[i-1] + viewers[i+adv_time-1]
        if cur_viewer > max_viewer:
            max_viewer = cur_viewer
            max_time = i

    return sec_to_time(max_time)



print(insert_ads("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# result = "01:30:59"
print(insert_ads("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# result = "01:00:00"
print(insert_ads("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
# result = "00:00:00"