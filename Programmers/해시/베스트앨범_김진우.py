# def solution(genres, plays):
#     answer = []
#     return answer
#
# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
#
# def solution(genres, plays):
#     # 장르별 재생 횟수와 노래 정보를 저장할 딕셔너리
#     genre_info = {}
#
#     # 장르별로 재생 횟수와 고유 번호를 함께 저장
#     for i in range(len(genres)):
#         genre = genres[i]
#         play = plays[i]
#         idx = i
#         if genre in genre_info:
#             genre_info[genre].append((play, idx))
#         else:
#             genre_info[genre] = [(play, idx)]
#
#     # 장르별 재생 횟수를 기준으로 내림차순 정렬
#     genre_rank = sorted(genre_info.keys(), key=lambda x: sum(play for play, _ in genre_info[x]), reverse=True)
#
#     answer = []
#
#     # 장르별로 최대 2개의 노래를 선택하여 베스트앨범에 추가
#     for genre in genre_rank:
#         songs = genre_info[genre]
#         songs = sorted(songs, key=lambda x: (x[0], -x[1]), reverse=True)
#         for i in range(min(2, len(songs))):
#             answer.append(songs[i][1])
#
#     return answer

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