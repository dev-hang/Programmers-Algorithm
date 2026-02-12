def analog_clock(h1, m1, s1, h2, m2, s2):
    answer = 0
    m_cnt, h_cnt = 0, 0
    from_sec = h1 * 60 * 60 + m1 * 60 + s1
    to_sec = h2 * 60 * 60 + m2 * 60 + s2

    if from_sec == 0 or from_sec == 60 * 60 * 12:
        answer += 1

    for i in range(from_sec, to_sec):
        s = (i * 6) % 360
        m = (i / 10) % 360
        h = (i / 120) % 360

        ns = 360 if ((i + 1) * 6) % 360 == 0 else ((i + 1) * 6) % 360
        nm = 360 if ((i + 1) / 10) % 360 == 0 else ((i + 1) / 10) % 360
        nh = 360 if ((i + 1) / 120) % 360 == 0 else ((i + 1) / 120) % 360

        if m > s and nm <= ns:
            m_cnt += 1
        if h > s and nh <= ns:
            h_cnt += 1
        if ns == nm == nh:
            answer -= 1

    answer += m_cnt + h_cnt

    return answer




print(analog_clock(0,	5,	30,	0,	7,	0)) # result = 2
print(analog_clock(12,	0,	0,	12,	0,	30)) # result = 1
print(analog_clock(0,	6,	1,	0,	6,	6)) # result = 0
print(analog_clock(11,	59,	30,	12,	0,	0)) # result = 1
print(analog_clock(11,	58,	59,	11,	59,	0)) # result = 1
print(analog_clock(1,	5,	5,	1,	5,	6)) # result = 2
print(analog_clock(0,	0,	0,	23,	59,	59)) # result = 2852