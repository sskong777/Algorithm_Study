def solution(genres, plays):
    arr = []
    for i in range(len(genres)):
        # genre, play, 고유번호 순으로 담아줌
        arr.append([genres[i], plays[i], i])
        # enumerate 사용하면 편함

    hash_map = {}
    # 장르별 합산 값을 구하기 위해 사용
    for genre, times, index in arr:
        hash_map[genre] = hash_map.get(genre, 0) + times

    # 장르별 합산값 내림차순, 장르 내 내림차순,
    arr.sort(key=lambda x: (hash_map[x[0]], x[1], -x[2]), reverse=True)

    answer = []  # 고유번호를 담아줄 배열
    temp_dict = {}  # 장르별 개수를 세어주기 위한 배열
    for genre, times, index in arr:
        temp_dict[genre] = temp_dict.get(genre, 0) + 1
        if temp_dict[genre] <= 2:
            answer.append(index)

    return answer