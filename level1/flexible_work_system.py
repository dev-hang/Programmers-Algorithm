def flexible_work_system(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        hh = schedules[i] // 100
        mm = schedules[i] % 100 + 10
        if mm > 59:
            mm -= 60
            hh += 1
        schedule = hh * 100 + mm
        for j in range(len(timelogs[i])):
            if startday == 7:
                if j != 7 - startday and j != startday - 1:
                    if timelogs[i][j] > schedule:
                        break
            else:
                if j != 7 - startday and j != 7 - startday - 1:
                    if timelogs[i][j] > schedule:
                        break
        else:
            answer += 1

    return answer




print(flexible_work_system([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))
# result = 3
print(flexible_work_system([730, 855, 700, 720], [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]], 1))
# result = 2