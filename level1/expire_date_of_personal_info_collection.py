def expire_date_of_personal_info_collection(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = today.split('.')
    duration = {}

    for term in terms:
        tp, dr = term.split()
        duration[tp] = dr

    for i in range(len(privacies)):
        pv_date, pv_term = privacies[i].split()
        pv_y, pv_m, pv_d = pv_date.split('.')

        tm_m = duration[pv_term]

        pv_m = int(pv_m) + int(tm_m)

        if pv_m > 12:
            if pv_m % 12 != 0:
                pv_y = int(pv_y) + pv_m // 12
                pv_m = pv_m - 12 * (pv_m // 12)
            else:
                pv_y = int(pv_y) + pv_m // 12 - 1
                pv_m = pv_m - 12 * (pv_m // 12 - 1)
        if pv_m < 10:
            pv_m = '0' + str(pv_m)

        today = int(today_y + today_m + today_d)
        pv = int(str(pv_y) + str(pv_m) + str(pv_d))

        if today >= pv:
            answer.append(i + 1)

    return sorted(answer)




print(expire_date_of_personal_info_collection("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# result = [1, 3]
print(expire_date_of_personal_info_collection("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
# result = [1, 4, 5]