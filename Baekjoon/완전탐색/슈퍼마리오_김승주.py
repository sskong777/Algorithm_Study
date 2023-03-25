import sys
input = sys.stdin.readline

mushrooms = []
ans = 0 

for i in range(10):
    mushrooms.append(int(input()))
    
for mushroom in mushrooms:
    if abs(100-ans) < abs(100-(ans+mushroom)):
        break
    ans+=mushroom
print(ans)