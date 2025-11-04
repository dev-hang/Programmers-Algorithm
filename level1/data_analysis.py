def data_analysis(data, ext, val_ext, sort_by):
    answer = []
    cond = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    for dt in data:
        if dt[cond[ext]] < val_ext:
            answer.append(dt)

    return sorted(answer, key=lambda x: x[cond[sort_by]])



print(data_analysis([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain"))
# result = [[3,20300401,10,8],[1,20300104,100,80]]