'''
    제약 조건 : 각 장르별로 2개 곡 까지 가능
'''
from collections import defaultdict
def solution(genres, plays):
    
    album_hash = defaultdict(list)
    
    for i in range(len(genres)):
        album_hash[genres[i]].append((plays[i], i)) # 장르 : [ ( 횟수, 인덱스 ), ( 횟수, 인덱스 )]
    
    total_count_hash = defaultdict(int)
    for genere in album_hash:
        total_count_hash[genere] += sum(x1 for x1, x2 in album_hash[genere])
        album_hash[genere] = sorted(album_hash[genere], key = lambda x : (-x[0], x[1]))
    total_count_hash = sorted(total_count_hash.items(), key=lambda x: x[1], reverse=True)


    answer = []
    for genere, total_count in total_count_hash:
        count = 0
        for play_count, album_num in album_hash[genere]:
            answer.append(album_num)
            count+=1
            if count >= 2:
                break
    return answer