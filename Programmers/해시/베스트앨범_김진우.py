

genres1 = ["classic", "pop", "classic", "classic", "pop"]
plays1 = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []

    all_play = {}
    each_play = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in all_play:
            all_play[genre] = play
            each_play[genre] = []
            each_play[genre].append([genre,play,i])
        else:
            all_play[genre] += play
            each_play[genre].append([genre, play, i])
    print(all_play)
    print(each_play)

    for key in each_play.keys():
        each_play[key] = sorted(each_play[key], key=lambda x : x[1], reverse=True)

    print(each_play)

    for j in all_play:
        if len(each_play[j]) >= 2:
            answer.append(each_play[j][0][2])
            answer.append(each_play[j][1][2])
        else:
            answer.append(each_play[j][0][2])
    print(answer)

solution(genres1, plays1)
