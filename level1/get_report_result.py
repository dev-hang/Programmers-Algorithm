def get_report_result(id_list, report, k):
    answer = []
    rpt_list = {}
    report = set(report)

    for user in id_list:
        rpt_list[user] = []

    for rpt in report:
        er, ee = rpt.split()
        rpt_list[ee].append(er)

    for user in id_list:
        cnt = 0
        for key in rpt_list:
            if len(rpt_list[key]) >= k:
                cnt += rpt_list[key].count(user)
        answer.append(cnt)

    return answer



print(get_report_result(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# result = [2,1,1,0]
print(get_report_result(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
# result = [0,0]