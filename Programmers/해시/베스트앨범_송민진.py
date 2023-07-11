s_dict = {}
g_dict = {}

def solution(genres, plays):
    answer = []

    for i in range(len(genres)):
        if genres[i] not in g_dict:
            g_dict[genres[i]] = plays[i]
            s_dict[genres[i]] = [(plays[i], i)]
        else:
            g_dict[genres[i]] += plays[i]
            s_dict[genres[i]].append((plays[i], i))

    arr = sorted(g_dict.items(), key=lambda x:x[1], reverse=True)

    for a in arr:
        checking_genre = a[0]
        songs = sorted(s_dict[checking_genre], key=lambda x:x[0], reverse=True)
        cnt = 0
        for song in songs:
            if cnt >= 2:
                break
            answer.append(song[1])
            cnt += 1

    return answer