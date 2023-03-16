a, b = map(int, input().split())
ans1 = int(-a - (a**2 - b)**0.5)
ans2 = int(-a + (a**2 - b)**0.5)
print(ans1, ans2) if ans1 != ans2 else print(ans1)
