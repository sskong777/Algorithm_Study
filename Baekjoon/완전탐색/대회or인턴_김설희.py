n, m, k= map(int, input().split())
t = 0

while True:
	n -= 2
	m -= 1
	if n + m < k or n < 0 or m < 0:
		break
	t += 1

print(t)
