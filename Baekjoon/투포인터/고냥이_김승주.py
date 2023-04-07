import sys
input = sys.stdin.readline

n = int(input())
words = input()


ans = 0
for start in range(len(words)-1):
    count,type_count = 1,1
    end = start+1
    a_set=set([words[start]])
    if ans >=len(words)-start:
        break
    while True:
        if type_count >n or end >=len(words):
            ans = max(count-1, ans)
            break
        if words[end] in a_set:
            count+=1
            end +=1
        else:
            a_set.add(words[end])
            end+=1
            type_count+=1
            count+=1
print(ans)