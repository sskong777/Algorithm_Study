import sys
input = sys.stdin.readline

def dfs(s, cnt):
    global v_cnt
    global c_cnt
    if cnt == l and v_cnt >= 1 and c_cnt >= 2:
        print(''.join(temp))
        return
        
    for i in range(s, c):
        if words[i] not in temp:
            temp.append(words[i])
            if words[i] in vowel:
                v_cnt += 1
            else:
                c_cnt += 1
            if temp[0] in words[c-l + 1:]:
                return
            
            dfs(i+1, cnt+1)
            if words[i] in vowel:
                v_cnt -= 1
            else:
                c_cnt -= 1
            temp.pop()
    

l, c = map(int, input().split())
words = list(input().split())
words.sort()
temp = []
vowel = ['a', 'e', 'i', 'o', 'u']
v_cnt = 0
c_cnt = 0
dfs(0, 0)