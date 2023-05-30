N = int(input())
P, a = 0, []
for p in map(int, input().split()):
    P = P + p/100 - P*p/100
    a.append(str(P*100))
print("\n".join(a))