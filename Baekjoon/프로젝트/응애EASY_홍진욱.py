def count_greeting_members(N, M, K, greetings):
    members = [0] * N
    for i in greetings:
        members[i] = 1
    
    for _ in range(K):
        temp = members[:]
        for i in range(N):
            if temp[i] == 1:
                if temp[i-1] == 1 and temp[(i+1)%N] == 1:
                    members[i] = 0
                elif temp[i-1] == 1 or temp[(i+1)%N] == 1:
                    members[i] = 1
                else:
                    members[i] = 0
            else:
                if temp[i-1] == 1 and temp[(i+1)%N] == 1:
                    members[i] = 1
    return members.count(1)

N, M, K = map(int, input().split())
greetings = [int(input()) for _ in range(M)]

print(count_greeting_members(N, M, K, greetings))
