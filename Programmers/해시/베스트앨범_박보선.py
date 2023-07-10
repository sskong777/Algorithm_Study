from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    musicPlays = defaultdict(int)
    musicDict = defaultdict(list)
    
    for i in range(len(genres)):
        musicPlays[genres[i]] += plays[i]
        musicDict[genres[i]].append([genres[i], plays[i], i])
        
    for k in musicDict.keys():
        musicDict[k] = sorted(musicDict[k], key = lambda x : -x[1])
        
    musicPlays = sorted(musicPlays.items(), key=lambda x:x[1], reverse=True)
    
    
    for g, p in musicPlays:
        if len(musicDict[g]) >= 2:
            answer.append(musicDict[g][0][2])
            answer.append(musicDict[g][1][2])
        else:
            answer.append(musicDict[g][0][2])
    
    return answer