def room(n):
    room_list = [0]
    for i in range(n):
        room_list.append(0)

    if n == 1:
        return 0

    j = 2
    while(j <= n):
        for i in range(j, n+1):
            if i % j == 0:
                if room_list[i] == 1:
                    room_list[i] = 0
                else:
                    room_list[i] = 1
            else:
                continue

        j += 1
    return room_list.count(0)-1


t = int(input())

input_list = []
for i in range(t):
    input_list.append(int(input()))

for i in range(t):
    print(room(input_list[i]))
