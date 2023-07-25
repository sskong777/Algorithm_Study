from bisect import bisect_left
def solution(citations):
    citations.sort()
    ans = 0
    for h in range(10001):
        pos = bisect_left(citations, h)
        if len(citations)-pos >= h and pos < h:
            ans = max(ans, h) 
    return ans