def solution(genres, plays):
    answer = []
    dic = {}
    play_list = {}

    idx = 0
    for g, p in zip(genres, plays):

        if g in dic:
            dic[g].append([p, idx])
            play_list[g] += p
        else:
            dic[g] = [[p, idx]]
            play_list[g] = p

        idx += 1

    for n in genres:
        dic[n].sort(reverse=True)

    play_list = dict(sorted(play_list.items(), key=lambda x: x[1], reverse=True))

    for key in play_list.keys():
        pl = sorted(dic[key], key=lambda x: (-x[0], x[1]), reverse=False)
        answer.append(pl[0][1])
        if len(pl) > 1:
            answer.append(pl[1][1])

    return answer
