def solution(genres, plays):
    answer = []
    dic = {}
    sum_list = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = {}
            dic[genres[i]][i] = plays[i]
            sum_list[genres[i]] = plays[i]
        else:
            dic[genres[i]][i] = plays[i]
            sum_list[genres[i]] += plays[i]

    sorted_dic = sorted(
        dic.items(), key=lambda x: sum_list[x[0]], reverse=True)

    for genre, songs in sorted_dic:
        sorted_songs = sorted(songs.items(), key=lambda x: x[1], reverse=True)
        for index, _ in sorted_songs[:2]:
            answer.append(index)

    return answer
