def best_album(genres, plays):
    answer = []
    d, total = {}, {}
    idx = 0

    for genre, play in zip(genres, plays):
        if genre not in d:
            d[genre] = [[idx, play]]
            total[genre] = play
        else:
            d[genre].append([idx, play])
            total[genre] += play
        idx += 1

    for g, p in sorted(total.items(), key=lambda x: x[1], reverse=True):
        cnt = 0
        for idx, play in sorted(d[g], key=lambda x: x[1], reverse=True):
            if cnt < 2:
                answer.append(idx)
                cnt += 1

    return answer



print(best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])) # result = [4, 1, 3, 0]