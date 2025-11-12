def to_sec(time):
    mm, ss = time.split(":")
    return int(mm) * 60 + int(ss)

def video_player(video_len, pos, op_start, op_end, commands):
    answer = ''

    video_len = to_sec(video_len)
    pos = to_sec(pos)
    op_start = to_sec(op_start)
    op_end = to_sec(op_end)

    for cmd in commands:
        if op_start <= pos <= op_end:
            pos = op_end

        if cmd == 'next':
            pos += 10
        elif cmd == 'prev':
            pos -= 10

        if pos < 0:
            pos = 0
        elif pos > video_len:
            pos = video_len

    if op_start <= pos <= op_end:
        pos = op_end

    mm = str(pos // 60)
    ss = str(pos % 60)

    if len(mm) < 2:
        mm = '0' + mm
    if len(ss) < 2:
        ss = '0' + ss

    answer = mm + ':' + ss

    return answer



print(video_player("34:33",	"13:00",	"00:55",	"02:55",	["next", "prev"]))
# result = "13:00"
print(video_player("10:55",	"00:05",	"00:15",	"06:55",	["prev", "next", "next"]))
# result = "06:55"
print(video_player("07:22",	"04:05",	"00:15",	"04:07",	["next"]))
# result = "04:17"




