N = int(input())
s_and_t = input()

print(sum(1 if s_and_t[i] != s_and_t[N - 1 - i] else 0 for i in range(N // 2)))
