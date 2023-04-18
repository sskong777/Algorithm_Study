n, m = map(int,input().split())

numbers = sorted(list(map(int,input().split())))

ans = []
def back(dep):
    if dep == m:
        print(' '.join(map(str,ans)))
        return
    
    for num in numbers:
        if num not in ans:
            ans.append(num)
            back(dep+1)
            ans.pop()

back(0)