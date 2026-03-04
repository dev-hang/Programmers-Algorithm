def multi_level_sales_of_toothbrush(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    graph = {}

    for idx, nm in enumerate(enroll):
        graph[nm] = idx

    for sell, amt in zip(seller, amount):
        profit = amt * 100
        while profit > 0 and sell != '-':
            idx = graph[sell]
            answer[idx] += profit - profit//10
            profit //= 10
            sell = referral[idx]

    return answer





print(multi_level_sales_of_toothbrush(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
                                      ,["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
                                      ,["young", "john", "tod", "emily", "mary"]
                                      ,[12, 4, 2, 5, 10]))
# result = [360, 958, 108, 0, 450, 18, 180, 1080]
print(multi_level_sales_of_toothbrush(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
                                      ,["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
                                      ,["sam", "emily", "jaimie", "edward"]
                                      ,[2, 3, 5, 4]))
# result = [0, 110, 378, 180, 270, 450, 0, 0]