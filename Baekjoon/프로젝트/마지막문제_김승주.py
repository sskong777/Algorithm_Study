

# 난이도의 최솟값 차이가 가장 커지도록 문제를 낼 것

n = int(input())

quizs = sorted(list(map(int, input().split())))

ans = -1
diff = -1
for i in range(1, n):
    temp = int((quizs[i-1] + quizs[i])//2)
    if temp not in quizs:
        temp_max_gap = min(temp-quizs[i-1], quizs[i]-temp)
        if temp_max_gap > diff:
            diff = temp_max_gap
            ans = temp

print(ans) 