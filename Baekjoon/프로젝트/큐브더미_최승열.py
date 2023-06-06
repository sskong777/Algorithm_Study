import sys
s={tuple(map(int, r.split())) for r in sys.stdin.readlines()[1:]}
d=[(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]
print(sum(len([1 for a,b,c in d if (x+a, y+b, z+c) in s])==6 for x,y,z in s))