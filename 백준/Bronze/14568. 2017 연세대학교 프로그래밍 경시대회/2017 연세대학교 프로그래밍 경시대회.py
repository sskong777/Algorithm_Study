n = int(input())
cnt = 0

# a + b + c = n-3
# c > b + 2
# a % 2 == 0

for a in range(0, n-2):
	for b in range(0, n-2):
		for c in range(0, n-2):
			if a + b + c == n-3 and a % 2 == 0 and c > b + 2:
				cnt += 1

print(cnt)