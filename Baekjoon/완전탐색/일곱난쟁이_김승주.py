
import sys
input = sys.stdin.readline

dwarfs = [ int(input()) for _ in range(9)]
ans = []
def find_dwarfs(start,count):
    if count == 7 :
        if sum(ans) == 100:
            for dwarf in sorted(ans):
                print(dwarf)
            exit()
        else:
            return
    
    for i in range(start,len(dwarfs)):
        ans.append(dwarfs[i])
        find_dwarfs(i+1,count+1)
        ans.pop()
        
find_dwarfs(0,0)