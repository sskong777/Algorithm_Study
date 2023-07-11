def solution(genres, plays):
    musics = {}
    total_genres = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in musics:
            musics[g] = [(i, p)]
        else:
            musics[g].append((i, p))

        if g not in total_genres:
            total_genres[g] = p
        else:
            total_genres[g] += p

    total_genres = sorted(total_genres.items(), key=lambda x: -x[1])

    for g in total_genres:
        genre_name = g[0]
        musics[genre_name] = sorted(musics[genre_name], key=lambda x: (-x[1], x[0]))

    result = []
    for g in total_genres:
        cnt = 0
        for i, p in musics[g[0]]:
            cnt += 1
            result.append(i)
            if cnt >= 2:
                break

    return result